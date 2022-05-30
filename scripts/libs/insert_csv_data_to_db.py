import libs.connect_2_db as connect_2_db
import pandas as pd
from pathlib import Path


def insert_csv_data_to_db(filename, tablename):
    # Establishing the connection
    conn = connect_2_db.connect2db()

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Inserting data as per requirement
    path = Path(__file__).parent / f"../data/{filename}"
    with path.open("r") as f:
        next(f)  # Skip the header row.
        # tbl = 'countries_of_the_world'
        cursor.copy_from(f, tablename, sep="\t", null="")

    # Executing SQL
    conn.commit()
    conn.close()

    print("Data inserted successfully........")


# insert_covid_data()
