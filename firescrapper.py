from bs4 import BeautifulSoup
import requests
import pyrebase
 
from bs4 import BeautifulSoup
import pyrebase
config = {"apiKey": "AIzaSyCPe6rb_bS-etgYhmf5O7aa_UOtemV1FIU",
  "authDomain": "tinkerhubtest.firebaseapp.com",
  "databaseURL": "https://tinkerhubtest-default-rtdb.firebaseio.com",
  "projectId": "tinkerhubtest",
  "storageBucket": "tinkerhubtest.appspot.com",
  "messagingSenderId": "436160506738",
  "appId": "1:436160506738:web:4e1a5889d3f259da224beb",
  "measurementId": "G-JC47ZLD39V"}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

choice = input("enter the topic you want to scrap: \n")
response = requests.get(
	url=f"https://en.wikipedia.org/wiki/{choice}",
)
soup = BeautifulSoup(response.content, 'html.parser')
ans = []
title = soup.find(id="firstHeading")
for data in soup.find_all("p"):
    ans.append(data.get_text())
print(title.string)
# the index of two is used because sometimes a newline or heading would come before that
print(ans[2])

data = {title.string:ans[2]}
db.push(data)
print("updated the database")

