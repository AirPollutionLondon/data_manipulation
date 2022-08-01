from xmlrpc.server import SimpleXMLRPCRequestHandler
import pandas as pd
import argparse
import random

def main(sensor_info_path: str, user_data_path: str, overwrite: bool) -> None:
    """ 
        Modify the .csvs created by the other scripts to include data which is created by scripts other than the initial creator.

        Params:
            - sensor_info_path: str, the path from which to load the sensor metadata .csv
            - user_data_path: str, the path from which to load the user data .csv
            - overwrite: bool, whether or not to overwrite the original files when writing the modifications

        Returns: None.
    """

    # Load the .csvs as pandas dataframes
    sensor_info_df = pd.read_csv(sensor_info_path)
    user_data_df = pd.read_csv(user_data_path)

    # Check to see whether we want to overwrite old files or if we want to create new ones.
    write_path_sensor = sensor_info_path if overwrite else (sensor_info_path[:-4] + "_modified.csv")
    write_path_user = user_data_path if overwrite else (user_data_path[:-4] + "_modified.csv")

    # Pull the connected data from each dataframe into the other.
    sensor_info_df["email"] = [random.choice(user_data_df["email"]) for _ in sensor_info_df["serialNumber"]]
    user_data_df["ownedSensors"] = [pd.Series.to_list(sensor_info_df.loc[sensor_info_df["email"] == email, "serialNumber"]) for email in user_data_df["email"]]

    # Write the now modified .csvs to their respective files.
    sensor_info_df.to_csv(write_path_sensor, index = False)
    user_data_df.to_csv(write_path_user, index = False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sensor_info_path", help = "Path at which the sensor info .csv exists")
    parser.add_argument("user_data_path", help = "Path at which the user data .csv exists")
    parser.add_argument("--overwrite", "-o", help = "Whether or not to modify the files (if False makes new ones).", default = True)
    args = parser.parse_args()
    main(args.sensor_info_path, args.user_data_path, args.overwrite)