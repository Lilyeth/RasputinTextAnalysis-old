# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:30:19 2020

@author: Lily
"""
import re
#import os

print("Search term?")
anymatch = False

while True:
    userInput = input()
    break
print("\n" + "--- Term found in:" + "\n")

with open (r"Definitions\archive.txt", "r") as data:
    fileContent  = data.read().split("\n")
    for line in fileContent:
        file, skipcrap, keyword = re.compile('(: )').split(line)
        if keyword in userInput.upper():
            print(file)
            anymatch = True
        else:
            continue
if not anymatch:
    print("Term was not found in any scanned file")