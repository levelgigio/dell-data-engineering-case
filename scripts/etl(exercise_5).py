from libs.create_vaccination_table import create_vaccination_table
from libs.get_vaccination_data import get_vaccination_data
from libs.insert_csv_data_to_db import insert_csv_data_to_db

# Vaccination
create_vaccination_table()
get_vaccination_data()
# insert_csv_data_to_db("vaccination.csv", "vaccination_by_country")