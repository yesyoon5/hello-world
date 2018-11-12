#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:44:42 2018

@author: hadoop
"""

import pandas as pd
import numpy as np

#data = [1, 3, 5, 7, 9]
#
#print(type(data))
#print(data)
#
#s = pd.Series(data)
#print(type(s))
#print(s)
#########################Ctrl + 1 블록주석
data = {"연도":[2016,2017,2018],
        "GDP":[2.8, 3.1, 3.0],
        "순위":[3, 1, 2]}
df = pd.DataFrame(data)

#print(df)
#print(df["연도", "GDP"]) # error
print(df[["연도", "GDP"]])
# 데이터프레임에 동일한 값 삽입
df["급여"] = [100, 300, 200]
print(df)

df["CIndex"] = ['C', 'A', 'B']
print(df)

df["DIndex"] = np.arange(3)+1
#df["DIndex"] = np.arange(1, 4)
print(df)

val = pd.Series(['가', '나', '다'], index=[1,2,0])
df["옵션"] = val
print(df)