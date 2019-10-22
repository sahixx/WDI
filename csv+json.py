# import pandas package to read n merger csv files
import pandas as pd
# import pachkage json for parsing json files
import json as js
# import csv package for reading from and writting into csv file
import csv as csv

# reading from the csv file into a dataframe
df = pd.read_csv('C:\\Users\\DELL\\Desktop\\categories_offers_en_clusters_sample.csv')
# reading content from Json file
with open('C:\\Users\\DELL\\Desktop\\sample_offersenglish.json', 'r') as file:
    content = file.read()
file.close()
js_parsed = js.loads(content)
print(type(js_parsed))
# first we should write this data into csv file
# for this we need to create a csv object
with open('C:\\Users\\DELL\\Desktop\\jsonData.csv', 'wt') as f:
    dict_writer = csv.DictWriter(f, fieldnames=['url', 'nodeID', 'cluster_id', 'identifiers','schema.org_description', 'parent_schema.org_description', 'parent_NodeID', 'relationToParent'])
    dict_writer.writeheader()  # writing header in the csv file
    for row in js_parsed:
        dict_writer.writerow(row)

# we are able to write data from json to csv file
# however this data contains unwanted blank rows, to remove them :

with open('C:\\Users\\DELL\\Desktop\\blankremoved.csv', 'wt') as output, open('C:\\Users\\DELL\\Desktop\\jsonData.csv') as f:
    # check for each row in the csv file if it is blank or not
    non_blank = (line for line in f if line.strip())
    # write all nonblank lines into the csv
    output.writelines(non_blank)

# now we have 2 csv files which we can merge using pandas pachkage
# creating new data frame for the new csv file

new_df = pd.read_csv('C:\\Users\\DELL\\Desktop\\blankremoved.csv')
merged = df.merge(new_df, on="cluster_id")  # merge the file on common attribute a

# writing merged file into the csv file
merged.to_csv('C:\\Users\\DELL\\Desktop\\new.csv', index=False)
