from flask import Flask
from flask import request
from flask import jsonify
from sense_hat import SenseHat
import datetime
import sqlite3
from flask import render_template

sense = SenseHat()
sense.clear()

sqlite_file="/home/pi/Desktop/P3/sensorsP5.db"
sqlite_filedata="/home/pi/Desktop/P3/dataP5.db"
conn = sqlite3.connect(sqlite_file)
c=conn.cursor()

app = Flask(__name__)

# @app.route('/')
@app.route('/hello')
def hello(name=None):
    group=request.args.get('group')
    data={}
    query_pressure=" SELECT * FROM sensors LIMIT 20"
#     query_humidity=" INSERT INTO datitos (name, description, value,date) VALUES ('humidity', 'humidity_sensor',{0},'{1}')".format(humidity,measure_time)
    a=c.execute(query_pressure)
    data=a.fetchall()
    conn.commit()
    conn.close()
    return render_template('FINALPROJECT.html', name=group,data=data)
# def main_route():
#     return 'ICT: Raspberry PI SenseHat API'
@app.route('/hello/<string:id>')
def show_post(id):

    conns = sqlite3.connect(sqlite_filedata)
    c=conns.cursor()
    
    data={}
    query_pressures=" SELECT "+{id}+" FROM data LIMIT 50"
#     query_humidity=" INSERT INTO datitos (name, description, value,date) VALUES ('humidity', 'humidity_sensor',{0},'{1}')".format(humidity,measure_time)
    a=c.execute(query_pressures)
    data=a.fetchall()
    conns.commit()
    conns.close()
    
    
    return render_template('FPSENS.html', data=data)