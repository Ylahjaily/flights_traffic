from flask import Flask, render_template
app = Flask(__name__)

from connect import mydb
import pymysql
import pandas as pd

cursor = mydb.cursor()

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/flights")
def flights():
    sql = "SELECT * FROM Flights"
    cursor.execute(sql)
    data = cursor.fetchall()

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
    "id"
    ]


    df = pd.DataFrame(data, columns = columns)

    return render_template('flights.html', tables = [df.to_html()])


@app.route("/flights/maintened")
def cancelledflights():
    sql = "SELECT * FROM Flights"
    cursor.execute(sql)
    data = cursor.fetchall()

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
    "id"
    ]

    df = pd.DataFrame(data, columns = columns)

    maintened_flights = df['dep_time'] != ''

    frame = df[maintened_flights]

    return render_template('flights.html', tables = [frame.to_html()])

@app.route("/airports")
def airports():
    sql = "SELECT * FROM Airports"
    cursor.execute(sql)
    data = cursor.fetchall()

    columns = [
    "faa",
    "name",
    "lat",
    "lon",
    "alt",
    "tz",
    "dst",
    "tzone"
    ]


    df = pd.DataFrame(data, columns = columns)

    return render_template('airports.html', tables = [df.to_html()])

@app.route("/airports/dst")
def airports_dst():
    sql = "SELECT * FROM Airports"
    cursor.execute(sql)
    data = cursor.fetchall()

    columns = [
    "faa",
    "name",
    "lat",
    "lon",
    "alt",
    "tz",
    "dst",
    "tzone"
    ]


    df = pd.DataFrame(data, columns = columns)
    is_airport_with_no_dst = df['dst'] == 'N'
    df[is_airport_with_no_dst]

    return render_template('airports.html', tables = [df.to_html()])

@app.route("/airports/tzone")
def airports_tzone():
    sql = "SELECT * FROM Airports"
    cursor.execute(sql)
    data = cursor.fetchall()

    columns = [
    "faa",
    "name",
    "lat",
    "lon",
    "alt",
    "tz",
    "dst",
    "tzone"
    ]


    df = pd.DataFrame(data, columns = columns)
    is_airport_with_tzone = df['tzone'] == '\\N'
    df[is_airport_with_tzone] 
  
    return render_template('airports.html', tables = [df.to_html()])

@app.route("/airlines")
def airlines():
    sql = "SELECT * FROM Airlines"
    cursor.execute(sql)
    data = cursor.fetchall()

    columns = [
    "carrier",
    "name"
    ]

    df = pd.DataFrame(data, columns = columns)

    return render_template('flights.html', tables = [df.to_html()])

@app.route("/planes")
def planes():
    sql = "SELECT * FROM Planes"
    cursor.execute(sql)
    data = cursor.fetchall()

    columns = [
    "tailnum",
    "year",
    "type",
    "manufacturer",
    "model",
    "engines",
    "seats",
    "speed",
    "engine"
    ]

    df = pd.DataFrame(data, columns = columns)

    return render_template('flights.html', tables = [df.to_html()])

@app.route("/weather")
def weather():
    sql = "SELECT * FROM Weather"
    cursor.execute(sql)
    data = cursor.fetchall()

    columns = [
    "origin",
    "year",
    "month",
    "day",
    "hour",
    "temp",
    "dewp",
    "humid",
    "wind_dir",
    "wind_speed",
    "wind_gust",
    "precip",
    "pressure",
    "visib",
    "time_hour"
    ]

    df = pd.DataFrame(data, columns = columns)

    return render_template('flights.html', tables = [df.to_html()])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
