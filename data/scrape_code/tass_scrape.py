# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:19:32 2019

@author: Patrick Stoyer
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

text = '''Events
It was the commendation of seomeone to do something 


Recommendation

HRW says something something and USA has to do something
HRW also ways US needs to do something something...
 '''
from selenium import webdriver
import time
from urllib import request 
##from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import pandas as pd
import bs4

options = webdriver.ChromeOptions()
options.add_argument('--lang=ru')
driver = webdriver.Chrome(options=options)

    
def get_links(site):
    driver.get(site)
    '''element = driver.find_element_by_xpath("//select")
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        print("Value is: %s" % option.get_attribute("value"))
        option.click()'''
    #select = Select(driver.find_element_by_xpath("//select[@class='b-mainpage-region-first ng-pristine ng-untouched ng-valid ng-scope ng-not-empty']"))

    
    """
    select = Select(driver.find_element_by_xpath('//select'))
    element = driver.find_element_by_xpath("//select")
    select.select_by_visible_text('Россия')
    all_options = element.find_elements_by_tag_name("option")
    
    
    time.sleep(3)
    for option in all_options:
        print("Value is: %s" % option.get_attribute("value"))
        option.submit()
    """
    for x in range(150):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        
    links = [path.get_attribute('href') for path in driver.find_elements_by_xpath("//div[@class='news-list__item ng-scope']/a")]
    driver.quit()
    return links

def get_text(page):
    response = request.urlopen(page)#request.urlopen returns html in bytes
    source = response.read().decode('utf-8') #decode bytes and append to source code list
    soup = bs(source, 'html.parser')
    text = soup.find('div',{'class':'text-content'})
    return text.text

def get_title(page):
    response = request.urlopen(page)#request.urlopen returns html in bytes
    source = response.read().decode('utf-8') #decode bytes and append to source code list
    soup = bs(source, 'html.parser')
    title = soup.find('h1',{'class':'news-header__title'})
    if title is None:
        title = soup.find('span',{'class':'article__title'})
    if title is None:
        print('NO TITLE')
        print(page)
        title = page
        return title
    return title.text

def get_time(page):
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=ru')
    driver = webdriver.Chrome(options=options)
    driver.get(page)
    element = driver.find_element_by_xpath("//dateformat/span")
    output=element.get_attribute('innerHTML')
    driver.close()
    return output[:output.index(",")]

def fix_names(filename):
   filename=filename.replace("\"",'')
   filename=filename.replace(":",'')
   filename=filename.replace("?",'')
   filename=filename.replace("/",'_')
   return filename

articles = get_links('https://tass.ru/v-strane')
print('Got {} articles...making DataFrame.'.format(len(articles)))
df = pd.DataFrame(articles)
df = df.rename(columns={0:"URL"})
print('Getting article titles')
df['Title']=df.URL.map(get_title)
df['Title'] = df.Title.map(fix_names)
print('Getting article dates')
df['Date']=df.URL.map(get_time)

for x in range (len(articles)):
    if (x % 100==0): 
        print('On article: {}'.format(x))
    filename='tass_articles/'+'_'.join(df.Title.iloc[x].split())+'_'+'_'.join(df.Date.iloc[x].split())+'.txt'
    with open(filename,'w+',encoding='utf-8')as f:
        f.write(get_text(df.URL.iloc[x]))
        
""" for x in range (len(articles)):
    if (x % 100==0): 
        print('On article: {}'.format(x))
    df['Title'][x] = fix_names(get_title(df['URL'][x]))
    
    #df['Date'][x] = get_time(df['URL'][x])
    filename='tass_articles/'+'_'.join(df['Title'][x].split()) +'.txt'#'_'.join(df['Date'][x].split())+'.txt'
    with open(filename,'w+',encoding='utf-8')as f:
        f.write(get_text(df.URL.iloc[x]))"""