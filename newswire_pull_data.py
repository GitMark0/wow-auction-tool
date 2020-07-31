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
mycursor.execute("SHOW COLUMNS FROM tblItemHistoryDaily")
column_names = mycursor.fetchall()

# mycursor.execute("SELECT * FROM tblItemHistoryMonthly WHERE item = 65891 ORDER BY month ASC LIMIT 100")
# myresult = mycursor.fetchall()
query = "SELECT DBItm.name_enus, IHD.* FROM tblItemHistoryDaily IHD JOIN tblDBCItem DBItm ON IHD.item = DBItm.id JOIN tblRealm RLM ON RLM.house = IHD.house WHERE RLM.region = 'EU' AND RLM.slug = 'doomhammer' AND DBItm.name_enus IN ('Monelite Ore') ORDER BY `when` DESC"
mycursor.execute(query)
monelite_prices = mycursor.fetchall()

header = ['item_name', 'item_id', 'house', 'date', 'pricemin', 'priceavg', 'pricemax', 'pricestart', 'priceend',
          'quantitymin', 'quantityavg', 'quantitymax']
# mycursor.execute("SELECT * FROM tblWowToken WHERE YEAR(`when`)>2019 AND region='EU'")
# myresult = mycursor.fetchall()

with open('monelite-ore-prices.csv', 'w+', newline='') as c:
    cw = csv.writer(c)
    cw.writerow(header)
    for x in monelite_prices:
        cw.writerow(x)
