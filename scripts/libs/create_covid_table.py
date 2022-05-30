import libs.connect_2_db as connect_2_db


def create_covid_table():
    # Establishing the connection
    conn = connect_2_db.connect2db()

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping COVID table if already exists.
    cursor.execute("DROP TABLE IF EXISTS COVID_19_CASES_AND_DEATH")

    # Creating table as per requirement
    sql = """
    CREATE TABLE IF NOT EXISTS COVID_19_CASES_AND_DEATH
    (
    COUNTRY CHAR(50),
    COUNTRY_CODE CHAR(3),
    CONTINENT CHAR(30),
    POPULATION BIGINT,
    INDICATOR CHAR(30),
    WEEKLY_COUNT NUMERIC(18,1),
    YEAR_WEEK CHAR(7),
    RATE_14_DAY NUMERIC(18,12),
    CUMULATIVE_COUNT INT,
    SOURCE TEXT,
    NOTE TEXT,
    META_EXTRACTED_DATE DATE
    )"""

    # Executing SQL
    cursor.execute(sql)
    conn.commit()
    conn.close()

    print("Table created successfully........")


# create_covid_table()
