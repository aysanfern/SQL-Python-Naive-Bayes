ALTER TABLE dbo.wine
ADD value float;
UPDATE dbo.wine SET value =CAST(points AS float) / CAST(price AS float);

SELECT * FROM dbo.wine
SET ROWCOUNT 50;
/*HOW MANY DISTINCT country values there are*/
SELECT COUNT(DISTINCT(country)) FROM dbo.wine
/*How many distinct varieties of wine there are*/
SELECT COUNT(DISTINCT(variety)) FROM dbo.wine

SELECT DISTINCT(country) FROM dbo.wine

SELECT country,COUNT(points) FROM dbo.wine
GROUP BY country
ORDER BY 2 DESC;


SELECT points, MAX(value) AS 'Value' FROM dbo.wine
GROUP BY points
ORDER BY points DESC;

