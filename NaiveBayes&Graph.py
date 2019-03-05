import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import numpy as np

#Server and Database used in the MSSQL server is imputed in this string
conn_string= (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-SHDVFGO\SQLEXPRESS;'
    r'DATABASE=Consumer;'
    r'Trusted_Connection=yes;'
)

#Connection with previous string is established
conn=pyodbc.connect(conn_string)

#Performing a query that will be imported as a dataframe here
query='''SELECT points, MAX(value) AS 'value' FROM dbo.wine
GROUP BY points
ORDER BY points DESC;'''

query2='''SELECT country,points,price,value,variety FROM dbo.wine
WHERE country='US' OR country ='France' OR country='Italy' 
'''
query3= '''SELECT country,points,price,value,variety FROM dbo.wine
WHERE (price IS NULL) 
AND
(country='US'
OR
country='France'
OR 
country='Italy')
'''

query4='''
SELECT country,price FROM dbo.wine
WHERE (price IS NOT NULL) 
AND
(country='US'
OR
country='France'
OR 
country='Italy')
'''


query5= '''
SELECT * FROM dbo.wine
WHERE description IS NOT NULL;
'''
#Reading the query and creating a resulting dataframe
df = pd.read_sql_query(query,conn)
df2= pd.read_sql_query(query2,conn)
df3=pd.read_sql_query(query3,conn)
df4=pd.read_sql_query(query4,conn)
df5=pd.read_sql_query(query5,conn)

#Creates a dataframe that tells you how much is grouped by each country
dfx=df3.groupby(('country')).size().reset_index(name='counts')

x1=dfx['country']
y1=dfx['counts']
dfy=df4.groupby(('country')).size().reset_index(name='counts')
x2=dfy['country']
y2=dfy['counts']



ind = np.arange(3)  # the x locations for the groups
width = 0.25  # the width of the bars


fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2,y1,width, label='Missing values',color='salmon')
rects2 = ax.bar(ind + width/2,y2,width, label='Non missing values',color='mediumspringgreen')
ax.set_xticks(ind)
ax.set_xticklabels(x1)
fig.set_size_inches(5, 5)
plt.legend()
plt.xlabel('Country', fontsize=13)
plt.title('Missing vs Non missing per Country', fontsize = 15)
plt.savefig('figure1.jpeg')
plt.show()


x=df['points']
y=df['value']

#Plotting the maximum value from each point
plt.title('Best value vs points',fontsize=15)
plt.xlabel('Points', fontsize=13)
plt.ylabel('Value',fontsize=13)
plt.bar(x,y,color='mediumspringgreen')
plt.savefig('figure2.jpeg')
#From this graph we can clearly see as the points go up you can expect to have less value in the wine you purchase, however this is no without making the misleading assumption that this point system is an interval scale, one in which the difference between for example 80 and 81 is the same as 99 to 100 which may not be correct

#Now I am going to try and be able to see if I can use the description of the data to determine wether a wine is 'Good (score <90)' or 'Really good (score>=90)'

#Creating the labels for the training data
points=df5['points']       
labels=[0 if points[i]<90 else 1 for i in range(len(points))]
df5['labels']=labels


#Creating a list of descriptions
description=df5['description'].tolist()

#Creating a count vectorizer to start a Naive Bayes Classifier
from sklearn.feature_extraction.text import CountVectorizer
counter= CountVectorizer()
counter.fit(description)
training_counts=counter.transform(description)
print(counter.vocabulary_)


from sklearn.naive_bayes import MultinomialNB

classifier=MultinomialNB()
review="This wine was exquisite!"
review_counts = counter.transform([review])
classifier.fit(training_counts,labels)



classifier.predict(review_counts)
classifier.predict_proba(review_counts)
