# coding: utf-8

import opendatalib as odlib
import pprint
import json

# dtraw = odlib.get_catalog(q='neighbourhood',limit=30)
dtraw = odlib.get_catalog(limit=1000)

i = 1
metadata = []
for reg in dtraw:
    print(i,end=' ')
    i+=1
    dataset = {}
    id = reg['resource']['id']
    data = odlib.resource_data_csv(id)
    with open("datasets/{}.csv".format(id),"wb") as f:
        f.write(data)

