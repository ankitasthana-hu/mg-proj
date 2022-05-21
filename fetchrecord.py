import re
import sys
import requests
import csv
import json

url = "https://reqres.in/api/users?page=2"

def test_APIconnectivity():
      url = "https://reqres.in/api/users?page=2"
      headers = {
       'Accept': 'application/json',
       'Content-Type': 'application/json'
       }
      response = requests.request("GET",url,headers=headers,data={})
      #return print("Response received : ", response.status_code , "If 200, then API connectivity established") 
      return print(response.status_code)

def test_dryrun_fetchdata():
#API URL
   url = "https://reqres.in/api/users?page=2"
   headers = {
     'Accept': 'application/json',
      'Content-Type': 'application/json'
   }
   response = requests.request("GET",url,headers=headers,data={})
   json_out = response.json()
   ourdata = []
   csvheader = ['ID','EMAIL','FIRST_NAME','LAST_NAME','AVATAR']


   for x in json_out['data']:
         listing = [x['id'],x['email'],x['first_name'],x['last_name'],x['avatar']]
         ourdata.append(listing)
   return print(ourdata)

def test_alluserdata():
#API URL
   url = "https://reqres.in/api/users?page=2"
   headers = {
     'Accept': 'application/json',
      'Content-Type': 'application/json'
   }
   response = requests.request("GET",url,headers=headers,data={})
   json_out = response.json()
   ourdata = []
   csvheader = ['ID','EMAIL','FIRST_NAME','LAST_NAME','AVATAR']


   for x in json_out['data']:
         listing = [x['id'],x['email'],x['first_name'],x['last_name'],x['avatar']]
         ourdata.append(listing)

   with open('out_allusers.csv','w',encoding='UTF8',newline='') as f:
         writer = csv.writer(f)
         writer.writerow(csvheader)
         writer.writerows(ourdata)

   print('done')


def test_singleuserdata():
#API URL
   print("https://reqres.in/api/users/"+ user_id)
   headers = {
       'Accept': 'application/json',
       'Content-Type': 'application/json'
   }

   response = requests.request("GET","https://reqres.in/api/users/"+ user_id,headers=headers,data={})

   json_out = response.json()
   ourdata = []
   csvheader = ['ID','EMAIL','FIRST_NAME','LAST_NAME','AVATAR']
   for key,value in json_out['data'].items():
         listing = value
         ourdata.append(listing)

   with open('out_singleuser.csv','w',encoding='UTF8',newline='') as f:
         writer = csv.writer(f)
         writer.writerow(csvheader)
         writer.writerow(ourdata)

   print('done')


if __name__ == '__main__':
    test_APIconnectivity()
    test_dryrun_fetchdata()
    operation = input("Select Operation : All_Data, Single_User")
    print("User selected operation: ", operation)
    if operation == "Single_User":
       user_id = input("Enter User_ID")
       print("User selected user_id: ",user_id)
    if operation == "All_Data": 
            test_alluserdata()   
    if operation == "Single_User":
       try:     
           test_singleuserdata()
       except Exception as e:
           print("Enter User ID is Unknown. Please select valid ID")
