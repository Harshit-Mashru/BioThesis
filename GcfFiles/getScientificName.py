import requests
import sys
import re
import os
from progress.bar import Bar

path = "./"

lst = os.listdir(path)

outFile = open('output.txt','w')

num = 0

for file in lst:

	if file[-4:] == ".fna":
		num += 1

bar = Bar('Processing', max = num)

for file in lst:

	if file[-4:] != ".fna":
		continue

	try:

		main_url = "https://www.ncbi.nlm.nih.gov/search/all/?term="

		term_to_search = file

		final_url = main_url + str(term_to_search)

		r = requests.get(final_url)

		content = r.content.decode()

		start = (re.search('<h4 class="ncbi-doc-title">', content, re.IGNORECASE).span())[1] + 1

		target = content[start : start+500]

		temp = (re.search('</h4>', target, re.IGNORECASE).span())[1] - 6

		final = target[:temp].strip().replace('\n','')

		final_list = final.split()

		answer = " ".join(final_list)
		
		outFile.write(answer + "\n")

		bar.next()

	except:
		
		pass

bar.finish()

outFile.close()