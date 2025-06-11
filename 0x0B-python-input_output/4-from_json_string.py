#!/usr/bin/python3
import json

def from_json_string(my_str):
    """return a python data structure representing a JSON string"""
    
    return json.loads(my_str)