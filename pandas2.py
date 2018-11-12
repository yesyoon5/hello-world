#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm

data = pd.read_csv('2013_baseball.csv')

#print(data.loc[0])
#print(data.loc[0:3])
#print(data.loc[0], '선수명')
#print(data['선수명'])
df = data
#print(data.loc[:,['선수명','홈런']])
v1 = df['선수명']
v2 = df['홈런']
df2 = df[['선수명','홈런']]
#선수명으로 정렬
#print(df2.sort_values('선수명'))
#홈런의 수로 정렬
df2 = df2.sort_values('홈런', ascending=False)
#idex값 정렬
df2 = df2.reset_index(drop=True)
#print(df2)

#한글문제
path = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'
myFont = fm.FontProperties(fname = path).get_name()
fm.matplotlib.rc('font', family = myFont)

plt.bar(df2.선수명, df2.홈런)
plt.show()
