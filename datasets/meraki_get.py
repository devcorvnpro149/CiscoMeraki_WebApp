import json
import sys
import pgpd


def GET_OG():
    resp = pgpd.get(api = "/organizations")
    og_list = json.dumps(resp.json(), indent=4)
    return og_list
   
def GET_OG_ID():
    og_list = json.loads(GET_OG())
    name = input("Your organization name you want to get info / access to: ")
    for og in og_list:
        if og["name"] == name:
            og_id = og["id"]
    return og_id

def GET_NW_IN_OG():
    og_id = GET_OG_ID()
    resp = pgpd.get(api = "/organizations/{}/networks".format(og_id))
    nw_list = json.dumps(resp.json(), indent=4)
    return nw_list

def GET_NW_ID():
    nw_list = json.loads(GET_NW_IN_OG())
    name = input("Your network name you want to get info / access to: ")
    for nw in nw_list:
        if nw["name"] == name:
            nw_id = nw["id"]
    return nw_id

def GET_DV_IN_NW():
    nw_id = GET_NW_ID()
    resp = pgpd.get(api = "/networks/{}/devices".format(nw_id))
    dv_list = json.dumps(resp.json(), indent=4)
    return dv_list

def POST_OG():
    name = input("Your new organization name: ")
    params = {"name": name}
    resp = pgpd.post(api = "/organizations", params=params)
    resp = json.dumps(resp.json(), indent=4)
    return resp

def POST_NW():
    og_id = GET_OG_ID()
    name = input ("Your new network name: ")
    params={
        "name": name,
        "timeZone":"GMT",
        "tags":["test2"],
        "productTypes":["switch"]
    }
    resp = pgpd.post(api = "/organizations/{}/networks".format(og_id), params=params)
    resp = json.dumps(resp.json(), indent=4)
    return resp

# def POST_DV():
#     nw_id = GET_NW_ID()
#     name = input ("Your new device name: ")
#     params = {
#         "name": name,
#         "mac": "ac:17:c8:24:4f:68",
#         "serial" : "Q2SW-SWQ2-HZ9L",
#         "lat": 37.4180951010362,
#         "lng": -122.098531723022,
#         "address": "",
#         "wan1Ip": "192.168.1.74",
#         "wan2Ip": "null",
#         "model": "MX250",
#         "firmware": "wired-15-44",
#         "tags": ["recently-added"]
#         }
#     resp = pgpd.post(api = "/networks/{}/devices".format(nw_id), params=params)
#     return resp

def DEL_OG():
    og_id = GET_OG_ID()
    resp = pgpd.delete(api = "/organizations/{}".format(og_id))
    return resp

def DEL_NW():
    nw_id = GET_NW_ID()
    resp = pgpd.delete(api = "/networks/{}".format(nw_id))
    return resp

def menu():
    print('''
1.Show list of organizations
2.Show list of networks in organization
3.Show list of devices in network
4.Exit''')
    try:
        answer = int(input('> '))
        if answer == 1:
            result = GET_OG()
            print (result)
            menu()
        elif answer == 2:
            result = GET_NW_IN_OG()
            print (result)
            menu()
        elif answer == 3:
            result = GET_DV_IN_NW()
            print (result)
            menu()    
        elif answer == 4:
            print ('Goodbye!')
            exit()   
        else:
            print ('Please enter number from 1-->4 only') 
            menu()
    except ValueError:
        print ('Please enter a number!')
#         menu()

def main():
    result = menu()
    print(result)


if __name__ == "__main__":
    sys.exit(main())