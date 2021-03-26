import mysql.connector

mydb = mysql.connector.connect(
  host="mysql-ipssi.alwaysdata.net",
  user="ipssi",
  database="ipssi_trafic",
  password="bikjir-1Vevto-dowvex"
)

print(mydb)

table = "SHOW TABLES"
airlines = "SELECT * FROM Airlines"
planes = "SELECT * FROM Planes"
airports = "SELECT * FROM Airports"
flights = "SELECT * FROM Flights"
weather = "SELECT * FROM Weather"

