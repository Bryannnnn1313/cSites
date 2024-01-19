from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import os
import time
import pandas as pd
import requests
import json

'''
url = 'https://www.recreation.gov/api/camps/availability/campground/10054578/month?start_date=2024-06-01T00%3A00%3A00.000Z'

response = requests.get(url)
page = response.text
soup = BeautifulSoup(page,"lxml")
print(soup.prettify())
'''

# get list of camp sites I want 
def getSites():
    headers = {
            'accept': 'application/json',
            'apikey': 'c4692194-3be6-49a1-862b-5055c35ebfe8',
            }

    params = {
            'limit': '50',
            'offset': '0',
            'state': 'CA',
            'latitude': '37.865101',
            'longitude': '-119.538330',
            'radius': '20.0',
            'lastupdated': '10-01-2018',
            }
    
    #struct for response
    #dict - list - dict
    response = requests.get('https://ridb.recreation.gov/api/v1/facilities', params=params, headers=headers)
    x = response.json()
    return x




#get list of available dates
def getDates(campID, fMonth): 
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Alt-Used': 'www.recreation.gov',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
            }
    params = {
            'start_date': f'2024-{fMonth:02}-01T00:00:00.000Z',
            }

    response = requests.get(
            f'https://www.recreation.gov/api/camps/availability/campground/{campID}/month',
            params=params,
            headers=headers,
            )
    print(response<LeftMouse>)
    if response == 200:
        x = response.json()
    return x

def facIdList(locations):
    ids = []
    for i in range(0, int(locations['METADATA']['RESULTS']['CURRENT_COUNT'])):
        if locations['RECDATA'][i]['FacilityTypeDescription'] == 'Campground':
            ids.append(locations['RECDATA'][i]['FacilityID'])
    return ids

#create a list 
def fullDataSet():
    locations = getSites()
    facId = facIdList(locations)
    curr_month = '{:02d}'.format(datetime.now().month)
    data = []
    for id in facId:
        for nMonth in range(0,6):
            print(id)
            print(curr_month)
            data.append(getDates(id, int(curr_month) + nMonth))

fullDataSet()
