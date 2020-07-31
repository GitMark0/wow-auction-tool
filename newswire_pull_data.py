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

# Get table names
mycursor.execute("SHOW TABLES")
table_names = mycursor.fetchall()

# Get column names
mycursor.execute("SHOW COLUMNS FROM tblItemHistoryMonthly")
column_names = mycursor.fetchall()

# mycursor.execute("SELECT * FROM tblItemHistoryMonthly WHERE item = 65891 ORDER BY month ASC LIMIT 100")
# myresult = mycursor.fetchall()

mycursor.execute("SELECT DISTINCT(month) AS Months FROM tblItemHistoryMonthly ORDER BY Months DESC")
distinct_month_vals = mycursor.fetchall()
print('Hello')
# mycursor.execute("SELECT * FROM tblWowToken WHERE YEAR(`when`)>2019 AND region='EU'")
# myresult = mycursor.fetchall()

# c = csv.writer(open('wow-token_2020.csv', 'w'))
# for x in myresult:
#     c.writerow(x)
