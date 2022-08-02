import pandas as pd
import random
import names
import string
from typing import List
import argparse

def generate_lst(num: int, min_ran: int, max_ran: int) -> List[int]:
    """
        Generates a list of random numbers of length num in the specified number 
        range.

        Parameters:
            - num: int, the number of times to run the random.randint for 
            - min_ran: int, the min of the range of random numbers in the listpy
            - max_ran: int, the max of the range of the random numbers in thpye list

        Returns:
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

def make_email(num: int, first: str, last: str) -> str:
    """
        Combines two names and a number to create a gmail address.

        Params:
            - num: int
        
        Returns:
            - str, a formatted gmail email address
    """
    return (first + last).lower() + str(num) + "@gmail.com"

def random_string(length: int) -> str:
    """
        Creates a random string of length <length>.

        Params:
            - length: int, the length of random characters to create

        Returns:
            - str, a random word of length <length>
    """
    return "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(length))

def generate_emails(count: int, first_names: List[str], last_names: List[str]) -> List[str]:
    """
        Generated a list of email addresses.

        Params:
            - count: int, the number of emails to create
            - first_names: List[str], list of first names to use
            - last_names: List[str], list of last names to use

        Returns:
            - List[str], a list of email addresses
    """
    email_list = []
    for i in range(count):
        email_list.append(make_email(i, first_names[i], last_names[i]))
    return email_list

def generate_unique_list(count: int, min: int, max: int) -> List[int]:
    """
        Generates a list of random numbers in which none are repeated.

        Params:
            - count: int, the number of elements to add to the list
            - min: int, the minimum number to generate
            - max: int, the maximum number to generate
        
        Returns:
            - List[int], a unique-element list of randomly generated numbers
    """
    list = []
    for i in range(count):
        item = random.randint(min, max)
        if item not in list:
            list.append(item)
        else:
            i -= 1
    return list

def main(out_path: str, count: int) -> None:
    """
        Creates a csv with data representing the users of the system.

        Params:
            - out_path: str, the path to which to write the csv
            - count: the number of rows to add to the csv

        Returns: None.
    """
    # Create an empty user dataframe that contains the prenamed columns
    user_df = pd.DataFrame(columns = ["email", "firstName", "lastName", "password", "phone", "postcode", "ownedSensors"])

    # Generate a list of random firstnames and then add it to the dataframe 
    user_df["firstName"] = [names.get_first_name() for _ in range(count)]
    
    # Generate a list of random lastnames and add it to the dataframe
    user_df["lastName"] = [names.get_last_name() for _ in range(count)]

    # Generate a list of random email addressses and add it to the dataframe
    user_df["email"] = generate_emails(count, user_df["firstName"], user_df["lastName"])
 
    # Generate a list of random passwords and add it to the dataframe
    user_df["password"] = [random_string(random.randint(8, 32)) for _ in range(count)]
    
    # Generate a list of random phone numbers and add it to the dataframe
    user_df["phone"] = generate_unique_list(count, 1000000000, 9999999999)
    
    # Generate a list of random postcodes and add it to the dataframe
    user_df["postcode"] = [("".join(random.SystemRandom().choice(string.ascii_lowercase + string.digits).upper() for i in range(6))) for _ in range(count)]
    
    # Add a blank column to the dataframe where the owned sensor lists can later be added
    user_df["ownedSensors"] = ["" for _ in range(count)]
        
    # Export the dataframe as a csv file
    user_df.to_csv(out_path, index = False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output_path", help = "Path to which to write the .csv")
    parser.add_argument("-c", "--count", help = "Number of entries to write.")
    args = parser.parse_args()
    count = 10000
    if args.count != None:
        count = int(args.count)
    main(args.output_path, count)
    
        
    