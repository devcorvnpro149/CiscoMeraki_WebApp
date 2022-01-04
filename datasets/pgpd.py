import requests
import json
import sys
import meraki_info

def get(base_url = meraki_info.base_url, api = '', params = ''):
    headers = {
            "X-Cisco-Meraki-API-Key": meraki_info.api_key,
            "Content-Type": "application/json"
        }
    url = base_url + api 
    print ("\nExecuting GET '%s'\n" %url)
    try:
        resp = requests.get(url,headers=headers,params=params)
        print ("Get '%s' Status" %api, resp.status_code, '\n')
        return (resp)
    except:
        print ("Something went wrong with GET", api)
        sys.exit()

def post(base_url = meraki_info.base_url, api = '', params = ''):
    headers = {
            "X-Cisco-Meraki-API-Key": meraki_info.api_key,
            "Content-Type": "application/json"
        }
    url = base_url + api 
    print ("\nExcuting POST '%s' \n"%url)
    try:
        resp = requests.post(url,json.dumps(params),headers=headers)
        print ("POST '%s' Status: "%api, resp.status_code, '\n')
        return (resp)
    except:
        print ("Something went wrong with POST", api)
        sys.exit()

def put(base_url = meraki_info.base_url,api = '', params = ''):
    headers = {
            "X-Cisco-Meraki-API-Key": meraki_info.api_key,
            "Content-Type": "application/json"
    }
    url = base_url + api
    print ("\nExcuting PUT '%s'\n"%url)
    try:
        resp = requests.put(url,headers=headers,params=params,verify=False)
        print ("PUT '%s' Status:" %api, resp.status_code, '\n')
        return (resp)
    except:
        print ("Something went wrong with PUT", api)
        sys.exit()

def delete(base_url = meraki_info.base_url, api = '', params = ''):
    headers = {
            "X-Cisco-Meraki-API-Key": meraki_info.api_key,
            "Content-Type": "application/json"
        }
    url = base_url + api
    print ("\nExcuting DEL '%s' \n"%url)
    try:
        resp = requests.delete(url,headers=headers,params=params, verify=False)
        print ("DEL '%s' Status: "%api, resp.status_code, '\n')
        return (resp)
    except:
        print ("Something went wrong with DEL", api)
        sys.exit()