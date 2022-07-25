# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:35:29 2022

@author: zheng
"""

import csv
import json
 
def create_json_file(csv_path, json_path):
    """
    Converts a csv file into a json file by reading in the csv file and then 
    creating a primary key for the json file.

    Parameters
    ----------
    csv_path : string
        Path to the csv file
    json_path : string
        Path to the converted jSON file

    Returns
    -------
    None.
    """
    
    # Create an empty dictionary to store data
    data = {}
     
    # Open and read in the csv file 
    with open(csv_path, encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
         
        # Iterate over each row in the csv_reader
        for rows in csv_reader:
            # Set a primary key to the dicitonary and then append the rest of 
            # the data as values
            key = rows['sensorReadingID']
            data[key] = rows
 
    # Open the josn file as a writer and use json.dumps() to dump data into 
    # the json file
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))

def main():
    # Set the file paths for the csv file and the exported json_file path
    csv_path = r'simulated_sensor_reading_data.csv'
    json_path = r'simulated_sensor_reading.json'
     
    # Call the function to create the json file
    create_json_file(csv_path, json_path)
    
    if __name__ == '__main__':
        main()