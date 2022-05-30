# Setup
A Postgres Server was created using Docker using the following commands:
    ```docker pull postgres```
Then:
    ```docker run --name dellPostgresDb -p 5455:5432 -e POSTGRES_USER=dellPostgresUser -e POSTGRES_PASSWORD=dellPostgresPW -e POSTGRES_DB=test -d postgres```

# Exercise #1
Solution can be achieved by running the following commands:
    ```python scripts/etl\(exercise_1\).py```

# Exercise #2
Solution can be achieved by scheduling the run of the following command in a daily manner:
    ```python scripts/get_latest_covid_data\(exercise_2\).py```
This can be done via a CRON schedule, Airflow, etc.

# Exercises #3 and #4
Solutions can be achieved by running the SQL codes directly inside pgAdmin's Query Tool

# Exercise #5
Solution can be achieved by running the following commands:
    ```python scripts/etl\(exercise_5\).py```
Then we can create a view that enriches the Covid "Data source 1: Covid Data" with the vaccination data ingested by running the SQL code directly inside pgAdmin's Query Tool

Thank you!