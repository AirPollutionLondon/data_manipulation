from xmlrpc.server import SimpleXMLRPCRequestHandler
import pandas as pd
import argparse
import random

def main(sensor_info_path, user_data_path, overwrite):
    sensor_info_df = pd.read_csv(sensor_info_path)
    user_data_df = pd.read_csv(user_data_path)

    write_path_sensor = sensor_info_path if overwrite else (sensor_info_path[:-4] + "_modified.csv")
    write_path_user = user_data_path if overwrite else (user_data_path[:-4] + "_modified.csv")

    sensor_info_df["email"] = [random.choice(user_data_df["email"]) for _ in sensor_info_df["serialNumber"]]
    user_data_df["ownedSensors"] = [pd.Series.to_list(sensor_info_df.loc[sensor_info_df["email"] == email, "serialNumber"]) for email in user_data_df["email"]]

    sensor_info_df.to_csv(write_path_sensor, index = False)
    user_data_df.to_csv(write_path_user, index = False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sensor_info_path", help = "Path at which the sensor info .csv exists")
    parser.add_argument("user_data_path", help = "Path at which the user data .csv exists")
    parser.add_argument("--overwrite", "-o", help = "Whether or not to modify the files (if False makes new ones).", default = True)
    args = parser.parse_args()
    main(args.sensor_info_path, args.user_data_path, args.overwrite)