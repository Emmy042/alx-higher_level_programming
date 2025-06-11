#!/usr/bin/python3

def append_write(filename="", text=""):
    """append a string to a UTF-8 text file and return the number of characters written."""
    
    with open(filename, 'a', encoding="utf8") as f:
        
        return f.write(text)