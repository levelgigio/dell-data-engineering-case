import libs.connect_2_db as connect_2_db
from libs.get_covid_data import get_covid_data
from libs.insert_csv_data_to_db import insert_csv_data_to_db
from pathlib import Path
import pandas as pd


def get_latest_covid_data():
    conn = connect_2_db.connect2db()

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Query for latest YEAR_WEEK in DB
    sql = f"""
            SELECT MAX(CAST(REPLACE(YEAR_WEEK, '-', '') AS INTEGER))
            FROM public.covid_19_cases_and_death 
            """

    # Executing SQL
    cursor.execute(sql)
    db_max_year_week = cursor.fetchall()

    # Downloading new covid data
    get_covid_data()

    # Load downloaded json file
    df = pd.read_csv(Path(__file__).parent / "data/covid.csv", sep="\t")

    # Find current max YEAR_WEEK
    series = pd.to_numeric(df["year_week"].str.replace("-", ""))
    source_max_year_week = series.max()

    # Checking if we need to delete old data that may be updated
    if db_max_year_week == source_max_year_week:
        print("Deleting rows that may duplicate.........")
        sql = f"""
            DELETE 
            FROM public.covid_19_cases_and_death 
            WHERE CAST(REPLACE(YEAR_WEEK, '-', '') AS INTEGER) = {source_max_year_week}
            """
        # Executing SQL
        cursor.execute(sql)

    # Creating a new json file only with new records
    df = df[
        df["year_week"]
        == str(source_max_year_week)[:4] + "-" + str(source_max_year_week)[4:]
    ]
    df.to_csv(
        Path(__file__).parent / "data/latest_covid.csv",
        index=False,
        sep="\t",
        decimal=".",
    )
    print("Saved latest covid data..........")

    # Inserting new records in DB
    insert_csv_data_to_db("latest_covid.csv", "covid_19_cases_and_death")

    # Commiting and closing
    conn.commit()
    conn.close()

    print("Data inserted successfully........")


get_latest_covid_data()
