import os
import sys
import re

path = "./"

lst = os.listdir(path)

for fileName in lst:
	
	if fileName == "filterStemPart.py":
		continue

	l = fileName.split(".")
	
	if l[-1] != "seq":
		continue

	newFile = ""
	
	for i in range(len(l)-1):
		
		if i == len(l)-2:
			newFile += l[i]
		else:
			newFile += l[i] + "."


	newFile += "." + "stemSeq"

	file = open(fileName, 'r')
	lines = file.readlines()
	
	filteredFile = open("../5.stemSequences/" + newFile, 'w', encoding = 'utf-8')
	
	lastLine = ""

	for line in lines:

		if(line[0] == ">"):
			filteredFile.write(line)
			continue

		elif(line[0] == "."):
			lastLine = line
			continue

		else:
			match = re.search("\.{3,15}", lastLine)
			if match == None:
				continue
			else:
				offset = match.start()
				end = match.end()

				lineToWrite = line[:offset] + " " + line[end:]
				otherLine = lastLine[:offset] + " " + lastLine[end:]
				filteredFile.write(otherLine)
				filteredFile.write(lineToWrite)
	
	filteredFile.close()
