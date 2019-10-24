# import pandas package to read n merger csv files
import pandas as pd
# import pachkage json for parsing json files
import json as js
# import csv package for reading from and writting into csv file
import csv as csv
import io

# reading from the csv file into a dataframe
df = pd.read_csv('./categories_offers_en_clusters.csv')
# reading content from Json file
with io.open('./test4.json', mode="r", encoding="utf-8") as file:
    print("start to read offers")
    content = file.read()
file.close()
print("already read offers")
js_parsed = js.loads(content)
#print(js_parsed)
# first we should write this data into csv file
# for this we need to create a csv object
wanted_keys = ['url', 'cluster_id']
with open('./jsonData4.csv', 'wt',  newline='', encoding='utf-8') as f:
    print("created empty csv")
    dict_writer = csv.DictWriter(f, fieldnames=wanted_keys)
    dict_writer.writeheader()  # writing header in the csv file
    for row in js_parsed:
        # url cleaning
        for s in ['.html', 'http://', 'https://', 'www.']:
            row['url'] = row['url'].replace(s,'')
        # create a dict d that contains all the required keys since parameter to writerow must be a dict
        d = {x:row[x] for x in wanted_keys}
        dict_writer.writerow(d)
print("already write to first csv")
# we are able to write data from json to csv file
# however this data contains unwanted blank rows, to remove them :

#with open('C:\\Users\\DELL\\Desktop\\blankremoved.csv', 'wt') as output, open('C:\\Users\\DELL\\Desktop\\jsonData.csv') as f:
    # check for each row in the csv file if it is blank or not
   # non_blank = (line for line in f if line.strip())
    # write all nonblank lines into the csv
  #  output.writelines(non_blank)
#print("blankremoved")
# now we have 2 csv files which we can merge using pandas pachkage
# creating new data frame for the new csv file

new_df = pd.read_csv('./jsonData4.csv')
print("already read written csv 1")
merged = df.merge(new_df, on="cluster_id")  # merge the file on common attribute cluster_id
print("merged csv and offers")
# writing merged file into the csv file
merged.to_csv('./categories+offers_english_1.csv', index=False)
# reading from the csv file into a dataframe