# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import random
from datetime import datetime, timedelta

def generate_timestamp(start_date, end_date):
    """ Function: generates hourly timestamp series from start date until 
                  end date   
        Parameters: start_date (datetime), end_date(datetime)
        Returns: the timedelta
    """
    
    # Create one time stamp per hour until the datetime reaches the end date
    delta = timedelta(hours = 1)
    while start_date < end_date:
        yield start_date
        start_date += delta
    
    return delta

def generate_lst(num, min_ran, max_ran):
    """ Function: generates a list of random numbers in the specified number 
                  range
        Parameters: num (int), min_ran (int), max_ran (int)
        Returns: a list of randomly generated numbers
    """
    
    # Create an empty lst
    data_lst = []
    
    # Iterate over each number in the specified range and generate a random 
    # number and then adding it to the list. 
    for i in range(num):
        data = random.randint(min_ran, max_ran)
        data_lst.append(data)
    
    return data_lst

def main():
    # Create an empty dataframe, with the defined column names
    sensor_df = pd.DataFrame(columns = \
                             ["TimeStamp", "Sensor ID", "Owner ID", 
                              "Serial Number","Status", "Latitude", 
                              "Longitude", "tVOC","CO2eq", "PM1.0CF", 
                              "PM2.5CF", "PM10CF","PM1.0AE", "PM2.5AE", 
                              "PM10AE:14"])
    
    # Create an empt timestamp list
    timestamp_lst = []
    start_date = datetime(2020, 1, 1, 00, 00)
    end_date = datetime(2022, 1, 1, 00, 00)
    for timestamp in generate_timestamp(start_date, end_date):
        timestamp_lst.append(timestamp.strftime("%Y-%m-%d %H:%M"))
    
    # Add the timestamp_lst into the df under column timestamp
    sensor_df["TimeStamp"] = timestamp_lst
    
    # Generate a random sensor id and set the csv path
    sensor_id_lst = []
    for i in range(17544):
        sensor_id = random.randint(0, 1000000000)
        if sensor_id not in sensor_id_lst:
            sensor_id_lst.append(sensor_id)
    sensor_df["Sensor ID"] = sensor_id_lst
    
    # Generate a list of random owner ids and add to dataframe
    owner_id_lst = []
    for i in range(17544):
        owner_id = random.randint(0, 9000000000)
        if owner_id not in owner_id_lst:
            owner_id_lst.append(owner_id)
            
    sensor_df["Owner ID"] = owner_id_lst
    
    # Generate a list of random serial numbers and add to dataframe
    serial_lst = []
    for i in range(17544):
        serial = random.randint(0, 100000000000)
        if serial not in serial_lst:
            serial_lst.append(serial)
            
    sensor_df["Serial Number"] = serial_lst
    
    # Generate a list of status strings and add to dataframe
    status_lst = []
    for i in range(17544):
        random_num = random.randint(0, 1)
        if random_num <= 0.5:
            status_lst.append("Active")
        else:
            status_lst.append("Inactive")
    sensor_df["Status"] = status_lst
        
    # Generate a list of random latitudes within the range and add to 
    # latittude column in the dataframe
    lat_data = generate_lst(17544, -90, 90)
    sensor_df["Latitude"] = lat_data
    
    # Generate a list of random longitudes within the range and add to 
    # the longitude column in the dataframe
    long_data = generate_lst(17544, -180, 180)
    sensor_df["Longitude"] = long_data
    
    # Generate a list of random VOC emissions within the range and add to 
    # the VOC(ppb) column in the dataframe
    voc_data = generate_lst(17544, 0, 325)
    sensor_df["tVOC"] = voc_data
    
    # Generate a list of random CO2 emissions within the range and add to 
    # the CO2(ppm) column in the dataframe
    co2_data = generate_lst(17544, 0, 500)
    sensor_df["CO2eq"] = co2_data
    
    # Generate a list of random pm1cf emissions within the range and add to 
    # the dataframe
    pm1cf_data = generate_lst(17544, 0, 500)
    sensor_df["PM1.0CF"] = pm1cf_data
    
    # Generate a list of random pm2.5cf emissions within the range and addd to 
    # the dataframe
    pm25cf_data = generate_lst(17544, 0, 500)
    sensor_df["PM2.5CF"] = pm25cf_data
    
    # Generate a list of random pm10cf emissions within the range and add to 
    # the dataframe
    pm10cf_data = generate_lst(17544, 0, 500)
    sensor_df["PM10CF"] = pm10cf_data
    
    # Generaate a list of random pm1ae emissions within the range and add to 
    # the dataframe
    pm1ae_data = generate_lst(17544, 0, 500)
    sensor_df["PM1.0AE"] = pm1ae_data
    
    # Generate a list of random pm2.5ae emissions within the range and add to 
    # the dataframe
    pm25ae_data = generate_lst(17544, 0, 500)
    sensor_df["PM2.5AE"] = pm25ae_data
    
    # Generate a list of pm10ae:14 emissions within the range and add to the 
    # dataframe
    pm10ae14_data = generate_lst(17544, 0, 500)
    sensor_df["PM10AE:14"] = pm10ae14_data 
    
    # Export the dataframe as as csv file
    sensor_df.to_csv('simulated_sensor_data.csv', index = False)
 
    if __name__ == "__main__":
        main()
        
        