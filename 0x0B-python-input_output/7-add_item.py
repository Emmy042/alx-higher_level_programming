#!/usr/bin/python3

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_list = []
new_list.extend(sys.argv[1:])
    
    
save_to_json_file(new_list, "add_item.json")
    
load_from_json_file("add_item.json")
    
    
