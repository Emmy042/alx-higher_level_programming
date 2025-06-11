#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
    """writes an object to a textfile in JSON format"""
    
    if isinstance(my_obj, set):
        my_obj = list(my_obj)  # Convert set to list
        
    convert_str = json.dumps(my_obj)
    
    with open(filename, 'w', encoding='utf8') as f:
        f.write(convert_str)
        
        