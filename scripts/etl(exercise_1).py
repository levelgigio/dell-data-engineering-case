from libs.create_covid_table import create_covid_table
from libs.create_world_table import create_world_table
from libs.insert_csv_data_to_db import insert_csv_data_to_db
from libs.get_covid_data import get_covid_data
from libs.get_world_data import get_world_data

# Covid
create_covid_table()
get_covid_data()
insert_csv_data_to_db('covid.csv', 'covid_19_cases_and_death')

# World
create_world_table()
get_world_data()
insert_csv_data_to_db('world.csv', 'countries_of_the_world')
