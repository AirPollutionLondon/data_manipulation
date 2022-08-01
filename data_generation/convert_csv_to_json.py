import csv
import json
import argparse
 
def create_json_file(csv_path: str, pk: str = 'sensorReadingID') -> None:
    """ 
        Converts a csv file into a json file by reading in the csv file and then 
        creating a primary key for the json file.

        Params
            - csv_path : str, path to the csv file

        Returns: None.
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
            key = rows[pk]
            data[key] = rows
    # Open the json file as a writer and use json.dumps() to dump data into 
    # the json file
    with open(csv_path[:len(csv_path) - 4] + ".json", 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))

def main(csv_path: str) -> None:
    """
        Given a csv, create a json.
        
        Params:
            - csv_path: str, path to the csv file

        Returns: None.
    """
    create_json_file(csv_path)

def main(csv_path: str, primary_key: str) -> None:
    """
        Given a csv and a primary key, create a json.
        
        Params:
            - csv_path: str, path to the csv file
            - primary_key: str, column header to base the .json file off of

        Returns: None.
    """
    create_json_file(csv_path, primary_key)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path', help="Path of the .csv file to be processed.")
    parser.add_argument('--primary_key', '-p', help="Name of the column-header corresponding to the primary key of the .csv file", required=False)
    args = parser.parse_args()
    if args.primary_key != None:
        main(args.csv_path, args.primary_key)
    else:
        main(args.csv_path)