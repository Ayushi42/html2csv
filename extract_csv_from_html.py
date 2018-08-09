from bs4 import BeautifulSoup
import sys
import os

def extract_csv(filename,soup):
	rows=["row"+str(i) for i in [1,15,10,-1,-1,-1,-1,-1,2,3,4,5,6,7,8,9,11,12,13,14,16]]
	filename=".".join(filename.split('.')[:-1])
	folder=filename
	if not os.path.exists(folder):
		os.makedirs(folder)
	sents=[tag for tag in soup.findAll('td',{"class":"outertd"})]
	temp=""
	for i in range(len(sents)):
		if "Anu translation" in sents[i].get_text():
			temp+=sents[i-1].get_text().strip()
			temp+="\n"
			temp+=sents[i].get_text().strip()
			temp+="\n"
			temp+=sents[i+1].get_text().strip()
			temp+="\n"
	for i in rows:
		entries=[]
		for tag in soup.findAll('tr',{"class":i}):
			if len(tag.findAll('script'))!=0:
				tag.findAll('script')[0].replaceWith('')
			elif len(tag.findAll('span'))!=0:
				for t in tag.find_all('span'):
					t.replaceWith('')
			if entries==[] and i=="row1":
				number=".".join(tag.get_text().split('.')[:-1]).strip()
				number+=".txt"
			entries=entries+[j for i in  tag.findAll('td') for j in i.get_text().strip().replace('...','').split()] 	
		#print (entries)
		temp+="`".join(entries)
		temp+="\n"
	file=open(folder+"/"+number,"w")
	file.write(temp)
	file.close()


def main():
	soup=BeautifulSoup(open(sys.argv[-1]).read(),"lxml")
	print(sys.argv[-1])
	tables=[i for i in soup.findAll('table') if "Parser Alignment info" in i.get_text()]
	for i in tables:
		extract_csv(sys.argv[-1],i)

if __name__ == '__main__':
	main()
