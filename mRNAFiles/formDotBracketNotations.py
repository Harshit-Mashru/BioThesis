import sys
import os
import subprocess
from progress.bar import Bar

path = "./"

lst = os.listdir(path)

num = 0

for file in lst:

	if file[-5:] == ".mRNA":
		num += 1

bar = Bar('Processing', max = num)

for fileName in lst:

	bar.start()

	if fileName == "formDotBracketNotations.py":
		continue

	l = fileName.split(".")
	
	if l[-1] != "mRNA":
		continue

	newFile = ""
	
	for i in range(len(l)-1):
	
		newFile += l[i] + "."

	newFile += "lfold"

	temp = "--outfile="+newFile

	subprocess.run(["RNALfold", "-i", fileName, temp])

	bar.next()

bar.finish()

subprocess.run('mv *.lfold ../dotBracketNotations', shell=True)