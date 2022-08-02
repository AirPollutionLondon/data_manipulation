# Using the scripts:

## Prerequisities

### Python libraries
1. **pandas**
2. **names**

## BASH Solution:

### generate_data.sh

The generating data script will function to run everything - however it does require root access as it creates directories.

In order to run (assuming repository is cloned into ~/AirPollutionLondon:

1. In the directory where the file is located run the following commands.
2. ```chmod +x generate_data.sh```
3. ```sudo ./generate_data.sh```
4. The output files will be in ~/AirPollutionLondon/data_manipulation/data_generation/csvs

If the user does not have Python installed and configured to run on PATH with the required libraries, it may be necessary to edit the script to use ```python3``` rather than ```python```

## Running the individual (data generation) scripts:

### sensor_metadata_generator.py

This script will create Sensor Metadata, but that data will not include the ownership emails.

#### Arguments:

1. **output_path**: required argument for file path or string representing the name of the file and where to write it (must end in .csv)
2. **--count** \[alias **-c**\]: number of entries to make in the output csv \[default: 10000\]

### user_data_generator.py

This script will create User Data, but will not add owned sensors.

#### Arguments:

1. **output_path**: required argument for file path or string representing the name of the file and where to write it (must end in .csv)
2. **--count** \[alias **-c**\]: number of entries to make in the output csv \[default: 10000\]

### data_metamodifier.py

This script will modify the User Data and the Sensor Metadata adding ownership (to both sides)

#### Arguments:

1. **sensor_metadata_path**: required argument for the file path at which the Sensor Metadata csv exists
2. **user_data_path**: required argument for the file path at which the User Data csv exists
3. **--overwrite** \[alias **-o**\]: whether or not to overwrite the original files (on False makes new ones) \[default: True\]

### sensor_reading_generator.py

This script will create example sensor readings using the Sensor Metadata.

#### Arguments:
1. **output_path**: required argument for file path or string representing the name of the file and where to write it (must end in .csv)
2. **sensor_metadata_path**: required argument for the file path at which the Sensor Metadata csv exists
3. **--count** \[alias **-c**\]: number of entries to make in the output csv \[default: 10000\]

## Other scripts:

### convert_csv_to_json.py

This script will convert a .csv file to a .json file for a given (or default) primary key.

#### Arguments:
1. **csv_path**: required argument for path to the .csv to load and convert (creates a .json in the same path)
2. **--primary_key** \[alias: **-p**\]: the column to use as the primary key for the .json \[default: "sensorReadingID"\]

### convert_txt_to_csv.py

This script will convert a .txt file to a .csv file given that it is formatted like:

```
Activated: **STATUS**
Serial Number: **NUMBER**
*this line ignored*
Time: **YYYY-MM-DD HH:MM:SS** Field2: **VALUE** Field3: **VALUE** ... FieldN: **VALUE**
...
...
```

#### Arguments:
1. **txt_path**: required argument for the path to the txt to load and convert (creates the .csv in the same path)
