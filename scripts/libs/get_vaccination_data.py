import requests
from datetime import datetime
from pathlib import Path
import pandas as pd


def get_vaccination_data():
    ''' 
    This function was intended to download the file using requests library
    but it was not working so I downloaded it manually and now this function
    only clean up a bit the file
    '''
    # url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    # response = requests.get(url).json()

    # # Add metadata to json indicating when it was downloaded
    # metadata = {"meta_extracted_date": datetime.today().strftime("%Y-%m-%d")}
    # for row in response:
    #     row.update(metadata)

    # # Creating a dataframe out of it
    # df = pd.DataFrame(response)

    # File manually downloaded
    df = pd.read_csv(Path(__file__).parent / f"../data/owid-covid-data.csv")

    # Manually adding metadata
    df["meta_extracted_date"] = datetime.today().strftime("%Y-%m-%d")

    # Selecting only a few extra information from it
    df = df[
        [
            "location",
            "date",
            "tests_per_case",
            "total_vaccinations",
            "people_vaccinated",
            "people_fully_vaccinated",
            "meta_extracted_date"
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
