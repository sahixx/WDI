import pandas as pd
from ast import literal_eval
from langdetect import detect_langs
from langdetect import DetectorFactory
from textblob import TextBlob
from whatthelang import WhatTheLang
wtl

DetectorFactory.seed = 0

df = pd.read_csv("Final.csv")
df10 = df[:200].copy(deep=True)
keyCounts = []
hasSpecTable = []
language = []

for i in df10['keyValuePairs']:

    # get kvp column as dict
    python_dict = literal_eval(i)

    # ----- count kvp -----
    keyCount = len(python_dict.keys())
    keyCounts.append(keyCount)

    # ----- language detection -----
    key1lang = ''
    curr_key = 0
    while (keyCount > curr_key):
        if (len(list(python_dict)[curr_key]) >= 3):
            try:
                key1lang = detect_langs(list(python_dict)[curr_key])
            except:
                key1lang = ''
            break
        else:
            curr_key = curr_key + 1

    language.append(str(key1lang))

    # ----- determine existence of specTable -----
    if len(python_dict.keys()) > 0:
        hasSpecTable.append("1")
    else:
        hasSpecTable.append("0")

df10['kvp_count'] = keyCounts
df10['hasSpecTable'] = hasSpecTable
df10['lang'] = language

df10.to_csv("/Users/danielkhan/Downloads/combined_final_language.csv")
