import pandas as pd
from ast import literal_eval
from langdetect import detect
from langdetect import DetectorFactory
DetectorFactory.seed = 0

df = pd.read_csv("Final.csv")


keyCounts = []
hasSpecTable = []
language = []

count = 1
for i in df['keyValuePairs']:
    print(count)
    # get kvp column as dict
    python_dict = literal_eval(i)

    # ----- count kvp -----
    keyCount = len(python_dict.keys())
    keyCounts.append(keyCount)

    # ----- language detection -----
    key1lang = ''
    if (keyCount > 0):
        try:
            key1lang = detect(str(python_dict))
        except:
            key1lang = ''
    language.append(str(key1lang))

    # ----- determine existence of specTable -----
    if len(python_dict.keys()) > 0:
        hasSpecTable.append("1")
    else:
        hasSpecTable.append("0")
    count=count+1
df['kvp_count'] = keyCounts
df['hasSpecTable'] = hasSpecTable
df['lang'] = language

df.to_csv("/Users/danielkhan/Downloads/combined_final_language.csv")
