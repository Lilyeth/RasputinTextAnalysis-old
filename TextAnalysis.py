# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 23:16:57 2020
	TextAnalys2.0
--- Main executable for definition highlighting

@author: Lily, (Mentioned: Shebpamm)
"""
import re
import os
import webbrowser


# print("Select file")
files = os.listdir(r"Data//")
txt = {}

i = 1

for file in files:
    if file[-4:] == ".txt":
        txt[str(i)] = file
        print("[{}] {}".format(i, file))
        i = i+1

"""while True:
	userInput = input()
	try: 
		int(userInput)
		break
	except: print("Use number")"""

l= 1

while i >= l:
    userInput = l
    fileName = txt[str(userInput)] [0:-4]

    fileLocation = r"Data/{}.txt".format(fileName)

    #   File selection for input file





    with open(fileLocation,"r") as data:
        fileContent = data.read()
    pt={
    } 
    
    d = {
    }

    patterns = [

    ]

    with open(r"colors.cfg", "r") as data:
        content = data.read().split("\n")
        for line in content:
            text, _, color = re.compile(' ?= ?(?=([^"]*"[^"]*")*[^"]*$)').split(line)

            colored = "<font color=\"{}\">".format(color)
            temp = '{}'.format(color)
            d[temp]=colored
    #   Add defined colors to dictionary
            pt[re.escape(text[1:-1])] = d[color]
            patterns.append((re.escape(text[1:-1]), d[color]))
    #   Add defined search patterns
    print(pt)
    
    
                    

    archive = open(r"Definitions/archive.txt","a+")
    
    globalPattern = re.compile(r"[A-Z][A-Z]([-]|[A-Z])*|" + '|'.join([i[0] for i in patterns]))
    matches = re.finditer(globalPattern, fileContent)

    titles = '<title>{} - Textmind</title><h3>{}</h3>\n'.format(fileName, fileName)

    finalString = "<pre>{}".format(titles)
    lastEnd = 0

    for match in matches:
        archive.write('\n' + fileName + ': ' + match.group())

    for pattern in pt.items():
        fileContent = re.sub(pattern[0], r'%s\g<0></font>' % pattern[1], fileContent)

    finalString += fileContent + '</pre>'


    archive.close() 
    output = open(r"Processed/{}.html".format(fileName),"w+")
    output.write(finalString)  
    output.close()
    #webbrowser.open(r"processed/{}.html".format(fileName), new = 0)

    exec(open("DefinitionsParser.py").read())
    #   Outputs and opens final file
    l= l+1
