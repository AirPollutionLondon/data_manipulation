import argparse
import random
import pandas as pd
import argparse
from datetime import datetime, timedelta
from typing import List

def generate_lst(num: int, min_ran: int, max_ran: int) -> List[int]:
    """
        Generates a list of random numbers of length num in the specified number 
        range.

        Params:
            - num: int, the number of times to run the random.randint for 
            - min_ran: int, the min of the range of random numbers in the list
            - max_ran: int, the max of the range of the random numbers in the list

        Returns
            - List[int], a list of random generated numbers within the specified range
    """
    
    # Create an empty lst
    data_lst = []
    
    # Iterate over each number in the specified range and generate a random 
    # number and then adding it to the list. 
    for i in range(num):
        data = random.randint(min_ran, max_ran)
        data_lst.append(data)
    
    return data_lst

def generate_timestamp(hours: int, start_date: datetime) -> timedelta:
    """
        Generate hourly timestamps from start date until end date 

        Params:
            - hours: int, the number of hours to generate times for
            - start_date: datetime, the start date

        Returns: 
            - timedelta, timedelta with the dates corresponding to each hour within
    """
    # Create one time stamp per hour until the datetime reaches the end date
    delta = timedelta(hours = 1)
    count = 0
    while count < hours:
        yield start_date
        start_date += delta
        count += 1
    
    return delta

def main(count: int, out_path: str, metadata_path: str) -> None:
    """
        Create a csv to store randomly (but logically) generated sensor readings.

        Params:
            - count: int, number of readings to create
            - out_path: str, output filepath at which to create the csv
            - metadata_path: str, path at which to load the metadata csv
        
        Returns: None.
    """

    # Generate an empty dataframe with the specified columns
    sensor_reading_df = pd.DataFrame(columns = ["sensorReadingID", "serialNumber", "timeStamp", "VOC", "CO2", "SPM1", "SPM25", "SPM10", "AEC1", "AEC25", "AEC10", "status", "lat", "lon"])    

    # Read and load the sensor metadata csv
    sensor_df = pd.read_csv(metadata_path)

    # Give a unique id to each sensor reading
    sensor_reading_df["sensorReadingID"] = range(count)
    
    # Load the serial numbers from the metadata mainframe and randomly assign one to each reading
    serial_list = [random.choice(sensor_df["serialNumber"]) for _ in range(count)]
    sensor_reading_df["serialNumber"] = serial_list
        
    # Add the timestamp_lst into the df under column timestamp
    sensor_reading_df["timeStamp"] = [time.strftime("%Y-%m-%d %H:%M") for time in generate_timestamp(count, datetime(2020, 1, 1, 0, 0))]
    
    # Generate a list of random VOC emissions within the range and add to 
    # the VOC(ppb) column in the dataframe
    sensor_reading_df["VOC"] = generate_lst(count, 0, 3300)
    
    # Generate a list of random CO2 emissions within the range and add to 
    # the CO2(ppm) column in the dataframe
    sensor_reading_df["CO2"] = generate_lst(count, 360, 27500)
    
    # Generate a list of random pm1cf emissions within the range and add to 
    # the dataframe
    sensor_reading_df["SPM1"] = generate_lst(count, 0, 1)
    
    # Generate a list of random pm2.5cf emissions within the range and addd to 
    # the dataframe
    sensor_reading_df["SPM25"] = generate_lst(count, 0, 1)
    
    # Generate a list of random pm10cf emissions within the range and add to 
    # the dataframe
    sensor_reading_df["SPM10"] = generate_lst(count, 6, 11)
    
    # Generaate a list of random pm1ae emissions within the range and add to 
    # the dataframe
    sensor_reading_df["AEC1"] = generate_lst(count, 6, 12)
    
    # Generate a list of random pm2.5ae emissions within the range and add to 
    # the dataframe
    sensor_reading_df["AEC25"] = generate_lst(count, 6, 11)
    
    # Generate a list of pm10ae:14 emissions within the range and add to the 
    # dataframe
    sensor_reading_df["AEC10"] = generate_lst(count, 6, 11)

    # Append an "Active" status to all readings (as it must be active to send a reading)
    sensor_reading_df["status"] = ["Active" for _ in range(count)]

    # Load lats and lons from sensor metadata
    sensor_reading_df["lat"] = [pd.Series.to_list(sensor_df.loc[sensor_df["serialNumber"] == serial, 'lat'])[0] for serial in serial_list]
    sensor_reading_df["lon"] = [pd.Series.to_list(sensor_df.loc[sensor_df["serialNumber"] == serial, 'lon'])[0] for serial in serial_list]
    
    # Export the dataframe as a csv file
    sensor_reading_df.to_csv(out_path, index = False)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output_path", help = "Path to which to write the .csv")
    parser.add_argument("sensor_metadata_path", help = "Path from which to pull sensor metadata.")
    parser.add_argument("-c", "--count", help = "Number of entries to write.")
    args = parser.parse_args()
    count = 10000
    if args.count != None:
        count = int(args.count)
    main(count, args.output_path, args.sensor_metadata_path)
    
    
    
    