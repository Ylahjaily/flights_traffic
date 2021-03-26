import pymysql
import pandas as pd

from connect import mydb

cursor = mydb.cursor()

sql = "SELECT * FROM Flights"
cursor.execute(sql)
data = cursor.fetchall() 

print(type(data))

columns = [
"year",
"month",
"day",
"dep_time",
"sched_dep_time",
"dep_delay",
"arr_time",
"sched_arr_time",
"arr_delay",
"carrier",
"flight",
"tailnum",
"origin",
"dest",
"air_time",
"distance",
"hour",
"minute",
"time_hour",
"empty"
]

df = pd.DataFrame(data, columns = columns)

print(df)
