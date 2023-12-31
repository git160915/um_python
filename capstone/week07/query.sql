WITH top_10_ev AS (
	SELECT make, ROUND(CAST(COUNT(*) AS FLOAT) / (SUM(COUNT(*)) OVER() / 100), 2) AS percentage_of_total
	FROM raw_ev_population_data
	GROUP BY make
	ORDER BY 2 DESC
	LIMIT 10
),

top_10_ev_with_rownum AS (
	SELECT *, ROW_NUMBER() OVER() as rownum
	FROM top_10_ev
)

SELECT make, percentage_of_total
FROM top_10_ev_with_rownum
WHERE make = 'TESLA'
UNION ALL
SELECT 'Others (next 9 competitors)', SUM(percentage_of_total) as percentage_of_total
FROM top_10_ev_with_rownum
WHERE rownum > 1
UNION ALL
SELECT 'Top 10', SUM(percentage_of_total) as percentage_of_total
FROM top_10_ev_with_rownum
WHERE rownum > 0