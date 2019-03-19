# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 00:30:50 2019

@author: Patrick Stoyer
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:03:58 2019

@author: Patrick Stoyer
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:19:32 2019

@author: Patrick Stoyer
"""


from selenium import webdriver
import time
from urllib import request 
##from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import pandas as pd
import bs4
import os

sites = ['https://www.bbc.com/russian/search/?q=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F&start={}'.format(10*x+1) for x in range (35)]

def get_article_links(page):
    articles_list = []
    response = request.urlopen(page)#request.urlopen returns html in bytes
    source = response.read().decode('utf-8') #decode bytes and append to source code list
    soup = bs(source, 'html.parser')
 
    for article in soup.find_all('div',{'class':'hard-news-unit hard-news-unit--regular faux-block-link'}):
        temp_stuff = ['','','']
        if isinstance (article, bs4.element.NavigableString):
            continue
        temp_stuff[1] = article.find('h3').text
        temp_stuff[2] = article.find('div',{'class':'date date--v2'}).text
        temp_stuff[0] = article.find('a').get('href').strip()
        articles_list.append([temp_stuff[0],temp_stuff[1],temp_stuff[2]])
        
    return articles_list
                        
def get_text(page):
    output =''
    response = request.urlopen(page)#request.urlopen returns html in bytes
    source = response.read().decode('utf-8') #decode bytes and append to source code list
    soup = bs(source, 'html.parser')
    body = soup.find('div',{'property':'articleBody'})
    if body is None:
        body = soup.find ('div',{'class':'vxp-media__summary'})
        if body is None:
            return ''
        for child in body.children:
            if isinstance (child, bs4.element.NavigableString):
                continue
            output +=child.text
        return output
    for child in body.children:
        if isinstance (child, bs4.element.NavigableString):
            continue
        if ((child.name !='div') and (child.name !='figure') and (child.name !=  'ul')):
            output +=child.text
            output +="\n"
    return output

def fix_names(filename):
   filename=filename.replace("\"",'')
   filename=filename.replace(":",'')
   filename=filename.replace("?",'')
   filename=filename.replace("/",'_')
   return filename


articles=[]
for site in sites:
    articles.extend(get_article_links(site))
print('Got articles...making DataFrame.')   
df = pd.DataFrame(articles)
df = df.rename(columns={0:"URL",1:"Title",2:"Date"})
df.Title = df.Title.map(fix_names)

for x in range (len(articles)):
    if (x % 100==0): 
        print('On article: {}'.format(x))
    filename='bbc_articles/'+'_'.join(df.Title.iloc[x].split())+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
    try:
        with open(filename,'w+',encoding='utf-8',)as f:
          f.write(get_text(df.URL.iloc[x]))
      
    except OSError:
       try:
            filename='bbc_articles/'+'_'.join(df.Title.iloc[x].split()[:-5])+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
           
            with open(filename,'w+',encoding='utf-8',)as f:
                f.write(get_text(df.URL.iloc[x]))
       except OSError:
            filename='bbc_articles/'+'_'.join(df.Title.iloc[x].split()[:-10])+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
            
            with open(filename,'w+',encoding='utf-8',)as f:
                f.write(get_text(df.URL.iloc[x]))  
#df['Text'] = df.URL.map(get_text)"""
#df['Word_Tokens']=df.Text.map(nltk.word_tokenize)
#df['Sent_Tokens']=df.Text.map(nltk.sent_tokenize)