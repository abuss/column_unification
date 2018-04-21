
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
    data = odlib.resource_metadata(id)
    dataset['id'] = id
    dataset['name'] = data['name']
    dataset['description'] = data['description'] if 'description' in data else ''
    dataset['category'] = data['category'] if 'category' in data else ''
    dataset['tags'] = data['tags'] if 'tags' in data else ''
    cust_fields = {}
    if 'custom_fields' in data['metadata']:
        if 'General Information' in data['metadata']['custom_fields']:
            cust_fields = data['metadata']['custom_fields']['General Information']
    dataset['purpose'] = cust_fields['Purpose'] if 'Purpose' in cust_fields  else ''
    fields = []
    for c in data['columns']:
        field = {}
        cname = c['name'].lower()
        desc = c.setdefault('description','')
        fields.append({'name':cname,'description':desc,'type':c['dataTypeName']})
    dataset['columns'] = fields
    metadata.append(dataset)

with open("od_edm_dataset_metadata.json","w") as f:
    f.write(json.dumps(metadata,indent=2))

