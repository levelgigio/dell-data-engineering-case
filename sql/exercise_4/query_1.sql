-- Query #1
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
    MAX_RATE_14_DAY DESC
LIMIT
    1;
    