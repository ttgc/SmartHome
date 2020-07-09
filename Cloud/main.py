#!usr/bin/env python3
#-*-coding:utf-8-*-

import psycopg2
import time
import urllib3
from edgeRequest import getTemperature

dbname="Cloud"
username_db="root"
password_db="root"

default_Location="Paris"
measure_rate=60
def run():
    urllib3.disable_warnings()
    connexion = init_db()
    house_id = getHouseID(connexion)

    print("Starting aquisition on edge, House n"+str(house_id))
    while(True):

        stats= getTemperature()
        insert_data(connexion, house_id ,stats)
        time.sleep(measure_rate)
    print("Stopping aquisition")


        
    

def init_db():
    
   
    conn = psycopg2.connect(host="localhost",database=dbname, user=username_db, password=password_db)
    db_cursor = conn.cursor()
    
    commands = (
    """
        CREATE TABLE IF NOT EXISTS Houses (
            house_id SERIAL PRIMARY KEY,
            location VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS GeoTemp (
            measure_id SERIAL PRIMARY KEY,
            house_id SERIAL,
            temperature_avg FLOAT(5) NOT NULL,
            temperature_unit CHAR,
            delta FLOAT(5),
            clim_duration FLOAT(2),
            heat_duration FLOAT(2),
            date VARCHAR(50),
            FOREIGN KEY (house_id) REFERENCES Houses (house_id)
        )
        """)
       
    for command in commands:
        db_cursor.execute(command)
    db_cursor.close()
    conn.commit()

    return conn

def insert_data(conn, house_id, request):
    db_cursor=conn.cursor()
    json = request.json()
    temp_avg = json.get("average")
    temp_delta= json.get("std_deviation")
    clim_duration= json.get("clim_duration")
    heat_duration= json.get("heat_duration")
    year= json.get("year")
    temperature_unit= json.get("temperature_unit")
    

    command= """INSERT INTO GeoTemp(house_id, temperature_avg, temperature_unit, delta,clim_duration,heat_duration,date)
             VALUES("""+str(house_id)+", "+str(temp_avg)+", '"+temperature_unit+"', "+str(temp_delta)+", "+str(clim_duration)+", "+str(heat_duration)+", "+year+") RETURNING measure_id;"""

    db_cursor.execute(command)

    measure_id= db_cursor.fetchone()[0]

    conn.commit()
    db_cursor.close()
    

    return measure_id

def getHouseID(conn):
    db_cursor=conn.cursor()
    command ="""SELECT house_id FROM Houses"""
    db_cursor.execute(command)
    house_id=None
    house_id_row = db_cursor.fetchone() #just taking the first one
    if(house_id_row == None):
        command =  """INSERT INTO Houses(location)
             VALUES('"""+default_Location+"') RETURNING house_id;"
        db_cursor.execute(command)
        house_id =db_cursor.fetchone()[0]
    else:
        house_id=house_id_row[0]
        
    db_cursor.close()
    conn.commit()
    return house_id




run()
