# Limitations of the code
# 1) If a line has offset of more than 5 digits i.e the offset value is > 99999, then the code fails to write the correct offset value, this wont happen in a normal
# cases, as mRNAs aren't that long.

import matplotlib.pyplot as plt
import forgi.visual.mplotlib as fvm
import forgi
import os
import sys
import re

path = "./"

lst = os.listdir(path)

for fileName in lst:
	
	if fileName == "dotBracket2Seq.py":
		continue

	l = fileName.split(".")
	
	if l[-1] != "lfold" and l[-1] != "txt":
		continue

	newFile = ""
	
	for i in range(len(l)-1):
		
		if i == len(l)-2:
			newFile += l[i]
		else:
			newFile += l[i] + "."


	newFile += "_filtered" + "."
	newFile += "seq"

	# This new file with extension fx will save the filtered RNAs which can be potential small RNAs.

	file = open(fileName, 'r')
	lines = file.readlines()
	#itr = 0
	filteredFile = open("../4.finalSequences/" + newFile, 'w', encoding = 'utf-8')
	#filteredFile = open(newFile, 'w')
	lastline = ""

	stored = []

	for line in lines:
		#itr += 1
		if(line[0] == ">"):
			filteredFile.write(line)
			continue

		if(line[0] == " "):
			#filteredFile.write(line)
			continue

		if(line[0] != "." and line[0] != "("):
			#filteredFile.write(line)
			# This is actual sequence
			
			for dotBracketSeq in stored:
				filteredFile.write(dotBracketSeq)
				temp = dotBracketSeq.split(".")
				offset = int(temp[-1])

				seq = ""
				for j in range(len(dotBracketSeq)):
					if(dotBracketSeq[j] == " "):
						seq += "\n"
						filteredFile.write(seq)
						break
					
					seq += line[offset + j]

			stored = []


		# Filter stuff here and then write to filteredFile if satisfies the criteria of length and threshold
		
		offset = 0
		f = re.search("\.(\(\.{0,2}){24}\.{3,15}(\)\.{0,2}){23}\)\.", line)
		if f != None:
			offset = int(line[-6:]) + f.start()
			newLine = f.group(0) + " " + str(offset) + "\n"
			if newLine != lastline:
				#filteredFile.write(newLine)
				stored.append(newLine)
			lastline = newLine
			continue
		e = re.search("\.(\(\.{0,2}){23}\.{3,15}(\)\.{0,2}){22}\)\.", line)
		if e != None:
			offset = int(line[-6:]) + e.start()
			newLine = e.group(0) + " " + str(offset) + "\n"
			if newLine != lastline:
				#filteredFile.write(newLine)
				stored.append(newLine)
			lastline = newLine
			continue
		d = re.search("\.(\(\.{0,2}){22}\.{3,15}(\)\.{0,2}){21}\)\.", line)
		if d != None:
			offset = int(line[-6:]) + d.start()
			newLine = d.group(0) + " " + str(offset) + "\n"
			if newLine != lastline:
				#filteredFile.write(newLine)
				stored.append(newLine)
			lastline = newLine
			continue
		c = re.search("\.(\(\.{0,2}){21}\.{3,15}(\)\.{0,2}){20}\)\.", line)
		if c != None:
			offset = int(line[-6:]) + c.start()
			newLine = c.group(0) + " " + str(offset) + "\n"
			if newLine != lastline:
				#filteredFile.write(newLine)
				stored.append(newLine)
			lastline = newLine
			continue
		b = re.search("\.(\(\.{0,2}){20}\.{3,15}(\)\.{0,2}){19}\)\.", line)
		if b != None:
			offset = int(line[-6:]) + b.start()
			newLine = b.group(0) + " " + str(offset) + "\n"
			if newLine != lastline:
				#filteredFile.write(newLine)
				stored.append(newLine)
			lastline = newLine
			continue
		a = re.search("\.(\(\.{0,2}){19}\.{3,15}(\)\.{0,2}){18}\)\.", line)
		if a != None:
			offset = int(line[-6:]) + a.start()
			newLine = a.group(0) + " " + str(offset) + "\n"
			if newLine != lastline:
				#filteredFile.write(newLine)
				stored.append(newLine)
			lastline = newLine
			continue

	filteredFile.close()

# This part is for plotting the mRNAs. But first we need to filter the output of the lfold files to include only those mRNAs that are useful to us.
# Criteria for selection was stem and loop length.
'''
for fileName in lst:

	if fileName == "dotBracket2Figure.py":
		continue

	l = fileName.split(".")
	
	if l[-1] != "lfold" and l[-1] != "txt":
		continue

	newFile = ""
	
	for i in range(len(l)-1):
	
		newFile += l[i] + "."

	newFile += "jpeg"
	
	cg = forgi.load_rna(fileName, allow_many=False)
	fvm.plot_rna(cg, text_kwargs={"fontweight":"black"}, lighten=0.7, backbone_kwargs={"linewidth":3})
	plt.savefig("../plottedRNA" + newFile)
'''
