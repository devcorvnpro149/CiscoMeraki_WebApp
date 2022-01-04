import sys
import pandas as pd
import csv
import json
import meraki_get

# ----- OUTPUT IS LIST TYPE ------
# with open('data.json', 'w') as outfile:
#     outfile.write(meraki_get.GET_OG())
# print (type(outfile))

# ----- OUTPUT IS STRING TYPE ------ 
# with open('data.json', 'w') as outfile:
#     json.dump(meraki_get.GET_OG(), outfile)
# print (type(outfile))

# ----- READ FILE WITH PANDAS ------ 
# data = pd.read_json('data.json')
# df = data.to_csv()


# with open('data.csv', 'w') as outfile:
#     outfile.write()

# infile = open('sample.json')
# data = json.load(infile)
# print (type(data))

def data_build_pie():
    c = csv.writer(open('data_build_pie.csv', 'w'), lineterminator = '\n')
    c.writerow(['OG_id','Name','Area','Health','State','Num Devices'])
    infile = open('data_build_pie.json')
    data = json.load(infile)
    for i in data:
        c.writerow([i['organizationId'], i['name'], i['area'], i['health'], i['state'], i['num_dv']])

    print ('Write data to csv file successfully!!!')

def data_build_bar():
    with open('data_build_bar.csv', 'w', newline ='') as outfile:
        fieldnames = ['OG_id', 'ProductType', 'Number of supported NWs']
        c = csv.DictWriter(outfile, fieldnames=fieldnames)
        c.writeheader()

        print ('---Please supply info to check NW product in particular OG---')
        number_og = int(input('Please enter number of OGs you want to take NW_data from: '))
        for i in range(number_og):
            nw = json.loads(meraki_get.GET_NW_IN_OG())
            n_sw = n_wl = n_ss = n_cm = n_sm = n_ap = n_cg = 0
            for i in nw:
                for j in i["productTypes"]:
                    if j == "switch": 
                        n_sw+=1
                    if j == "wireless":
                        n_wl+=1
                    if j == "sensor":
                        n_ss+=1
                    if j == "camera":
                        n_cm+=1
                    if j == "appliance":
                        n_ap+=1
                    if j == "systemsManager":
                        n_sm+=1
                    if j == "cellularGateway":
                        n_cg+=1
            c.writerow({'OG_id' : i['organizationId'], 'ProductType' : 'SWITCH', 'Number of supported NWs' : n_sw})
            c.writerow({'OG_id' : i['organizationId'], 'ProductType' : 'WIRELESS', 'Number of supported NWs' : n_wl})
            c.writerow({'OG_id' : i['organizationId'], 'ProductType' : 'SENSOR', 'Number of supported NWs' : n_ss})
            c.writerow({'OG_id' : i['organizationId'], 'ProductType' : 'CAMERA', 'Number of supported NWs' : n_cm})
            c.writerow({'OG_id' : i['organizationId'], 'ProductType' : 'APPLIANCE', 'Number of supported NWs' : n_ap})
            c.writerow({'OG_id' : i['organizationId'], 'ProductType' : 'SYSMANAGER', 'Number of supported NWs' : n_sm})
            c.writerow({'OG_id' : i['organizationId'], 'ProductType' : 'CELLGATE', 'Number of supported NWs' : n_cg})

    print ('Write data to csv file successfully!!!')

def data_build_scatter_geo():
    c = csv.writer(open('data_build_scatter_geo.csv', 'w'), lineterminator = '\n')
    c.writerow(['id','organizationId','name','productTypes','location','timeZone'])
    infile = open('data_build_scatter_geo.json')
    data = json.load(infile)
    for i in data:
        c.writerow([i['id'], i['organizationId'], i['name'], i['productTypes'], i['location'], i['timeZone']])

    print ('Write data to csv file successfully!!!')

def data_build_map_density():
    c = csv.writer(open('data_build_map_density.csv', 'w'), lineterminator = '\n')
    c.writerow(['organizationId','name','productTypes','latitude','longitude','timeZone','num_devices'])
    infile = open('data_build_map_density.json')
    data = json.load(infile)
    for i in data:
        c.writerow([i['organizationId'], i['name'], i['productTypes'],i['latitude'], i['longitude'], i['timeZone'], i['num_devices']])

    print ('Write data to csv file successfully!!!')


def main():
    result = data_build_map_density()
    print(result)


if __name__ == "__main__":
    sys.exit(main())




