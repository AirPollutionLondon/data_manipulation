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
    
def generate_num(min_ran, max_ran):
    """ Function: randomly generate a number in the specified range
        Parameter: min_ran (int), max_ran (int)
        Returns: n (int)
    """
    
    n = random.randint(min_ran, max_ran)
    
    return n 

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
        data = generate_num(min_ran, max_ran)
        data_lst.append(data)
    
    return data_lst

def main():
    # Create an empty dataframe, with the defined column names
    sensor_df = pd.DataFrame(columns = ["TimeStamp", "Sensor ID", "Latitude", 
                                             "Longitude", "VOC(ppb)", "CO2(ppm)"])
    
    # Create an empt timestamp list
    timestamp_lst = []
    start_date = datetime(2021, 1, 1, 00, 00)
    end_date = datetime(2022, 1, 1, 00, 00)
    for timestamp in generate_timestamp(start_date, end_date):
        timestamp_lst.append(timestamp.strftime("%Y-%m-%d %H:%M"))
    
    # Add the timestamp_lst into the df under column timestamp
    sensor_df["TimeStamp"] = timestamp_lst
    
    # Generate a random sensor id and set the csv path
    sensor_id = random.randint(1000, 9000)
    csv_path = "Sensor " + str(sensor_id) + " 2021-2022" + '.csv'
    sensor_df["Sensor ID"] = sensor_id
    
    # Generate a list of 8760 random latitudes within the range and add to 
    # latittude column in the dataframe
    lat_data = generate_lst(8760, -90, 90)
    sensor_df["Latitude"] = lat_data
    
    # Generate a list of 8760 random longitudes within the range and add to 
    # the longitude column in the dataframe
    long_data = generate_lst(8760, -180, 180)
    sensor_df["Longitude"] = long_data
    
    # Generate a list of 8760 random VOC emissions within the range and add to 
    # the VOC(ppb) column in the dataframe
    voc_data = generate_lst(8760, 0, 325)
    sensor_df["VOC(ppb)"] = voc_data
    
    # Generate a list of 8760 random CO2 emissions within the range and add to 
    # the CO2(ppm) column in the dataframe
    co2_data = generate_lst(8760, 0, 500)
    sensor_df["CO2(ppm)"] = co2_data
    
    # Export the dataframe as as csv file
    sensor_df.to_csv(csv_path, index = False)
 
    if __name__ == "__main__":
        main()
        
        