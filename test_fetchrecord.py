import unittest
import requests
import csv
import json
import fetchrecord
from fetchrecord import test_APIconnectivity
from fetchrecord import test_dryrun_fetchdata

url = "https://reqres.in/api/users?page=2"
headers = {
         'Accept': 'application/json',
         'Content-Type': 'application/json'
}
 
def test_APIcall():

      response = requests.request("GET",url,headers=headers,data={})
      json_out = response.json()
      assert response.status_code == 200
      print("API endpoint connectivity is successful")

def test_nodata_check():

      response = requests.request("GET",url,headers=headers,data={})
      json_out = response.json()
      #print(json_out)
      assert (len(json_out)) >= 1

def test_comparedata_validity():

      response = requests.request("GET",url,headers=headers,data={})
      json_out = response.json()
      ourdata = []
      for x in json_out['data']:
            listing = [x['id'],x['email'],x['first_name'],x['last_name'],x['avatar']]
            ourdata.append(listing)

      for i in ourdata[0]:
            assert i == 7
            print("Data Found !!")
            break
