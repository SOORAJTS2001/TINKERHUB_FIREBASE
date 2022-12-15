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

# #this is to set data
data = {"name":"sam","age":10,"list":[1,2,3]}
#this pushes with random key
db.push(data)
# this pushes with the key as tkmce
db.child("tkmce").set(data)
print("setted the data")


# #this is to update data
data = {'tkmce/':{"name":"bob","age":25,"list":[8,9,0]}}
db.update(data)
print("updated the data")

# this is to retreive data from the firebase
data = db.child("tkmce").get()
# data.val gives ordered dict so convert it into normal dictionary
datavalue = dict(data.val())
print(datavalue)

# this is to remove data
db.child('tkmce').remove()

