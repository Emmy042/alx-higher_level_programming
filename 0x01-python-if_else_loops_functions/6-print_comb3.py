#!/usr/bin/python3

for i in range(0, 91):
    s = f"{i:02}"  
    if s[0] != s[1]:
        print(s, end="," + ' ')

print()