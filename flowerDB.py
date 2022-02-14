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



def addFullOrd():
      mydict = {
      #1
      "orderItems" : [ {
      "amount" : 1,
            "id" : "Tears of Falka",
            "name" : "White roses",
            "price" : 3.5
      }, {
            "amount" : 1,
            "id" : "-MiYEWhO5qzS_hndN60b",
            "name" : "Aquilégia bush",
            "price" : 10.5
      } ],
      "user" : {
            "city" : "Київ",
            "email" : "allons.y.ka@gmail.com",
            "name" : "Abramov Kirill",
            "postal_code" : "02149",
            "street" : "ELlvesForest 21a"
            },
      #2
      "orderItems" : [ {
            "amount" : 1,
            "id" : "-Mir-fwGo-IcTn3oTOEo",
            "name" : "Bouquet of tulips",
            "price" : 7.5
      }, {
            "amount" : 2,
            "id" : "-Mir-fwGo-IcTnghhfhfghf",
            "name" : "Amaryllis Charisma",
            "price" : 5.5
      } ],
      "user" : {
            "city" : "Київ",
            "email" : "allons.y.ka@gmail.com",
            "name" : "Abramov Kirill",
            "postal_code" : "02149",
            "street" : "ELlvesForest 21a"
            },
      #3
      "orderItems" : [ {
            "amount" : 1,
            "id" : "-Mir-pkopklp",
            "name" : "Celosia",
            "price" : 8.5
      }, {
            "amount" : 1,
            "id" : "-MiYEWhO5qzS_hndN60b",
            "name" : "Aquilégia bush",
            "price" : 10.5
      } ],
      "user" : {
            "city" : "Київ",
            "email" : "allons.y.ka@gmail.com",
            "name" : "Abramov Kirill",
            "postal_code" : "02149",
            "street" : "ELlvesForest 21a"
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

def get_orders():
	arr = []
	for value in coll.find():
		arr.append(value)
		print(value)
	return arr


def addFullProd():
      data = [{
            "description" : "Tears of Falka",
            "eng_name" : "White roses",
            "id" : "f1",
            "img" : "https://img.wattpad.com/00e19c8a514a636eb00cdbd58534846ff72b8068/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f454b434b347570735768354a4d513d3d2d323530372e313635663762313731656135313130633939323335343530383733372e6a7067",
            "location" : "elven forest",
      "name" : "elven flower field",
      "price" : 3.5,
      "weight" : 50},{
      "description" : "Aquilegia is one of the most unpretentious ornamental plants for decorating the site. Despite the seeming rusticity, it has an exquisite charm that is not evident at first sight. But if you look closely, the structure and shape of its flowers are truly unique.",
      "eng_name" : "Aquilégia bush",
      "id" : "f2",
      "img" : "https://rastenievod.com/wp-content/uploads/2017/06/24-3.jpg",
      "location" : "elven forest",
      "name" : "elven flower field",
      "price" : 10.5,
      "weight" : 25},{
      "description" : "Tulips are in general the symbol of perfect love, but every color also has its symbolism.",
      "eng_name" : "Bouquet of tulips",
      "id" : "f3",
      "img" : "https://na-dache.pro/uploads/posts/2021-05/1620300655_22-p-tyulpani-v-ogorode-foto-25.jpg",
      "location" : "elven forest",
      "name" : "elven flower field",
      "price" : 7.5,
      "weight" : 25},{
      "description" : "This flower symbolizes pride and beauty. The perfect flower to show affection for example at a graduation ceremony or to thank someone. If you are giving an Amaryllis, you are always giving a significant gesture.",
      "eng_name" : "Amaryllis Charisma",
      "id" : "f4",
      "img" : "https://www.holex.com/wp-content/uploads/2017/12/amaryllis-2-768x768.jpg",
      "location" : "elven forest",
      "name" : "elven flower field",
      "price" : 5.5,
      "weight" : 20},{
      "description" : "Uncomplicated addiction is the general symbolism of this cut flower.",
      "eng_name" : "Celosia",
      "id" : "f5",
      "img" : "https://www.holex.com/wp-content/uploads/2018/03/celosia-2-768x768.jpg",
      "location" : "elven forest",
      "name" : "elven flower field",
      "price" : 8.5,
      "weight" : 90}]
      x = coll2.insert_many(data)
      return "ok"

# # добавить: удаление всех док из колекции
# addFullProd()
# get_products()
