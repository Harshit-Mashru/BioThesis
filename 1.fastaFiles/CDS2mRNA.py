import Bio
import sys
from Bio import SeqIO
import os

# For everything to work perfectly, make a parent directory (by any name)
# Now make 2 sub-directories: fastaFiles & mRNAFiles
# Paste all the CDS files and this python file in the fastaFiles folder
# The extension for all those fasta files can be .fasta or .txt

# Run python3 CDS2mRNA.py and all mRNA files will be made in the mRNAFiles folder

# Now we do further analysis in the mRNAFiles Folder.

path = "./"

lst = os.listdir(path)

for fileName in lst:
	
	#fileName = sys.argv[1]
	
	if fileName == "CDS2mRNA.py":
		continue

	l = fileName.split(".")
	
	if l[-1] != "fasta" and l[-1] != "txt":
		continue

	newFile = ""
	
	for i in range(len(l)-1):
	
		newFile += l[i] + "."

	newFile += "mRNA"
	
	file = open("../2.mRNAFiles/" + newFile, 'w', encoding = 'utf-8')

	for seq_record in SeqIO.parse(fileName, 'fasta'):

		file.write(">" + seq_record.description + "\n")
		if "complement(" in seq_record.description:
			template_strand = seq_record.seq.reverse_complement()
			#print(repr(template_strand.transcribe()))
			file.write(str(template_strand.transcribe()) + "\n\n")
		else:

			file.write(str(seq_record.seq.transcribe()) + "\n\n")
		
	file.close()