from bs4 import BeautifulSoup
import re
from pathlib import Path

#insert the index link here
baseurl = 'insert the index link here'

class ListOfUrls:
    
    def __init__(self,raw_urls):
        self.raw_urls=raw_urls
        
        prelist = raw_urls[:]
        for i in range(len(prelist)):
            if re.search('^/.',prelist[i]):
                prelist[i] = baseurl+ prelist[i]
        self.complete_urls = prelist
        self.name_files = list(map(lambda x: (x[len(baseurl)+1::].replace('/','-')), self.complete_urls))
        self.name_urls = list(map(lambda x: (x[len(baseurl)+1::]), self.complete_urls))
        auxlist = self.name_files[:]
        self.name_views = []
        for item in auxlist:
            aux = re.split('-',item)
            strSum = ''
            for i in range(len(aux)):
                strSum += aux[i].capitalize()
            self.name_views.append(strSum)


    def raw_list(self):
        return self.raw_urls
    
    def complete_list(self):
        return self.complete_urls
    
    def html_maker(self):
        
        return self.name_files
    
    def url_maker(self):
        
        return self.name_urls
    
    def view_maker(self):
        
        return self.name_views
            

INDEX_PATH = Path(__file__).parent.resolve()
file_html = open(INDEX_PATH / 'index.html', "r", encoding = 'ISO-8859-1')
html = file_html.read()
pattern='<a.*href="[^"]*"'

matches = re.findall(pattern,html)

raw_urls=[]
check=[]
for match in matches:
    
    href = re.findall('href="[^"]*"',match)
    link = re.findall('"[^"]*"',href[0])[0][1:-1]
    if re.search('^/.',link) or re.search(baseurl,link):    
        raw_urls.append(link)
    
raw_urls= list(set(raw_urls))
print(len(raw_urls))
raw_urls = list(filter(lambda x : (len(x)) > 1, raw_urls))
raw_urls.sort()

VariousLists = ListOfUrls(raw_urls)

new_html = html
raw_list= VariousLists.raw_list()[::-1]
html_maker= VariousLists.html_maker()[::-1]

for raw,tag in zip(raw_list,html_maker):
    print(raw+' , '+tag )
    new_html = re.sub(raw,"{% url '"+tag+"'%}",new_html)

with open('new_index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
f.close()