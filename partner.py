import requests
import json


BASE_URL='http://paulsoumen76.pythonanywhere.com/'
ENDPOINT='api/'
LISTENDPOINT='list-api/'
print("""for retrive all data press 1
         for get only one data press 2
         for post data press 3
         for update data press 4
         for delete data press 5""")

i=int(input("enter any number: "))
if i==1:
    def get_alluser():
          resp=requests.get(BASE_URL+LISTENDPOINT)
          print(resp.status_code)
          print(resp.json())
    get_alluser()
if i==2:
    try:
        def get_user(user_id):
            id={
             'user_id':user_id
            }

            resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(id))
            print(resp.status_code)
            print(resp.json())
        user_id=input("enter an valid user_id: ")
        get_user(user_id)
    except:
        print("user_id is already asigned to someone else")

if i==3:
    def create_user():
        data={
        "user_id": "W025A3CEE",
        "real_name": "Koushik konar",
        "tz": "ASIA/Bangalore",
        "activity_periods": [{"start_time": "Feb 1 2020  1:33PM","end_time": "Feb 1 2020 1:54PM"},{"start_time": "Mar 1 2020  11:11AM","end_time": "Mar 1 2020 2:00PM"},{"start_time": "Mar 16 2020  5:33PM","end_time": "Mar 16 2020 8:02PM"}]
        }

        d = data['activity_periods']
        str = json.dumps(d)
        data['activity_periods'] = str
        resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(data))
        print(resp.status_code)
        print(resp.json())
    create_user()
if i==4:
    try:
        def update_user(user_id):
              data={
              "user_id": user_id,
              "real_name": "Egon Spengler",
              "tz": "Asia/Kolkata"
              }
              resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(data))
              print(resp.status_code)
              print(resp.json())
        user_id=input('please enter a valid user_id: ')
        update_user(user_id)
    except:
        print('user_id is already asigned to someone else')
if i==5:
    try:
        def delete_user(user_id):
             id={
              'user_id':user_id
             }

             resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(id))
             print(resp.status_code)
             print(resp.json())
        user_id=input("enter an valid user_id: ")
        delete_user(user_id)
    except:
        print('user_id is already asigned to someone else')    









#  #dont provide user_id if you want to view all users
#
# def get_alluser():
#     resp=requests.get(BASE_URL+LISTENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
# get_alluser()
#
# def update_user(user_id):
#       data={
#       "user_id": user_id,
#       "real_name": "Egon Spengler",
#       "tz": "Asia/Kolkata"
#       }
#
#
#       resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(data))
#       print(resp.status_code)
#       print(resp.json())
# user_id=input('please enter a valid user_id: ')
# update_user(user_id)
