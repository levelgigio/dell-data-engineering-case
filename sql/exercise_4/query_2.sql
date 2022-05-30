-- Query #2
-- This query returns 10 rows, but we have more than 10 countries tied at 0 cases
-- so, might be useful to query for countries with 0 cases other than top 10.
SELECT
    COUNTRY,
    MAX(RATE_14_DAY) AS MAX_RATE_14_DAY
FROM
    public.covid_19_cases_and_death
WHERE
    YEAR_WEEK = TO_CHAR('2020-07-31' :: DATE, 'YYYY-WW')
    AND INDICATOR = 'cases'
    AND COUNTRY NOT LIKE '%(total)%'
GROUP BY
    COUNTRY
ORDER BY
    MAX_RATE_14_DAY
LIMIT
    10;