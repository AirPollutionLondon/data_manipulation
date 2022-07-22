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
    """ Function: generates a list of random numbers in the specified number 
                  range
        Parameters: num (int), min_ran (int), max_ran (int)
        Returns: a list of randomly generated numbers
    """
    
    # Create an empty lst
    data_lst = []
    
    # Iterate over each number in the specified range and generate a random 
    # number and then adding it to the list. 
    for i in range(num):
        data = random.randint(min_ran, max_ran)
        data_lst.append(data)
    
    return data_lst


def random_char(y):
    return "".join(random.choice(string.ascii_lowercase) for x in range(y))

def main():
    user_df = pd.DataFrame(columns = ["UID", "First Name", "Last Name", 
                                          "Email", "Password", "Phone", 
                                          "Postcode", "Owned Sensors"])
    
    user_id_data = generate_lst(17544, 0, 100000)
    user_df["UID"] = user_id_data
    
    first_name_lst = []
    for i in range(17544):
        firstname = names.get_first_name()
        first_name_lst.append(firstname)
    user_df["First Name"] = first_name_lst
    
    last_name_lst = []
    for i in range(17544):
        last_name = names.get_last_name()
        last_name_lst.append(last_name)
    user_df["Last Name"] = last_name_lst

    email_lst = []
    for i in range(17544):
        email = random_char(10) + "@gmail.com"
        email_lst.append(email)
    user_df["Email"] = email_lst
    
    password_lst = []
    for i in range(17544):
        random_string = string.ascii_uppercase + string.ascii_lowercase + \
            string.digits
        password = "".join(random.SystemRandom().\
                           choice(random_string) for i in range(10))
        password_lst.append(password)
    user_df["Password"] = password_lst
    
    phone_lst = []
    for i in range(17544):
        phone_num = (random.randint(0, 9) for i in range(10))
        phone_lst.append(phone_num)
    user_df["Phone"] = phone_lst
    
    postcode_lst = []
    for i in range(17544):
        random_6_string = string.ascii_lowercase + string.digits
        postcode = "".join(random.SystemRandom().choice(random_6_string) for i in range(6))
        postcode_lst.append(postcode)
    user_df["Postcode"] = postcode_lst
    
    owed_sns_lst = generate_lst(17544, 0, 5)
    user_df["Owned Sensors"] = owed_sns_lst
        
    user_df.to_csv("random_user_data.csv", index = False)
    
    main()
    
        
    