# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:30:19 2020

@author: Lily
"""
def searchFunc(userInput):
    import re
    
    anymatch = False
    
    output = '<head><link rel="stylesheet" type="text/css" href="sr-style.css"></head><body> \n <title>Search Results - Textmind</title>'

    output = output + '<h2 style="font-family:verdana;"> --- Term found in files: </h2>' + '<br> <p>'

    with open (r"Definitions/archive.txt", "r") as data:
        fileContent  = data.read().split("\n")
        for line in fileContent:
            # file, _, keyword = re.compile('(: )').split(line)
            file, keyword = line.split(": ")
            if userInput.upper() in keyword.upper():
                if file in output:
                    continue
                url = file.replace(' ', '%20')
                output= output + '<br>' + "<a href=/file.view?document={}>{}</a>".format(url, file) + '\n'
                anymatch = True
            else:
                continue

    if not anymatch:
        return '<h2> Term was not found in any scanned file </h2></p>'
    output = output + '</body>'
    return output