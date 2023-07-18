from flask import Flask
from flask import request
from flask import jsonify
from sense_hat import SenseHat
import datetime
import sqlite3
from flask import render_template

sense = SenseHat()
sense.clear()

sqlite_file="/home/pi/Desktop/P3/dataP5.db"
conn = sqlite3.connect(sqlite_file)
c=conn.cursor()

app = Flask(__name__)

# @app.route('/')
@app.route('/measures')
def measures():
   
    data={}
    query_pressure=query_pressure=" SELECT * FROM data WHERE  date BETWEEN '2023-05-25 11:13:40' AND '2023-05-25 11:13:45.0'"
#     query_humidity=" INSERT INTO datitos (name, description, value,date) VALUES ('humidity', 'humidity_sensor',{0},'{1}')".format(humidity,measure_time)
    a=c.execute(query_pressure)
    data=a.fetchall()
    conn.commit()
    conn.close()
    return jsonify(data)
# def main_route():
#     return 'ICT: Raspberry PI SenseHat API'
@app.route('/measures/<string:id>')
def show_post(id):
    
    
    data={}
    query_pressure=" SELECT "+{id}+" FROM data WHERE  date BETWEEN '2023-05-25 11:13:40' AND '2023-05-25 11:13:45.0'"
#     query_humidity=" INSERT INTO datitos (name, description, value,date) VALUES ('humidity', 'humidity_sensor',{0},'{1}')".format(humidity,measure_time)
    a=c.execute(query_pressure)
    data=a.fetchall()
    conn.commit()
    conn.close()
    
    
    return jsonify(data)

@app.route('/live/sensor_id')
def show_post():
    
    
    data={}
    
    query_humidity=" INSERT INTO data (name, description, value,date) VALUES ('humidity', 'humidity_sensor',{0},'{1}')"".format(humidity,measure_time)"
    query_humidityselect=" SELECT * FROM data WHERE  date CURRENT_TIMESTAMP AT TIME ZONE 'UTC'"
    a=c.execute(query_humidity)
    a=c.execute(query_humidityselect)
    data=a.fetchall()
    conn.commit()
    conn.close()
    
    
    return jsonify(data)

@app.route('/live/<string:new_text>')
def show_post(new_text):

    b=(0,0,255)
    r=(255,0,0)
    sense.show_message({new_text}, text_colour=r, back_colour=b,scroll_speed=0.05)
    return jsonify(new_text)