# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:56:17 2019

@author: Patrick Stoyer
"""

from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

#This function lemmatizes and gets rid of punctuation
def preprocess_text(text):
    mystem = Mystem() 
    rs = ''
    for x in stopwords.words('russian'):
        rs += x+" "
    rs = mystem.lemmatize(rs)
    russian_stopwords = list(set(stopwords.words("russian") + rs +["который","это", "считать","радио","сказать", "/ТАСС/", "тыс", "млн","млрд", "президент", "весь", "год","“","”, - "," “","сообщать",') - ',"”","мочь","также","” ","время",""]))
    mystem = Mystem()
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if (token not in russian_stopwords) and (token != " ") and (token.strip() not in punctuation)]
    
    return tokens

import os, pandas as pd
folder_path = r'C:\Users\Patrick Stoyer\Dropbox\Documents\Sophomore Year\Semester_2\Ling_1340_Data_Science_for_Linguists\Project\art\rad'
   
#this function gets all of the texts and puts them in a series
def make_text():
    os.chdir(folder_path)
    text = []  
    files = os.listdir()
    for file in range(len(files)):
        if ((file % 25 == 0) & (file > 0)): print("Finished file {}".format(file))
        with open(files[file], 'r', encoding ='utf-8') as f:
            text.append(f.read())
    return pd.Series(text)

print("Getting texts...")
unprocessed_files = make_text()
print("Finished getting texts... Processing texts...")
files = unprocessed_files
for file in range(len(unprocessed_files)):
    if ((file % 25 == 0)): print("Processed file {}".format(file))
    files[file] = preprocess_text(unprocessed_files[file])

        
from gensim.corpora import Dictionary

print("Finished processing texts... Making dictionary...")
dictionary = Dictionary(files) #finds all unique words i think
print("Finished making dictionary... Converting to bag of words...")
bow_corp = [dictionary.doc2bow(file) for file in files] ##the counts of each word's occurrence in the data set

import gensim

print("Finished converting to bag of words... Making lda model...")
lda = gensim.models.ldamodel.LdaModel(bow_corp, num_topics = 200, id2word=dictionary, update_every=0, passes=20)
os.chdir(folder_path[:-8]+"\gensim")
lda.save('ldamodel_rad.gensim')
topics = lda.print_topics(20)
print("Printing topics...")
with open('rad_lda.txt', 'w', encoding='utf-8') as f:
    for topic in topics:
        print("Topic {}: ".format(topic[0]+1)+"\n\t"+('\n\t'.join([x.strip() for x in topic[1].replace('*',':\t\t').split('+')]))+"\n")
        f.write("Topic {}: ".format(topic[0]+1)+"\n\t"+('\n\t'.join([x.strip() for x in topic[1].replace('*',':\t\t').split('+')]))+"\n")
        
files.to_pickle('rad_lemmatized_series.pkl')

print("Finished lda model... Now let's try an lsa model...")
tfidf=gensim.models.TfidfModel(bow_corp)
lsi = gensim.models.lsimodel.LsiModel(corpus=tfidf.__getitem__(bow=bow_corp), id2word=dictionary, num_topics=400)
lsi.save('lsimodel_rad.gensim')
topics = lsi.print_topics(20)
print("Printing topics...")
with open('rad_lsa.txt', 'w', encoding='utf-8') as f:
    for topic in topics:
        print("Topic {}: ".format(topic[0]+1)+"\n\t"+('\n\t'.join([x.strip() for x in topic[1].replace('*',':\t\t').split('+')]))+"\n")
        f.write("Topic {}: ".format(topic[0]+1)+"\n\t"+('\n\t'.join([x.strip() for x in topic[1].replace('*',':\t\t').split('+')]))+"\n")
        