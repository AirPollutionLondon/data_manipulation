# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import random
USER_DATA = "simulated_user_data.csv"


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

def generate_lst_float(num, min_ran, max_ran):
    data_lst = []
    
    for i in range(num):
        data = random.uniform(min_ran, max_ran)
        data_lst.append(data)
        
    return data_lst

def main():
    # Create an empty dataframe, with the defined column names
    sensor_df = pd.DataFrame(columns = \
                             ["sensorID", "userID", "serialNumber", "status", 
                              "latitude", "longitude"])
    
    # Read in the user csv file as a dataframe    
    user_df = pd.read_csv(USER_DATA)
    
    
    # Generate a random sensor id and set the csv path
    sensor_id_lst = []
    for i in range(17544):
        sensor_id = random.randint(0, 1000000000)
        if sensor_id not in sensor_id_lst:
            sensor_id_lst.append(sensor_id)
    sensor_df["sensorID"] = sensor_id_lst
    
    # Grab the user id from the user csv file and add it to the sensor 
    # dataframe
    sensor_df["userID"] = user_df["userID"]
    
    # Generate a list of random serial numbers and add to dataframe
    serial_lst = []
    for i in range(17544):
        serial = random.randint(0, 100000000000)
        if serial not in serial_lst:
            serial_lst.append(serial)
            
    sensor_df["serialNumber"] = serial_lst
    
    # Generate a list of status strings and add to dataframe
    status_lst = []
    for i in range(17544):
        random_num = random.randint(0, 1)
        if random_num <= 0.5:
            status_lst.append("Active")
        else:
            status_lst.append("Inactive")
    sensor_df["status"] = status_lst
        
    # Generate a list of random latitudes within the range and add to 
    # latittude column in the dataframe
    lat_data = generate_lst_float(17544, 51.29528, 51.704214)
    sensor_df["latitude"] = lat_data
    
    # Generate a list of random longitudes within the range and add to 
    # the longitude column in the dataframe
    long_data = generate_lst_float(17544, -0.495984, 0.155427)
    sensor_df["longitude"] = long_data
    
    # Export the dataframe as as csv file
    sensor_df.to_csv('simulated_sensor_data.csv', index = False)
 
    if __name__ == "__main__":
        main()
        
        
