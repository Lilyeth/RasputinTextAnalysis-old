# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 23:16:57 2020

--- Main executable for definition highlighting

@author: Lily, (Mentioned: Shebpamm)
"""
import re
import os
import webbrowser


print("Select file")
files = os.listdir(r"Data\\")
txt = {}

i = 1

for file in files:
	if file[-4:] == ".txt":
		txt[str(i)] = file
		print("[{}] {}".format(i, file))
		i = i+1

while True:
	userInput = input()
	try: 
		int(userInput)
		break
	except: print("Use number")


fileName = txt[userInput] [0:-4]

fileLocation = r"Data\{}.txt".format(fileName)

#   File selection for input file





with open(fileLocation,"r") as data:
    fileContent = data.read()
    
d = {
     
     }

patterns = [
(r"[A-Z][A-Z]([-]|[A-Z])*", '<font color=\"blue\">'),
]

with open(r"colors.cfg","r") as data:
    content = data.read().split("\n")
    for line in content:
        text, skipcrap, color = re.compile(' ?= ?(?=([^"]*"[^"]*")*[^"]*$)').split(line)

        colored = "<font color=\"{}\">".format(color)
        temp = '{}'.format(color)
        d[temp]=colored
#   Add defined colors to dictionary        
        patterns.append((re.escape(text[1:-1]), d[color]))
#   Add defined search patterns




archive = open(r"Definitions\archive.txt","a+")
     
globalPattern = re.compile( '|'.join([i[0] for i in patterns]))
matches = re.finditer(globalPattern, fileContent)  

finalString = "<pre>"
lastEnd = 0

for match in matches:

    finalString += fileContent[lastEnd:match.start()]

    textColor = '</font>' 

    for pattern, color in patterns:
        if re.match(pattern, match.group()): textColor = color
    archive.write('\n' + fileName + ': ' + match.group())

#   Extracts all matches from text

    finalString += textColor + match.group() + '</font>'
    lastEnd = match.end()

finalString += fileContent[lastEnd:]+'</pre>'
#   Compiles final color match




archive.close() 
output = open(r"Processed\{}.html".format(fileName),"w+")
output.write(finalString)  
output.close()
#webbrowser.open(r"processed\{}.html".format(fileName), new = 0)

exec(open("DefinitionsParser.py").read())
#   Outputs and opens final file