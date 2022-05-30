import requests
from datetime import datetime
from pathlib import Path
import pandas as pd


def get_vaccination_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    response = requests.get(url).json()

    # Add metadata to json indicating when it was downloaded
    metadata = {"meta_extracted_date": datetime.today().strftime("%Y-%m-%d")}
    for row in response:
        row.update(metadata)

    # Creating a dataframe out of it
    df = pd.DataFrame(response)

    # Selecting only a few extra information from it
    df = df[
        [
            "location",
            "date",
            "tests_per_case",
            "tests_units",
            "total_vaccinations",
            "people_vaccinated",
            "people_fully_vaccinated",
        ]
    ]

    # Saving downloaded vaccination data
    df.to_csv(
        Path(__file__).parent / "../data/vaccination.csv",
        index=False,
        sep="\t",
        decimal=".",
    )

    print("Data downloaded successfully........")


# get_vaccination_data()
