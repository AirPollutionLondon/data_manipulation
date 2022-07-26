# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:29:16 2022

@author: zheng
"""

import random
import pandas as pd
from typing import List
SENSOR_DATA = "simulated_sensor_data.csv"

def generate_lst(num: int, min_ran: int, max_ran: int) -> List[int]:
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

def main():
    # Generate an empty dataframe with the specified columns
    sensor_reading_df = pd.DataFrame(columns = \
                                     ["Serial Number", "tVOC","CO2eq", 
                                      "PM1.0CF", "PM2.5CF", "PM10CF","PM1.0AE", 
                                      "PM2.5AE", "PM10AE:14"])    
    
    # Read in the sensor data csv as a df and grab the serial number column 
    # from the sensor data df and add it to the sensor reading df
    sensor_df = pd.read_csv(SENSOR_DATA)
    sensor_reading_df["Serial Number"] = sensor_df["Serial Number"] 
    
    # Generate a list of random VOC emissions within the range and add to 
    # the VOC(ppb) column in the dataframe
    voc_data = generate_lst(17544, 0, 325)
    sensor_reading_df["tVOC"] = voc_data
    
    # Generate a list of random CO2 emissions within the range and add to 
    # the CO2(ppm) column in the dataframe
    co2_data = generate_lst(17544, 0, 500)
    sensor_reading_df["CO2eq"] = co2_data
    
    # Generate a list of random pm1cf emissions within the range and add to 
    # the dataframe
    pm1cf_data = generate_lst(17544, 0, 500)
    sensor_reading_df["PM1.0CF"] = pm1cf_data
    
    # Generate a list of random pm2.5cf emissions within the range and addd to 
    # the dataframe
    pm25cf_data = generate_lst(17544, 0, 500)
    sensor_reading_df["PM2.5CF"] = pm25cf_data
    
    # Generate a list of random pm10cf emissions within the range and add to 
    # the dataframe
    pm10cf_data = generate_lst(17544, 0, 500)
    sensor_reading_df["PM10CF"] = pm10cf_data
    
    # Generaate a list of random pm1ae emissions within the range and add to 
    # the dataframe
    pm1ae_data = generate_lst(17544, 0, 500)
    sensor_reading_df["PM1.0AE"] = pm1ae_data
    
    # Generate a list of random pm2.5ae emissions within the range and add to 
    # the dataframe
    pm25ae_data = generate_lst(17544, 0, 500)
    sensor_reading_df["PM2.5AE"] = pm25ae_data
    
    # Generate a list of pm10ae:14 emissions within the range and add to the 
    # dataframe
    pm10ae14_data = generate_lst(17544, 0, 500)
    sensor_reading_df["PM10AE:14"] = pm10ae14_data 
    
    # Export the dataframe as a csv file
    sensor_reading_df.to_csv("simulated_sensor_reading_data.csv", 
                             index = False)
    
    if __name__ == "__main__":
        main()
    
    
    
    