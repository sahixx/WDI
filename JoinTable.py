import json
import pandas as pd
from tqdm import tqdm


with open('sample_specTables.json', 'r',  encoding='utf-8')as f:
    specTable = []
    for row in f.readlines():
        dict1 = json.loads(row)
        specTable.append(dict1)
    for a in specTable:
        urls = a['url'].replace('.html', '')
        urls = urls.replace('http://www.', 'www.')

with open('sample_offersenglish.json', 'r', encoding='utf-8')as f:
    offerEnglish = []
    for line in f.readlines():
        dict2 = json.loads(line)
        offerEnglish.append(dict2)
        print(dict2)
    ids = [int(b['cluster_id']) for b in offerEnglish]
    print(ids)


url = 'https://tweakers.net/pricewatch/331960/g-technology-g-drive-mobile-usb-30-5400rpm-1tb-zilver.html'
putDicts = {}
join_Array = []
connect_file = pd.read_csv('categories.csv', encoding='utf-8')

# loop through all cluster_ids in categories csv
for i in tqdm(range(len(connect_file.cluster_id))):   
# for i in tqdm(range(1)):

    # turn the i-th row of the category csv into a list with the format [categoryName, clusterId]
    convertToList = list(connect_file.iloc[i, ])

    category_name = convertToList[0]
    cluster_id = convertToList[1]

    # append (category_name, {}) to putDicts
    putDicts.setdefault(category_name, {})

    putDicts[category_name].setdefault(cluster_id, (0, 0))
    
    if cluster_id in ids:

        # find first match of cluster_id in offerEnglish
        offerEnglish = offerEnglish[ids.index(cluster_id)]

        # process url strings
        url = offerEnglish['url'].replace('.html', '')
        url = url.replace('http://www.', 'www.')

        # matching the above url (which comes from offers) against all urls in specTable 
        if url in urls:
            specTable = specTable[urls.index(url)]
            num_key_value_pair = len(specTable['keyValuePairs'])
            print('The number of k_v pair is :' + str(num_key_value_pair))

        else:
            num_key_value_pair = 0
            print('The number of k_v pair is : ' + str(num_key_value_pair))

        join_Array.append([category_name, cluster_id, 0, num_key_value_pair])
        putDicts[category_name, cluster_id] = (1, num_key_value_pair)
    else:
        # case when cluster_id (from the csv) does not exist in offersenglish
        # (basically means that no offers belong to this cluster)
        join_Array.append([category_name, cluster_id, 0, 0])
        putDicts[category_name, cluster_id] = (0, 0)


df = pd.DataFrame(join_Array)
df.columns = ['category', 'subcategory', 'hasSpecTable', 'num_k_v']
print(df)


