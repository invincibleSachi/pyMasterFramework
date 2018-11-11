import requests
import json

def doGet(url,data=None,headers=None):
    if data is None:
        r=requests.get(url=url,headers=headers)
    else:
        r=requests.get(url=url,data=data,headers=headers)
    return r

def doPostUrlWithJSON(url,payload,headers=None):
    r = requests.post(url=url, data=json.dumps(payload),headers=headers)
    return r

def doPostUrlWithJSON(url, file,headers):
    fileObj={'file': open(file, 'rb')}
    r = requests.post(url=url, file=fileObj,headers=headers)
    return r
