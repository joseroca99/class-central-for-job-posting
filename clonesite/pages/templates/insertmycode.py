

def insertMyCode(file_html,new_name):
    html = file_html.read()
    html = html.replace('<!DOCTYPE html>','<!DOCTYPE html>\n{%load static%}')
    html = html.replace('</body>','<script src=\'{%static "js/dropdown.js"%}\'></script>\n</body>')
    with open(new_name, 'w', encoding='utf-8') as f:
        f.write(html)
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
    insertMyCode(file_html,filepage+'.html')