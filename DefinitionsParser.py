# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 22:35:04 2020

--- Parser for log files for usage in definition mapping

@author: Lily
"""
output = [
    ]

with open (r"Definitions\Archive.txt","r") as data:
    seen = set()
    seen.add("\n")
    for line in data:
        if line in seen:
            continue
        else:
            seen.add(line)
        output.append(line)
        #print(line)
#   Organizes content and removes duplicates
    
with open (r"Definitions\Archive.txt","w+") as f:
    f.write(''.join(output))
#   Replace original file with modified file
    