from urllib import request, error
from bs4 import BeautifulSoup
import re
import csv
import time

class ListOfUrls:
    
    def __init__(self,raw_urls):
        self.raw_urls=raw_urls
        
        prelist = raw_urls[:]
        for i in range(len(prelist)):
            if re.search('^/.',prelist[i]):
                prelist[i] = 'https://www.classcentral.com'+ prelist[i]
        self.complete_urls = prelist
        self.name_files = list(map(lambda x: (x[29::].replace('/','-')), self.complete_urls))
        self.name_urls = list(map(lambda x: (x[29::]), self.complete_urls))
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
            

file_html = open("C:/Users/joser/OneDrive/Documentos/Cursos/curso-python/prueba miami/clonesite/index.html", "r", encoding = 'ISO-8859-1')
html = file_html.read()
pattern='<a.*href="[^"]*"'

matches = re.findall(pattern,html)
print(len(matches))


raw_urls=[]
check=[]
for match in matches:
    
    href = re.findall('href="[^"]*"',match)
    link = re.findall('"[^"]*"',href[0])[0][1:-1]
    #print(link)
    if re.search('^/.',link) or re.search('https://www.classcentral.com',link):    
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