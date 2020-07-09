#!usr/bin/env python3
#-*-coding:utf-8-*-
#import psycopg-2

import time
from edgeRequest import getTemperature

dbname="Cloud"
username_db="postgres"
password_db="postgres"

default_Location="Paris"
measure_rate=60
def run():
    
    connexion = init_db()
    house_id = getHouseID(conn)

    print("Starting aquisition on edge, House n°"+house_id)
    while(True):

        stats= getTemperature()
        insert_data(connexion, house_id ,stats)
        time.sleep(measure_rate)
    print("Stopping aquisition")


        
    

def init_db():
    
   
    conn = psycopg2.connect(host="localhost",database=dbname, user=username, password=password_db)
    db_cursor = conn.cursor()
    
    commands = (
    """
        CREATE TABLE IF NOT EXISTS House (
            house_id SERIAL PRIMARY KEY,
            location VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS GeoTemp (
            measure_id SERIAL PRIMARY KEY,
            house_id SERIAL,
            temperature_avg DOUBLE NOT NULL,
            temperature_unit CHAR,
            delta DOUBLE,
            clim_duration DOUBLE,
            date VARCHAR(50),
            FOREIGN KEY (house_id) REFERENCES Edge (id)
        )
        """)
       
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()

        return conn

def insert_data(conn, house_id, request):
    db_cursor=conn.cursor()
     public string Statyear { get; set; }
    temp_avg = request.json().get("average")
    temp_delta= request.json().get("std_deviation")
    clim_duration= request.json().get("clim_duration")
    heat_duration= request.json().get("heat_duration")
    year= request.json().get("year")
    temperature_unit= request.json().get("temperature_unit")
    

    command= """INSERT INTO GeoTemp(house_id, temperature_avg, temperature_unit, delta,clim_duration,heat_duration,date)
             VALUES("""+house_id+", "+temp_avg+", "+temp_delta+", "+clim_duration+", "+heat_duration+", "+year+") RETURNING measure_id;"""

    cur.execute(command)

    measure_id= cur.fetchone()[0]

    conn.commit()
    cur.close()
    

    return measure_id

def getHouseID(conn):
    db_cursor=conn.cursor()
    command ="""SELECT house_id FROM House"""
    cur.execute(command)
    house_id = cur.fetchone()[0] #just taking the first one
    if(house_id == None):
        command =  """INSERT INTO House(location)
             VALUES("""+default_Location+") RETURNING house_id;"""
        cur.execute(command)
        house_id =cur.fetchone()[0]




run()
