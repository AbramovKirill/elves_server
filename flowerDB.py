import pymongo
from itertools import count
import datetime

client = pymongo.MongoClient("mongodb+srv://12345:12345@cluster0.htukn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.FlowersDB
coll = db.orders
coll2 = db.products



def add_new_order():
      mydict = {
      "orderItems" : [ {
            "amount" : 1,
            "id" : "-MiYEZuzULM-wg0KuKPw",
            "name" : "Natural Jasmine Green Tea",
            "price" : 3.5
      }, {
            "amount" : 1,
            "id" : "-MiYEWhO5qzS_hndN60b",
            "name" : "Phoenix Honey Orchid",
            "price" : 10.5
      } ],
      "user" : {
            "city" : "Київ",
            "email" : "maab2198@gmail.com",
            "name" : "Марія Вікторівна Абрамова",
            "postal_code" : "02149",
            "street" : "Бажана 26"
            }
      }
      x = coll.insert_one(mydict)
      return x.inserted_id

def get_products():
	arr = []
	for value in coll2.find():
		arr.append(value)
		print(value)
	return arr