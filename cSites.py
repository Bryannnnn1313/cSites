#!/usr/bin/python3
import requests
import json
#get total campgrounds
'''
headers = {
        'accept': 'application/json',
        'apikey': 'c4692194-3be6-49a1-862b-5055c35ebfe8',
        }

params = {
        'limit': '50',
        'offset': '0',
        }

response = requests.get('https://ridb.recreation.gov/api/v1/campsites', params=params, headers=headers)
'''

import requests

headers = {
        'accept': 'application/json',
        'apikey': 'c4692194-3be6-49a1-862b-5055c35ebfe8',
        }

params = {
        'query': 'Valley',
        'limit': '50',
        'offset': '0',
        'state': 'CA',
        'latitude': '37.7408333',
        'longitude': '-119.5666667',
        'radius': '25',
        'sort': '"Name"',
        }

response = requests.get('https://ridb.recreation.gov/api/v1/facilities', params=params, headers=headers)

data = response.json()
facList = []

for facs in data['RECDATA']:
    facList.append(facs.get('FacilityName'))


headers = {
        'accept': 'application/json',
        'apikey': 'c4692194-3be6-49a1-862b-5055c35ebfe8',
        }


params = {
        'limit': '50',
        'offset': '0',
        }

response = requests.get('https://ridb.recreation.gov/api/v1/facilities/232450/campsites', params=params, headers=headers)

data = response.json()
with open('dat.json', 'w') as file:
    json.dump(data,file,indent=2)
for campsite in data['RECDATA']:
    campsite_number = campsite.get('CampsiteName')
    print(f"Facility Name: {facList[0]}, Campsite Name: {campsite_number}")
    #get total campsites for campground 
    #check if open 
    # get location 
    #post link
