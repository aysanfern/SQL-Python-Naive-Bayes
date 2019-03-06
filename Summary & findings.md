# Summary and findings

SQL- Using MSSQL to analyse the data and gain initial insights prior to further analysis

NaiveBayes&Graph.py - Python file that reads SQL queries and creates graphs explained shown in figure 1 and figure 2. I also used a Naive Bayes classifier that predicts whether a wine is going to be really good (score of 90 or over) or just good (less than 90)
E.g 
The classifier correctly predicts that a review stating
‘ This wine is average’ will be a wine that has a score of less than 90
Whereas a review stating 
‘This wine is exquisite’ will be predicted to have a score of 90 or more.

Figure 1 - Showing how many missing values there are for each of the countries compared to how many non missing values, quite clearly we can see that the US has very few non missing values but accounts for many of the values in total which differs from the other countries, from this insight we can infer that this research was conducted in the US making it easier to obtain the prices for each wine.

Figure 2 - Shows the best value per wine when I define value as points/price. From this graph we can clearly see as the points go up you can expect to have less value in the wine you purchase, however this is no without making the misleading assumption that this point system is a ratio scale, one in which the difference between for example 80 and 81 is the same as 99 to 100 which may not be correct

