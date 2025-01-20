# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MBvQIrxddjjub6VS53SgPmOSaL4wjQ0E
"""

from google.colab import userdata
import requests
import pandas as pd
import xml.etree.ElementTree as ET


url = 'http://kopis.or.kr/openApi/restful/pblprfr'

params = {
    'service': userdata.get('key'),
    'stdate': '20230601',
    'eddate': '20230630',
    'cpage': 1,
    'rows': 100,
    'signgucode': '11',
    'kidstate': 'N'
}


response = requests.get(url, params=params)

root = ET.fromstring(response.text)

row_dict = {
    'mt20id': [], 'prfnm': [], 'prfpdfrom': [], 'prfpdto': [], 'fcltynm': [], 'poster': [], 'area': [], 'genrenm': [], 'openrun': [], 'prfstate': []
}

for i in root.findall('.//db'):
  for j in i:
       row_dict[j.tag].append(j.text)
df = pd.DataFrame(row_dict)
df.head()