# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:35:52 2022

@author: zheng
"""

import pandas as pd
import random
import names
import string

def generate_lst(num, min_ran, max_ran):
    """
    Generates a list of random numbers of length num in the specified number 
    range.

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
    data_lst = []
    
    # Iterate over each number in the specified range and generate a random 
    # number and then adding it to the list. 
    for i in range(num):
        data = random.randint(min_ran, max_ran)
        data_lst.append(data)
    
    return data_lst


def random_word(y):
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
    random_word = "".join(random.choice(string.ascii_lowercase) \
                          for x in range(y))
    
    return random_word

def main():
    # Create an empty user dataframe that contains the prenamed columns
    user_df = pd.DataFrame(columns = ["User ID", "First Name", "Last Name", 
                                          "Email", "Password", "Phone", 
                                          "Postcode", "Owned Sensors"])
    
    # Generate a list of random user ids and add it to the dataframe
    user_id_data = generate_lst(17544, 0, 100000)
    user_df["User ID"] = user_id_data
    
    # Generate a list of random firstnames and then add it to the dataframe 
    first_name_lst = []
    for i in range(17544):
        firstname = names.get_first_name()
        first_name_lst.append(firstname)
    user_df["First Name"] = first_name_lst
    
    # Generate a list of random lastnames and add it to the dataframe
    last_name_lst = []
    for i in range(17544):
        last_name = names.get_last_name()
        last_name_lst.append(last_name)
    user_df["Last Name"] = last_name_lst

    # Generate a list of random email addressses and add it to the dataframe
    email_lst = []
    for i in range(17544):
        email = random_word(10) + "@gmail.com"
        email_lst.append(email)
    user_df["Email"] = email_lst
    
    # Generate a list of random passwords and add it to the dataframe
    password_lst = []
    for i in range(17544):
        random_string = string.ascii_uppercase + string.ascii_lowercase + \
            string.digits
        password = "".join(random.SystemRandom().\
                           choice(random_string) for i in range(10))
        password_lst.append(password)
    user_df["Password"] = password_lst
    
    # Generate a list of random phone numbers and add it to the dataframe
    phone_lst = []
    for i in range(17544):
        num = [random.randint(0, 9) for i in range(10)]
        #num = str((random.randint(0, 9) for i in range(10)))
        #phone_num = "".join(num)
        number = ""
        for i in num:
            number = "".join([number, str(i)])
        phone_lst.append(number)
    user_df["Phone"] = phone_lst
    
    # Generate a list of random postcodes and add it to the dataframe
    postcode_lst = []
    for i in range(17544):
        random_6_string = string.ascii_lowercase + string.digits
        postcode = "".join(random.SystemRandom().choice(random_6_string) \
                           for i in range(6))
        postcode_lst.append(postcode)
    user_df["Postcode"] = postcode_lst 
    
    # Generate a list of random number of sensors owned by each user
    owed_sns_lst = generate_lst(17544, 0, 5)
    user_df["Owned Sensors"] = owed_sns_lst
        
    # Export the dataframe as a csv file
    user_df.to_csv("simulated_user_data.csv", index = False)
    
    if __name__ == "__main__":
        main()
    
        
    