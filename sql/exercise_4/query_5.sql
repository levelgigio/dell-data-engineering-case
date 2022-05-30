-- Query #5
WITH NUMBER_OF_EACH_ROW_CTE AS (
    SELECT
        COUNT(*) AS QTY,
        COUNTRY,
        COUNTRY_CODE,
        CONTINENT,
        INDICATOR,
        YEAR_WEEK,
        SOURCE
    FROM
        public.covid_19_cases_and_death
    GROUP BY
        COUNTRY,
        COUNTRY_CODE,
        CONTINENT,
        INDICATOR,
        YEAR_WEEK,
        SOURCE
)
SELECT
    *
FROM
    NUMBER_OF_EACH_ROW_CTE
WHERE
    QTY > 1;
