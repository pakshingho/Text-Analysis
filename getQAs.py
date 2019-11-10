#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:42:28 2019

@author: shinggg
"""

import requests
import json
import pandas as pd

url = 'http://rs.p5w.net/roadshowLive/getNInteractionDatas.shtml'

data = {'roadshowId':'0001479025D51EF04D528FFC803FEADBE95D', # This is 'pid' in the csv-file which contains all the links.
        'isPagination':None,
        'rows':None,
        'type':2, # type 1 is all, type 2 is Q&A
        'page':None
       }
s = requests.Session()
r = s.post(url, data=data)
aaa=r.text

# Convert text to dictionary:
import json
aaa_d = json.loads(aaa)

# Convert dictionary to dataframe:
import pandas as pd
df = pd.DataFrame.from_dict(aaa_d['rows'])

# Extract reply answers from 'replyList' column cells:
df.loc[df['replyList'].isna(), 'replyList'] = [[{}.fromkeys(df['replyList'].str[0][1], None)]] # Convert None into dictionary with all None values.

#df_reply = pd.DataFrame(df['replyList'].apply(pd.Series).iloc[:,0].to_list())
df_reply = pd.DataFrame(df['replyList'].str[0].to_list())
