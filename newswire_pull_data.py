import mysql.connector
import csv

# Connect to database newsstand
mydb = mysql.connector.connect(
    host="newswire.theunderminejournal.com",
    user="anonymous",
    password="",
    database="newsstand"
)

mycursor = mydb.cursor()

# Get column names
mycursor.execute("SHOW COLUMNS FROM tblWowToken")
column_names = mycursor.fetchall()

# mycursor.execute("SHOW TABLES")
mycursor.execute("SELECT * FROM tblWowToken WHERE YEAR(`when`)>2019 AND region='EU'")
myresult = mycursor.fetchall()

c = csv.writer(open('wow-token_2020.csv', 'w'))
for x in myresult:
    c.writerow(x)
