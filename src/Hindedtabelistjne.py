import sqlite3
import pandas
conn = sqlite3.connect("hinded.db")
dataframe = pandas.read_sql_query ("SELECT * FROM hinded", conn)
print(dataframe)