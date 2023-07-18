from sense_hat import SenseHat
sense = SenseHat()
import datetime
import time
import sqlite3

sqlite_file="database.db"
conn = sqlite3.connect(sqlite_file)
c=conn.cursor()
try:
    c.execute("CREATE TABLE data (name TEXT,description TEXT,value REAL,date DATETIME)")

except:
    print("already exists")
    
for i in range(0,10000):
    pressure=sense.get_pressure()
    humidity=sense.get_humidity()
    Temp_Pressure = sense.get_temperature_from_pressure()
    Temp_Humidity = sense.get_temperature_from_humidity()
    North = sense.get_compass()
    Raw = sense.get_compass_raw()
    Gyro = sense.get_gyroscope()
    Accel = sense.get_accelerometer()
    Ori_deg = sense.get_orientation_degrees()
    Ori_rad = sense.get_orientation_radians()
    
    measure_time=datetime.datetime.utcnow()

    query_pressure=" INSERT INTO data(name, description, value,date) VALUES ('pressure', 'pressure_sensor',{0},'{1}')".format(pressure,measure_time)
    query_humidity=" INSERT INTO data (name, description, value,date) VALUES ('humidity', 'humidity_sensor',{0},'{1}')".format(humidity,measure_time)
    query_Temp_Pressure=" INSERT INTO data(name, description, value,date) VALUES ('Temp_Pressure', 'Temp_Pressure_sensor',{0},'{1}')".format(Temp_Pressure,measure_time)
    query_Temp_Humidity=" INSERT INTO data (name, description, value,date) VALUES ('Temp_Humidity', 'Temp_Humidity_sensor',{0},'{1}')".format(Temp_Humidity,measure_time)
    query_North=" INSERT INTO data(name, description, value,date) VALUES ('North', 'North_sensor',{0},'{1}')".format(North,measure_time)
    query_Raw_x=" INSERT INTO data (name, description, value,date) VALUES ('Raw', 'Raw_sensor_x',{0},'{1}')".format(Raw['x'],measure_time)
    query_Raw_y=" INSERT INTO data (name, description, value,date) VALUES ('Raw', 'Raw_sensor_y',{0},'{1}')".format(Raw['y'],measure_time)
    query_Raw_z=" INSERT INTO data (name, description, value,date) VALUES ('Raw', 'Raw_sensor_z',{0},'{1}')".format(Raw['z'],measure_time)
    query_Gyro_pitch=" INSERT INTO data(name, description, value,date) VALUES ('Gyro', 'Gyro_sensor_pitch',{0},'{1}')".format(Gyro['pitch'],measure_time)
    query_Gyro_roll=" INSERT INTO data(name, description, value,date) VALUES ('Gyro', 'Gyro_sensor_roll',{0},'{1}')".format(Gyro['roll'],measure_time)
    query_Gyro_yaw=" INSERT INTO data(name, description, value,date) VALUES ('Gyro', 'Gyro_sensor_yaw',{0},'{1}')".format(Gyro['yaw'],measure_time)
    query_Accel_pitch=" INSERT INTO data (name, description, value,date) VALUES ('Accel', 'Accel_sensor_pitch',{0},'{1}')".format(Accel['pitch'],measure_time)
    query_Accel_roll=" INSERT INTO data (name, description, value,date) VALUES ('Accel', 'Accel_sensor_roll',{0},'{1}')".format(Accel['roll'],measure_time)
    query_Accel_yaw=" INSERT INTO data (name, description, value,date) VALUES ('Accel', 'Accel_sensor_yaw',{0},'{1}')".format(Accel['yaw'],measure_time)
    query_Ori_deg_pitch=" INSERT INTO data(name, description, value,date) VALUES ('Ori_deg', 'Ori_deg_sensor_pitch',{0},'{1}')".format(Ori_deg['pitch'],measure_time)
    query_Ori_deg_roll=" INSERT INTO data(name, description, value,date) VALUES ('Ori_deg', 'Ori_deg_sensor_roll',{0},'{1}')".format(Ori_deg['roll'],measure_time)
    query_Ori_deg_yaw=" INSERT INTO data(name, description, value,date) VALUES ('Ori_deg', 'Ori_deg_sensor_yaw',{0},'{1}')".format(Ori_deg['yaw'],measure_time)
    query_Ori_rad_pitch=" INSERT INTO data (name, description, value,date) VALUES ('Ori_rad', 'Ori_rad_sensor_pitch',{0},'{1}')".format(Ori_rad['pitch'],measure_time)
    query_Ori_rad_roll=" INSERT INTO data (name, description, value,date) VALUES ('Ori_rad', 'Ori_rad_sensor_roll',{0},'{1}')".format(Ori_rad['roll'],measure_time)
    query_Ori_rad_yaw=" INSERT INTO data (name, description, value,date) VALUES ('Ori_rad', 'Ori_rad_sensor_yaw',{0},'{1}')".format(Ori_rad['yaw'],measure_time)

    



    c.execute(query_pressure)
    c.execute(query_humidity)
    c.execute(query_Temp_Pressure)
    c.execute(query_Temp_Humidity)
    c.execute(query_North)
    c.execute(query_Raw_x)
    c.execute(query_Raw_y)
    c.execute(query_Raw_z)
    
    c.execute(query_Gyro_pitch)
    c.execute(query_Gyro_roll)
    c.execute(query_Gyro_yaw)
    c.execute(query_Accel_pitch)
    c.execute(query_Accel_roll)
    c.execute(query_Accel_yaw)
    c.execute(query_Ori_deg_pitch)
    c.execute(query_Ori_deg_roll)
    c.execute(query_Ori_deg_yaw)
    c.execute(query_Ori_rad_pitch)
    c.execute(query_Ori_rad_roll)
    c.execute(query_Ori_rad_yaw)

    time.sleep(1) 

conn.commit()
conn.close()
