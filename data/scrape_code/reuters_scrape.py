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

feb = [x for x in range(1,29)]
jan = [x for x in range(1,32)]
april =[x for x in range (1,31)]

dates = {2018:{11:[x for x in range(27,31)],12:jan},2019:{1:jan,2:[x for x in range(1,26)]}}
formatted_dates = [("0" if y < 10 else "")+str(y)+("0" if z < 10 else "" )+str(z)+str(x) for x in dates for y in dates[x] for z in dates[x][y]]
sites = [('https://ru.reuters.com/news/archive/topNews?date={}'.format(x),x[-4:]+'-'+x[2:-4]+'-' +x[:2]) for x in formatted_dates]

def get_article_links(page, date):
    articles_list = []
    response = request.urlopen(page)#request.urlopen returns html in bytes
    source = response.read().decode('utf-8') #decode bytes and append to source code list
    soup = bs(source, 'html.parser')
    parent = soup.find('div',{'class':'module'}) #for loop through all the soups descendant
    for article in parent.children:
        temp_stuff = ['','']
        if isinstance (article, bs4.element.NavigableString):
            continue
        if article is None: return articles_list ##some dates have no articles
        
        temp_stuff[1] = article.find('a').text
        temp_stuff[0] = 'https://ru.reuters.com' + article.find('a').get('href').strip()
        articles_list.append([temp_stuff[0],temp_stuff[1],date])
    return articles_list
                        
def get_text(page):
    output =''
    response = request.urlopen(page)#request.urlopen returns html in bytes
    source = response.read().decode('utf-8') #decode bytes and append to source code list
    soup = bs(source, 'html.parser')
    body = soup.find('div',{'class':'StandardArticleBody_body'})
    """if body is None:
        body = soup.find ('header',{'class':'b-gallery__header'})
        if body is None:
            return ''
        for child in body.children:
            if isinstance (child, bs4.element.NavigableString):
                continue
            output +=child.text
        return output"""
    for child in body.children:
        if isinstance (child, bs4.element.NavigableString):
            continue
        if (child.name !='div'):
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
    articles.extend(get_article_links(site[0],site[1]))
print('Got articles...making DataFrame.')   
df = pd.DataFrame(articles)
df = df.rename(columns={0:"URL",1:"Title",2:"Date"})
df.Title = df.Title.map(fix_names)
for x in range (len(articles)):
    if (x % 100==0): 
        print('On article: {}'.format(x))
    filename='reuters_articles/'+'_'.join(df.Title.iloc[x].split())+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
    try:
        filename_bad='kommersant_articles/'+'_'.join(df.Title.iloc[x].split())+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
        try:
                os.remove(filename_bad)
        except: 
            pass
        with open(filename,'w+',encoding='utf-8',)as f:
          f.write(get_text(df.URL.iloc[x]))
      
    except OSError:
       try:
            filename='reuters_articles/'+'_'.join(df.Title.iloc[x].split()[:-5])+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
            filename_bad='kommersant_articles/'+'_'.join(df.Title.iloc[x].split()[:-5])+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
            try:
                os.remove(filename_bad)
            except: 
                pass
            with open(filename,'w+',encoding='utf-8',)as f:
                f.write(get_text(df.URL.iloc[x]))
       except OSError:
            filename='reuters_articles/'+'_'.join(df.Title.iloc[x].split()[:-10])+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
            filename_bad='kommersant_articles/'+'_'.join(df.Title.iloc[x].split()[:-10])+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
            try:
                os.remove(filename_bad)
            except: 
                pass
            with open(filename,'w+',encoding='utf-8',)as f:
                f.write(get_text(df.URL.iloc[x]))  
#df['Text'] = df.URL.map(get_text)"""
#df['Word_Tokens']=df.Text.map(nltk.word_tokenize)
#df['Sent_Tokens']=df.Text.map(nltk.sent_tokenize)