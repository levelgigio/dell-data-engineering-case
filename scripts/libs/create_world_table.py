import libs.connect_2_db as connect_2_db


def create_world_table():
    # Establishing the connection
    conn = connect_2_db.connect2db()

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping COVID table if already exists.
    cursor.execute("DROP TABLE IF EXISTS COUNTRIES_OF_THE_WORLD")

    # Creating table as per requirement
    sql = """
    CREATE TABLE IF NOT EXISTS COUNTRIES_OF_THE_WORLD
    (
    COUNTRY CHAR(50),
    REGION CHAR(50),
    POPULATION BIGINT,
    AREA_SQ_MI BIGINT,
    POP_DENSITY_PER_SQ_MI NUMERIC(18,1),
    COASTLINE_COAST_OVER_AREA_RATIO NUMERIC(18,2),
    NET_MIGRATION NUMERIC(18,2),
    INFANT_MORTALITY_PER_1000_BIRTHS NUMERIC(18,2),
    GDP_DOLLAR_PER_CAPITA NUMERIC(18,1),
    LITERACY_PERCENT NUMERIC(18,1),
    PHONES_PER_1000 NUMERIC(18,1),
    ARABLE_PERCENT NUMERIC(18,2),
    CROPS_PERCENT NUMERIC(18,2),
    OTHER_PERCENT NUMERIC(18,2),
    CLIMATE NUMERIC(18,1),
    BIRTHRATE NUMERIC(18,2),
    DEATHRATE NUMERIC(18,2),
    AGRICULTURE NUMERIC(18,3),
    INDUSTRY NUMERIC(18,3),
    SERVICE NUMERIC(18,3)
    )"""

    # Executing SQL
    cursor.execute(sql)
    conn.commit()
    conn.close()

    print("Table created successfully........")


# create_world_table()
