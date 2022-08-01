from typing import List
import pandas as pd
import random
import argparse

def generate_lst(num: int, min_ran: int, max_ran: int) -> List[int]:
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
    return [int(i) for i in generate_lst_float(num, min_ran, max_ran)]

def generate_lst_float(num: int, min_ran: float, max_ran: float) -> List[float]:
    data_lst = []
    
    for _ in range(num):
        data = random.uniform(min_ran, max_ran)
        data_lst.append(data)
        
    return data_lst

def generate_unique_list(count: int) -> List[int]:
    list = []
    for i in range(count):
        item = random.randint(0, 1000000000)
        if item not in list:
            list.append(item)
        else:
            i -= 1
    return list

def generate_bool_list(count: int) -> List[bool]:
    list = []
    for _ in range(count):
        val = random.uniform(0, 1)
        list.append(True if val < 0.5 else False)
    return list

def main(path: str, count: int) -> None:
    # Create an empty dataframe, with the defined column names
    sensor_df = pd.DataFrame(columns = ["serialNumber", "email", "status", "lat", "lon"])
    
    # Generate a random sensor id and set the csv path
    sensor_df["serialNumber"] = [str(i) for i in generate_unique_list(count)]
    
    sensor_df["email"] = ["" for _ in range(count)]
    
    # Generate a list of status strings and add to dataframe
    sensor_df["status"] = [("Active" if i else "Inactive") for i in generate_bool_list(count)]
        
    # Generate a list of random latitudes within the range and add to 
    # latittude column in the dataframe
    sensor_df["lat"] = generate_lst_float(count, 51.29528, 51.704214)
    
    # Generate a list of random longitudes within the range and add to 
    # the longitude column in the dataframe
    sensor_df["lon"] = generate_lst_float(count, -0.495984, 0.155427)
    
    # Export the dataframe as as csv file
    sensor_df.to_csv(path, index = False)
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help = "Path to write the .csv to")
    parser.add_argument("-c", "--count", help = "Number of entries to write.")
    args = parser.parse_args()
    count = 10000
    if args.count != None:
        count = int(args.count)
    main(args.path, count)