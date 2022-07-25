# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:29:16 2022

@author: zheng
"""

import random
import pandas as pd
from datetime import datetime, timedelta
SENSOR_DATA = "simulated_sensor_data.csv"

"""----------------BEGIN DATA TYPES TO GENERATE----------------"""
"""1. VOC in ppb: known range 0 through 3086 +/- 10% = 0 -> 3300"""
"""2. CO2 in ppm: known range 400 through 25000 +/- 10% = 360 -> 27500"""
"""3. SPM1.0: known range 0 through 0 +/- 10% = 0 -> 0"""
"""4. SPM2.5: known range 0 through 3086, same as VOC"""
"""5. SPM10: known range 7 through 10 +/- 10% = 6 -> 11"""
"""6. AEC1: known range 7 through 11 +/- 10% = 6 -> 12"""
"""7. AEC2.5: known range 7 through 10 +/- 10% = 6 -> 11"""
"""8. AEC1.0: known range 7 through 10 +/- 10% = 6 -> 11"""
"""All AEC values are similar and only rarely deviate from each other"""
"""-----------------END DATA TYPES TO GENERATE-----------------""" 

def generate_lst(num, min_ran, max_ran):
    """
    Generates a list of random numbers of length num in the specified number 
    range.

    Parameters
    ----------
    num : int
        The number of times to run the random.randint for 
    min_ran : int
        The min of the range of random numbers in the list
    max_ran : int
        The max of the range of the random numbers in the list

    Returns
    -------
    data_lst : list
        A list of random generated numbers within the specified range

    """
    
    # Create an empty lst
    data_lst = []
    
    # Iterate over each number in the specified range and generate a random 
    # number and then adding it to the list. 
    for i in range(num):
        data = random.randint(min_ran, max_ran)
        data_lst.append(data)
    
    return data_lst

def generate_timestamp(start_date, end_date):
    """
    Generate hourly timestamps from start date until end date 

    Parameters
    ----------
    start_date : datetime
        The start date.
    end_date : datetime
        The end date.

    Yields
    ------
    delta
        A delta for the timestamp

    """
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

def main():
    # Generate an empty dataframe with the specified columns
    sensor_reading_df = pd.DataFrame(columns = \
                                     ["sensorReadingID", "serialNumber", 
                                      "timeStamp", "VOC","CO2", "SPM1_0", 
                                      "SPM2_5", "SPM10","ACE1_0", "ACE2_5", 
                                      "ACE10"])    
    
    sensor_reading_id_lst = []
    for i in range(17544):
        sensor_reading_id = random.randint(0, 1000000000)
        if sensor_reading_id not in sensor_reading_id_lst:
            sensor_reading_id_lst.append(sensor_reading_id)
    sensor_reading_df["sensorReadingID"] = sensor_reading_id_lst 
    
    # Read in the sensor data csv as a df and grab the serial number column 
    # from the sensor data df and add it to the sensor reading df
    sensor_df = pd.read_csv(SENSOR_DATA)
    sensor_reading_df["serialNumber"] = sensor_df["serialNumber"]     
        
    # Create an empty timestamp list
    timestamp_lst = []
    start_date = datetime(2020, 1, 1, 00, 00)
    end_date = datetime(2022, 1, 1, 00, 00)
    for timestamp in generate_timestamp(start_date, end_date):
        timestamp_lst.append(timestamp.strftime("%Y-%m-%d %H:%M"))
    
    # Add the timestamp_lst into the df under column timestamp
    sensor_reading_df["timeStamp"] = timestamp_lst
    
    # Generate a list of random VOC emissions within the range and add to 
    # the VOC(ppb) column in the dataframe
    voc_data = generate_lst(17544, 0, 3300)
    sensor_reading_df["VOC"] = voc_data
    
    # Generate a list of random CO2 emissions within the range and add to 
    # the CO2(ppm) column in the dataframe
    co2_data = generate_lst(17544, 360, 27500)
    sensor_reading_df["CO2"] = co2_data
    
    # Generate a list of random pm1cf emissions within the range and add to 
    # the dataframe
    pm1cf_data = generate_lst(17544, 0, 0)
    sensor_reading_df["SPM1_0"] = pm1cf_data
    
    # Generate a list of random pm2.5cf emissions within the range and addd to 
    # the dataframe
    pm25cf_data = generate_lst(17544, 0, 0)
    sensor_reading_df["SPM2_5"] = pm25cf_data
    
    # Generate a list of random pm10cf emissions within the range and add to 
    # the dataframe
    pm10cf_data = generate_lst(17544, 6, 11)
    sensor_reading_df["SPM10"] = pm10cf_data
    
    # Generaate a list of random pm1ae emissions within the range and add to 
    # the dataframe
    pm1ae_data = generate_lst(17544, 6, 12)
    sensor_reading_df["ACE1_0"] = pm1ae_data
    
    # Generate a list of random pm2.5ae emissions within the range and add to 
    # the dataframe
    pm25ae_data = generate_lst(17544, 6, 11)
    sensor_reading_df["ACE2_5"] = pm25ae_data
    
    # Generate a list of pm10ae:14 emissions within the range and add to the 
    # dataframe
    pm10ae14_data = generate_lst(17544, 6, 11)
    sensor_reading_df["ACE10"] = pm10ae14_data 
    
    # Export the dataframe as a csv file
    sensor_reading_df.to_csv("simulated_sensor_reading_data.csv", 
                             index = False)
    
    if __name__ == "__main__":
        main()
    
    
    
    