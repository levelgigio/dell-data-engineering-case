import libs.connect_2_db as connect_2_db


def create_vaccination_table():
    # Establishing the connection
    conn = connect_2_db.connect2db()

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping COVID table if already exists.
    cursor.execute("DROP TABLE IF EXISTS VACCINATION_BY_COUNTRY")

    # Creating table as per requirement
    sql = """
    CREATE TABLE IF NOT EXISTS VACCINATION_BY_COUNTRY
    (
    LOCATION CHAR(50),
    FULL_DATE DATE,
    TESTS_PER_CASE NUMERIC(18,3),
    TESTS_UNITS NUMERIC(18,3),
    TOTAL_VACCINATIONS NUMERIC(18,3),
    PEOPLE_VACCINATED NUMERIC(18,3),
    PEOPLE_FULLY_VACCINATED NUMERIC(18,3),
    META_EXTRACTED_DATE DATE
    )"""

    # Executing SQL
    cursor.execute(sql)
    conn.commit()
    conn.close()

    print("Table created successfully........")


# create_covid_table()
