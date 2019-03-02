/*Get a general look for the first 50 entries of the data*/
SELECT COUNT(*) FROM dbo.wine
SET ROWCOUNT 50;

/*Create a column named value which divides the points by it's price to get the points per unit of price*/
ALTER TABLE dbo.wine
ADD value float;

/*Saturate the column with the calculated values for each instance*/
UPDATE dbo.wine SET value =CAST(points AS float) / CAST(price AS float);

/*How many distinct country values there are*/
SELECT COUNT(DISTINCT(country)) FROM dbo.wine

/*How many distinct varieties of wine there are*/
SELECT COUNT(DISTINCT(variety)) FROM dbo.wine

/*Create a function to show the 3 most biggest producers of wine in this data*/
SELECT country,COUNT(points) FROM dbo.wine
GROUP BY country
ORDER BY 2 DESC
SET ROWCOUNT 3;

/*HOW MANY DISTINCT country values there are*/
SELECT COUNT(*) AS 'Total' FROM dbo.wine
WHERE province IS NOT NULL;

/*Calculate how many entries these 3 countries represent*/
SELECT COUNT(*) AS 'Total for top 3' FROM dbo.wine
WHERE province IS NOT NULL AND country = 'US' OR country='Italy' OR country='France';
/*From this we can see that the top 3 countries represent over two thirds of the data in the model, hence determining the model for these 3 countries will be the most important*/

/*HOW MANY DISTINCT country values there are*/
SELECT points, MAX(value) AS 'Value' FROM dbo.wine
GROUP BY points
ORDER BY points DESC;
