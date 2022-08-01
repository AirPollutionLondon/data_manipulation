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

    Parameters
    ----------
    num : int
        The number of times to run the random.randint for 
    min_ran : int
        The min of the range of random numbers in the listpy
    max_ran : int
        The max of the range of the random numbers in thpye list

    Returns
    -------
    data_lst : list
        A list of random generated numbers within the specified range

    """
    
    # Create an empty lst
    data_lst = []
    
    # Iterate over each number in the specified range and generate a random 
    # number and then adding it to the list. 
    for i in range(num):
        data = random.randint(min_ran, max_ran)
        data_lst.append(data)
    
    return data_lst

def make_email(num, first, last) -> str:
    return (first + last).lower() + str(num) + "@gmail.com"

def random_string(y: int) -> str:
    """
    Create random characters of a specific length

    Parameters
    ----------
    y : int
        The length of random characters to create

    Returns
    -------
    random_word: int and string
        A random word of length y
    """
    # Generate a random word of length y
    random_word = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(y))
    
    return random_word

def generate_emails(count, first_names, last_names):
    email_list = []
    for i in range(count):
        email_list.append(make_email(i, first_names[i], last_names[i]))
    return email_list

def generate_unique_list(count, min, max):
    list = []
    for i in range(count):
        item = random.randint(min, max)
        if item not in list:
            list.append(item)
        else:
            i -= 1
    return list

def main(path: str, count: int) -> None:
    # Create an empty user dataframe that contains the prenamed columns

    # email: str, firstName: str, lastName: str, password: str, phone: int, postcode: str, ownedSensors: List[str]

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
    
    # Generate a list of random number of sensors owned by each user
    user_df["ownedSensors"] = ["" for _ in range(count)]
        
    # Export the dataframe as a csv file
    user_df.to_csv(path, index = False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help = "Path to write the .csv to")
    parser.add_argument("-c", "--count", help = "Number of entries to write.")
    args = parser.parse_args()
    count = 10000
    if args.count != None:
        count = int(args.count)
    main(args.path, count)
    
        
    