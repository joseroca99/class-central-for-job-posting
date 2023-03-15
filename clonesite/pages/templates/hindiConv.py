from deep_translator import GoogleTranslator
import re
from pathlib import Path
from bs4 import BeautifulSoup

#set to translate from english to hindi, change source and target values to change the languages
my_translator = GoogleTranslator(source='en', target='hi')
def turnIntoHindi(file_html, new_name):
    
    html = file_html.read()

    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    text = soup.get_text('\n')

    lines = [line for line in text.splitlines()]
    lines = list(set(lines))
    lines.remove('')
    lines.sort()
    if 'load static' in lines[-1]:
        lines.pop(-1)

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


INDEX_PATH = Path(__file__).parent.parent.parent.resolve()
with open( INDEX_PATH / 'namesforTrl.csv', 'r') as f:
    reader = f.readlines()
    reader = [reader[i] for i in range(len(reader)) if i % 2 ==0]
    reader = list(map(lambda x: (x[3:-5]),reader))
    print(reader[0])
f.close()

for filepage in reader:
    print(filepage)
    file_html = open(filepage+'.html','r',encoding = 'ISO-8859-1')
    turnIntoHindi(file_html,filepage+'.html')

