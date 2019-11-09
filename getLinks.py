#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:17:11 2019

@author: shinggg
"""

import requests

#roadshowType = 5 # 5: 业绩说明会
roadshowType = 12 # 12: 投资者说明会

url = 'http://rs.p5w.net/roadshow/getRoadshowList.shtml'

data = {'perComType':0,
       'roadshowType':roadshowType,
       'companyType':None,
       'roadshowDate':None,
       'page':0,
       'rows':13000
       }
s = requests.Session()
r = s.post(url, data=data)

#print(r.headers)
#print(r.status_code)
#print(r.url)
#print(r.content)
aaa= r.text

#ss = requests.post(url, data=data)

import json
aaa_d = json.loads(aaa)

#for k,i in enumerate(aaa_d['rows']):
#    print(k+1, i['perRealname'], i['companyShortname'], i['roadshowTypeName'], i['shareWXUrl'])

import pandas as pd
df = pd.DataFrame.from_dict(aaa_d['rows'])
df.to_csv('roadshowType-'+str(roadshowType)+'.csv')
