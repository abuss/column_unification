# Library to read data from socrata (data.edmonton.ca)
import requests

def get_catalog(q=None,tags=None,limit=None):
    "Search in the catalog for the given query or returns all datasets entries"
    query = "http://api.us.socrata.com/api/catalog/v1"
    param = {'domains':"data.edmonton.ca",
             'offset':"0",
             'only':"datasets",
             # 'limit': "10",
    }
    if q:
        param['q']=q
    if tags!=None:
        param['domain_tags']=tags
    if limit!=None:
        param['limit']=limit
    resp = requests.get(query,params=param)
    print(resp.url)
    if resp.status_code == requests.codes.ok:
        print(resp,resp.json().keys(),len(resp.json()["results"]))
        data = resp.json()['results']
        return data
    return None


def resource_data_json(resource_id,domain='data.edmonton.ca'):
    "Returns the data associated to the given resource id"
    url = "https://{}/resource/{}.json".format(domain,resource_id)
    print(url)
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:
        data = resp.json()
        return data
    return None

def resource_data_csv(resource_id,domain='data.edmonton.ca'):
    "Returns the data associated to the given resource id"
    url = "https://{}/resource/{}.csv".format(domain,resource_id)
    print(url)
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:
        data = resp.content
        return data
    return None


def resource_metadata(resource_id,domain='data.edmonton.ca'):
    "Returns the information about the given resource id"
    url = "https://{}/api/views/{}.json".format(domain,resource_id)
    resp = requests.get(url)
    print(resp.url)
    if resp.status_code == requests.codes.ok:
        data = resp.json()
        return data
    return None
