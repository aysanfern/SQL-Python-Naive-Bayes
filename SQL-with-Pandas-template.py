#Importing necessary libraries
import pandas as pd
import pyodbc

#Server and Database used in the MSSQL server is imputed in this string
conn_string= (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-SHDVFGO\SQLEXPRESS;'
    r'DATABASE=Consumer;'
    r'Trusted_Connection=yes;'
)

#Connection with string is established
conn=pyodbc.connect(conn_string)

#Performing a query that will be imported as a dataframe here
query='''SELECT points, MAX(value) AS 'Value' FROM dbo.wine
GROUP BY points
ORDER BY points DESC;'''

#Reading the query and creating a resulting dataframe
df = pd.read_sql_query(query,conn)
