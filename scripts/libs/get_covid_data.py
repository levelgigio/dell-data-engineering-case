import requests
from datetime import datetime
from pathlib import Path
import pandas as pd


def get_covid_data():
    url = r"https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/json"
    response = requests.get(url).json()

    # Add metadata to json indicating when it was downloaded
    metadata = {"meta_extracted_date": datetime.today().strftime("%Y-%m-%d")}
    for row in response:
        row.update(metadata)

    # Creating a dataframe out of it
    df = pd.DataFrame(response)

    # Making sure that the columns are in the right order
    df = df[
        [
            "country",
            "country_code",
            "continent",
            "population",
            "indicator",
            "weekly_count",
            "year_week",
            "rate_14_day",
            "cumulative_count",
            "source",
            "note",
            "meta_extracted_date",
        ]
    ]

    # Saving downloaded covid data
    df.to_csv(
        Path(__file__).parent / "../data/covid.csv", index=False, sep="\t", decimal="."
    )

    print("Data downloaded successfully........")


# get_covid_data()
