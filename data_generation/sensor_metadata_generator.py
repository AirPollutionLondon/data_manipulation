import string
from typing import List
import pandas as pd
import random
import argparse

def generate_lst(count: int, min_ran: int, max_ran: int) -> List[int]:
    """
        Generates a list of random ints in the specified range.

        Params:
            - count: int, the number of elements to add to the list
            - min_ran : int, the min of the range of random numbers in the list
            - max_ran : int, the max of the range of the random numbers in the list

        Returns:
            - List[int], a list of random generated numbers within the specified range
    """
    return [int(i) for i in generate_lst_float(count, min_ran, max_ran)]

def generate_lst_float(count: int, min_ran: float, max_ran: float) -> List[float]:
    """
        Generates a list of random floats in the specified range.

        Params:
            - count: int, numbers of elements to add to the list
            - min_ran: float, the min of the random number range
            - max_ran: float, the max of the random number range
        
        Returns:
            - List[float], a list of random generated numbers within the specified range

    """
    return [random.uniform(min_ran, max_ran) for _ in range(count)]

def generate_unique_list(count: int) -> List[int]:
    """
        Generates a random list of integers where each integer is not repeated within the list.

        Params:
            - count: int, number of elements to add to the list
        
        Returns:
            - List[int], a list of <count> numbers where all elements are unique
    """
    list = []
    for i in range(count):
        item = "".join([random.choice("1234567890" + string.ascii_lowercase) for _ in range(16)])
        if item not in list:
            list.append(item)
        else:
            i -= 1
    return list

def generate_bool_list(count: int) -> List[bool]:
    """
        Creates a list of booleans.

        Params:
            - count: int, number of elements to add to the list

        Returns:
            - List[bool]: a list of <count> booleans

    """
    return [True if random.uniform(0, 1) < 0.5 else False for _ in range(count)]

def main(path: str, count: int) -> None:
    """
        Create a sensor metadata .csv.

        Params:
            - path: str, the filepath to which to write the file
            - count: int, the number of rows to add to the .csv
        
        Returns: None.
    """

    # Create an empty dataframe, with the defined column names
    sensor_df = pd.DataFrame(columns = ["serialNumber", "email", "status", "lat", "lon"])
    
    # Generate a random sensor id and set the csv path
    sensor_df["serialNumber"] = [str(i) for i in generate_unique_list(count)]
    
    # Add a blank column to the dataframe for where the emails of sensor owners can later be added
    sensor_df["email"] = ["" for _ in range(count)]
    
    # Generate a list of status strings and add to dataframe
    sensor_df["status"] = [("Active" if i else "Inactive") for i in generate_bool_list(count)]
        
    # Generate a list of random latitudes within the range and add to latittude column in the dataframe
    sensor_df["lat"] = generate_lst_float(count, 51.29528, 51.704214)
    
    # Generate a list of random longitudes within the range and add to the longitude column in the dataframe
    sensor_df["lon"] = generate_lst_float(count, -0.495984, 0.155427)
    
    # Export the dataframe as as csv file
    sensor_df.to_csv(path, index = False)
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output_path", help = "Path to write the .csv to")
    parser.add_argument("-c", "--count", help = "Number of entries to write.")
    args = parser.parse_args()
    count = 10000
    if args.count != None:
        count = int(args.count)
    main(args.output_path, count)