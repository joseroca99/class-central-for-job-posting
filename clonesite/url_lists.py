from urllib import request
from bs4 import BeautifulSoup
import re
from pathlib import Path
import csv



def extractHtml(baseurl,namefile):
    opener = request.build_opener()
    #defining headers as some servers mandiate it
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
                            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                            ('Connection', 'keep-alive')
                        ]
    request.install_opener(opener)
    html_doc = request.urlopen(baseurl).read()

    soup = BeautifulSoup(html_doc, 'lxml')
    f = open( namefile, 'w', encoding='utf-8' )
    f.write(str(soup))
    f.close()

#insert the index link here
baseurl = 'insert the index link here'
###Uncomment to retreive the index file, once retreived, please comment again
# extractHtml(baseurl,'index.html')

class ListOfUrls:

    def __init__(self,raw_urls):
        self.raw_urls=raw_urls
        prelist = raw_urls
        for i in range(len(prelist)):
            if re.search('^/.',prelist[i]):
                prelist[i] = baseurl+ prelist[i]
        self.complete_urls = prelist
        self.name_files = list(map(lambda x: (x[len(baseurl)+1::].replace('/','-')), self.complete_urls))
        self.name_urls = list(map(lambda x: (x[len(baseurl)+1::]), self.complete_urls))
        auxlist = self.name_files
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
print(len(matches))


raw_urls=[]
check=[]
for match in matches:
    
    href = re.findall('href="[^"]*"',match)
    link = re.findall('"[^"]*"',href[0])[0][1:-1]
    #print(link)
    if re.search('^/.',link) or re.search(baseurl,link):    
        raw_urls.append(link)
    

raw_urls= list(set(raw_urls))
print(len(raw_urls))
raw_urls = list(filter(lambda x : (len(x)) > 1, raw_urls))
raw_urls.sort()

VariousLists = ListOfUrls(raw_urls)

### Uncomment to extract each page for each url in the index page
# for link_0,link_1 in zip(VariousLists.complete_list(),VariousLists.html_maker()):
#     try:
#         extractHtml(link_0,link_1+'.html')
#         print(link_0)
#     except error.HTTPError:
#         time.sleep(5)
#         extractHtml(link_0,link_1+'.html')
#         print(link_0)

### Uncomment to created a django Class based View with TemplateView for each url
# with open('viewsfordjango.txt', 'w') as f:
#     for view,template in zip(VariousLists.view_maker(),VariousLists.html_maker()):
#         f.write(
#             "class "+view+"View(TemplateView):\n    template_name = '"+template+".html'\n\n"
#             )
#     f.close()

### Uncomment to create a django urlpattern element using Class based Views for each url
# with open('urlsfordjango.txt', 'w') as f:
#     for url,view,name in zip(VariousLists.url_maker(),VariousLists.view_maker(), VariousLists.html_maker()):
#         f.write(
#             "path('" +url+ "'," +view+ "View.as_view(), name='" +name+"'),\n"
#             )
#     f.close()

# # Uncomment to create a csv list of the html file names
# with open('namesforTrl.csv', 'w') as f:
#     writer=csv.writer(f)
#     for name in zip(VariousLists.html_maker()):
#         writer.writerow([name,])
#     f.close()







