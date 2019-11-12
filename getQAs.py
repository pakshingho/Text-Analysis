#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:42:28 2019

@author: shinggg
"""

# Need also download the parts from this page: 
# http://rsc.p5w.net/rsc/sme/yjsmh/yjsmh.html

import requests
import json
import pandas as pd


####################
# Part 1 newer part
#################
pid = pd.read_csv('roadshowType-12.csv', usecols=['pid']).pid[0:113]

url = 'http://rs.p5w.net/roadshowLive/getNInteractionDatas.shtml'

for i in pid:
    data = {'roadshowId':i, # This is 'pid' in the csv-file which contains all the links.
            'isPagination':None,
            'rows':None,
            'type':2, # type 1 is all, type 2 is Q&A
            'page':None
           }
    r = requests.post(url, data=data)
    text = r.text
    
    # Convert text to dictionary:
    text_dict = json.loads(text)
    
    # Convert dictionary to dataframe:
    df = pd.DataFrame.from_dict(text_dict['rows'])
    df.to_csv('roadshowType-12-text/' + str(i) + '.csv', index=False)

print('Download done.')

# Extract reply answers from 'replyList' column cells:
df.loc[df['replyList'].isna(), 'replyList'] = [[{}.fromkeys(df['replyList'].str[0][1], None)]] # Convert None into dictionary with all None values.

#df_reply = pd.DataFrame(df['replyList'].apply(pd.Series).iloc[:,0].to_list())
df_reply = pd.DataFrame(df['replyList'].str[0].to_list())

#############################
# Part 2 older part
#######################
url = 'http://zsptbs.p5w.net/bbs/chatbbs/left.asp?boardid=1271'
#url = 'http://zsptbs.p5w.net/bbs/chatbbs/left.asp?boardid=1271&pageNo=2'

data = {'boardid':1271,
        'pageNo':1}

s = requests.Session()
r = s.get(url, data=data)
r.encoding = r.apparent_encoding
aaa=r.text