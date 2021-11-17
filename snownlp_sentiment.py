#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 01:39:53 2021

@author: ian
"""
from snownlp import SnowNLP
import csv
# handle dialog_mom to shortlist the positive sentence
file = open("/home/ian/perfectmom/mom.txt",encoding='utf-8')
i=0
dialog_mom=[]
positive_index=[]
for line in file:
    s = SnowNLP('u'+line)
    sentiment_score=s.sentiments
    if sentiment_score>0.5:
        label="pos"
        positive_index.append(i)
    else:
        label="neg"
        
    dialog_mom.append([i,line,label,sentiment_score])
   
    i +=1

dialog_mom_pos = []
for item in dialog_mom:
    if item[2] == 'pos':
        dialog_mom_pos.append(item)
        
# handle dialog_son to shortlist the positive sentence according to 
# mom sentence sentiment
file = open("/home/ian/perfectmom/son.txt",encoding='utf-8')
i=0
dialog_son=[]
dialog_son_pospair=[]
for line in file:
    s = SnowNLP('u'+line)
    sentiment_score=s.sentiments
    if sentiment_score>0.5:
        label="pos"
    else:
        label="neg"
        
    dialog_son.append([i,line,label,sentiment_score])
    if i in positive_index:        
        dialog_son_pospair.append([i,line,label,sentiment_score])
    i +=1
    
# Save the generated pair

  
  
# field names 
fields = ['index', 'sentence', 'sentiment', 'sentiment_score'] 
    
# data rows of csv file 
  
with open('dialog_mom', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(dialog_mom)
    
with open('dialog_mom_pos', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(dialog_mom_pos)

with open('dialog_son', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(dialog_son)
with open('dialog_son_pospair', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(dialog_son_pospair)