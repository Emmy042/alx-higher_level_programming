#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """writes an Object from a JSON file"""
    
    with open(filename, 'r', encoding='utf8') as f:
        return json.load(f)
