# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json

london_air = requests.get("http://api.erg.ic.ac.uk/AirQuality/Hourly/Map")
contents = json.loads(london_air)



json_file_path = "http://api.erg.ic.ac.uk/AirQuality/Hourly/Map"

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read()) 
     print(contents)
