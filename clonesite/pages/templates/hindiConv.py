from deep_translator import GoogleTranslator, MicrosoftTranslator, MyMemoryTranslator
import re
import csv
from bs4 import BeautifulSoup

my_translator = GoogleTranslator(source='en', target='hi')
#file_html = open("C:/Users/joser/OneDrive/Documentos/Cursos/curso-python/prueba miami/clonesite/index.html", "r", encoding = 'ISO-8859-1')
def turnIntoHindi(file_html, new_name):
    
    html = file_html.read()

    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    text = soup.get_text('\n')

    #print(soup.get_text())
    lines = [line for line in text.splitlines()]
    lines = list(set(lines))
    lines.remove('')
  
    
    

    
    lines.sort()
    if 'load static' in lines[-1]:
        lines.pop(-1)
    # for line in lines:
    #     print(line)

    lower_lines = [line.lower() for line in lines]
    charac = 0
    prev = 0
    hindi_lines=[]
    for n,line in enumerate(lower_lines):
        
        charac+=len(line)+1
        if charac >= 500:

            tanda = '\n'.join(lower_lines[prev:n])
            tanda = tanda.replace('â','')
            new_html = my_translator.translate(text=tanda)
            # new_html = GoogleTranslator(source='en', target='hi').translate(text=tanda)
            #new_html = MyMemoryTranslator(source='en', target='hi').translate(tanda)
            
            hindi_lines =hindi_lines +  new_html.split('\n')
            prev = n
            charac = len(line)+1


        if n == len(lower_lines)-1:
            tanda = '\n'.join(lower_lines[prev:len(lower_lines)])
            tanda = tanda.replace('â','')

            new_html = my_translator.translate(text=tanda)

            hindi_lines =hindi_lines +  new_html.split('\n')
            

    hindi_html = html[:]


    for line, hindi in zip(lines[::-1], hindi_lines[::-1]):
        #print(line)
        line_to_check = line[:]
        if '+' in line_to_check:
            line_to_check = line_to_check.replace('+','\+')
        if '[' in line_to_check:
            line_to_check = line_to_check.replace('[','\[')
        if '(' in line_to_check:
            line_to_check = line_to_check.replace('(','[(]')
        if ')' in line_to_check:
            line_to_check = line_to_check.replace(')','[)]')
        try:
            if re.search('>'+line_to_check, hindi_html):

                hindi_html = hindi_html.replace('>'+line,'>'+hindi)
                #print(hindi)
            elif re.search('>\n'+line_to_check, hindi_html):
                
                hindi_html = hindi_html.replace('>\n'+line,'>\n'+hindi)
                #print(hindi)
        except re.error:
            print(re.error)
            

    with open(new_name, 'w', encoding='utf-8') as f:
        f.write(hindi_html)
    f.close()

with open('namesforTrl.csv', 'r') as f:
    reader = f.readlines()
    reader = [reader[i] for i in range(len(reader)) if i % 2 ==0]
    reader = list(map(lambda x: (x[3:-5]),reader))
    print(reader[0])
f.close()

for filepage in reader:
    print(filepage)
    file_html = open(filepage+'.html','r',encoding = 'ISO-8859-1')
    turnIntoHindi(file_html,filepage+'.html')

