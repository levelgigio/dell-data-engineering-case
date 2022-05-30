from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from pathlib import Path


def get_world_data():
    # Getting data from Kaggle
    api = KaggleApi()
    api.authenticate()

    path = Path(__file__).parent / "../data"
    api.dataset_download_file(
        "fernandol/countries-of-the-world", "countries of the world.csv", path=path
    )

    # Cleaning up data
    df = pd.read_csv("../data/countries%20of%20the%20world.csv", decimal=",")
    cols = ["Country", "Region"]
    df[cols] = df[cols].apply(lambda x: x.str.strip())

    # Saving cleaned data
    df.to_csv(path / "world.csv", index=False, sep="\t", decimal=".")

    print("Data downloaded successfully........")


# get_world_data()
