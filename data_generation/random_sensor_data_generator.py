# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import random
from datetime import datetime, timedelta
USER_DATA = "simulated_user_data.csv"

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

def generate_lst(num, min_ran, max_ran):
    """
    Generates a list of random numbers in the specified number range.

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

def main():
    # Create an empty dataframe, with the defined column names
    sensor_df = pd.DataFrame(columns = \
                             ["TimeStamp", "Sensor ID", "User ID", 
                              "Serial Number","Status", "Latitude", 
                              "Longitude"])
    
    # Read in the user csv file as a dataframe    
    user_df = pd.read_csv(USER_DATA)
    
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
    
    # Grab the user id from the user csv file and add it to the sensor 
    # dataframe
    sensor_df["User ID"] = user_df["User ID"]
    
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
    
    # Export the dataframe as as csv file
    sensor_df.to_csv('simulated_sensor_data.csv', index = False)
 
    if __name__ == "__main__":
        main()
        
        