import csv
import json
import argparse
 
def create_json_file(csv_path: str) -> None:
    """
    Converts a csv file into a json file by reading in the csv file and then 
    creating a primary key for the json file.

    Parameters
    ----------
    csv_path : string
        Path to the csv file

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
            key = rows['Serial']
            data[key] = rows
    # Open the json file as a writer and use json.dumps() to dump data into 
    # the json file
    with open(csv_path[:len(csv_path) - 4] + ".json", 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))

def main(csv_path: str) -> None:
    """
    Main method to execute creating a .json from the .csv
    Parameters
    ----------
    csv_path : string
        Path to the csv file

    Returns
    -------
    None.
    """
    create_json_file(csv_path)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path', help="Name of the text file to be processed.")
    args = parser.parse_args()
    main(args.csv_path)