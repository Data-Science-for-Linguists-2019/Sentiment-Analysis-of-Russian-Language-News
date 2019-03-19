# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 01:14:12 2019

@author: Patrick Stoyer
"""

from urllib import request #to get html source code from websites
from bs4 import BeautifulSoup #to process source code
import pandas as pd
import bs4


sites_list = ['https://www.svoboda.org/z/16685?p={}'.format(x) for x in range(1,101)]
def get_article_links(page):
    articles_list = []
    response = request.urlopen(page)#request.urlopen returns html in bytes
    source = response.read().decode('utf-8') #decode bytes and append to source code list
    soup = BeautifulSoup(source, 'html.parser')
    for parent in soup.descendants: #for loop through all the soup's descendant
            if (parent.name =='li') and(parent.has_attr('class'))and (['col-xs-12', 'col-sm-12', 'col-md-12', 'col-lg-12'] == parent.get('class')):
                temp_stuff = ['','','','','',''] #this temporary list will hold various information to be stored
                for child in parent.descendants: #if the name is 'article' then loop through the parents children
                    if isinstance (child, bs4.element.NavigableString):
                        continue
                    if(child.has_attr('class') and (child.get('class')[0] == 'title')) :  #if a childs name is 'p' it will hold the country info
                        temp_stuff[1] = child.string.strip()
                    elif child.name == 'a' : #if a child's name is 'a' it will hold the hyperlink
                        temp_stuff[0] = 'https://www.svoboda.org' + child.get('href').strip()
                    elif (child.has_attr('class') and (child.get('class')[0] == 'date')):
                        temp_stuff[2] = child.string.strip()
                articles_list.append([temp_stuff[0],temp_stuff[1],temp_stuff[2]])
    return articles_list
                        
def get_text(page):
    output =''
    response = request.urlopen(page)#request.urlopen returns html in bytes
    source = response.read().decode('utf-8') #decode bytes and append to source code list
    soup = BeautifulSoup(source, 'html.parser')
    body = soup.find('div',{'id':'article-content'})
    for child in body.div.children:
        if isinstance (child, bs4.element.NavigableString):
            continue
        if ((child.name !='div')and(child.name != 'template')):
            if (child.name != 'ul'):
                output +=child.text
                output +="\n"
            else:
                for baby_child in [x for li in child.children if not isinstance(li, bs4.element.NavigableString) for x in li.contents]:
                    if isinstance(baby_child,bs4.element.NavigableString):
                        output +=baby_child
                     
                    elif (baby_child.name =='a'):
                        output += baby_child.text   
                    
                    elif (baby_child.name !='div'):
                        output +=baby_child.text
                        
                output +="\n"
    return output

def fix_names(filename):
   filename=filename.replace("\"",'')
   filename=filename.replace(":",'')
   filename=filename.replace("?",'')
   filename=filename.replace("/",'_')
   return filename


articles=[]
for site in sites_list:
    articles.extend(get_article_links(site))
print('Got articles...making DataFrame.')
df = pd.DataFrame(articles)
df = df.rename(columns={0:"URL",1:"Title",2:"Date"})
df.Title = df.Title.map(fix_names)

for x in range (len(articles)):
    if (x % 100==0): 
        print('On article: {}'.format(x))
    filename='radio_svoboda_articles/'+'_'.join(df.Title.iloc[x].split())+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
    with open(filename,'w+',encoding='utf-8')as f:
        f.write(get_text(df.URL.iloc[x]))
#df['Text'] = df.URL.map(get_text)"""
#df['Word_Tokens']=df.Text.map(nltk.word_tokenize)
#df['Sent_Tokens']=df.Text.map(nltk.sent_tokenize)