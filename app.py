from flask import Flask
import flowerDB as flower
import json
from bson import json_util
from flask import jsonify
from flask import request

from flask_cors import CORS, cross_origin


from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys


app = Flask(__name__ 
    ,static_folder='elves/build',static_url_path='')
CORS(app)



@app.route('/get_products')
@cross_origin()
def get_products():
    responce = flower.get_products()
    noObjectID = json.loads(json_util.dumps(responce))
    return jsonify(noObjectID)

@app.route('/get_orders')
@cross_origin()
def get_orders():
    responce = flower.get_orders()
    return jsonify(responce)

@app.route('/create_order',methods=['POST'])
@cross_origin()
def create_order():
    request_data = request.json
    # mydict = {
    #   "orderItems" : [ {
    #         "amount" : 1,
    #         "id" : "-MiYEZuzULM-wg0KuKPw",
    #         "name" : "Natural Jasmine Green Tea",
    #         "price" : 3.5
    #   }, {
    #         "amount" : 1,
    #         "id" : "-MiYEWhO5qzS_hndN60b",
    #         "name" : "Phoenix Honey Orchid",
    #         "price" : 10.5
    #   } ],
    #   "user" : {
    #         "city" : "Київ",
    #         "email" : "maab2198@gmail.com",
    #         "name" : "Марія Вікторівна Абрамова",
    #         "postal_code" : "02149",
    #         "street" : "Бажана 26"
    #         }
    # }
    print(request_data)
    #noObjectID = json.loads(json_util.dumps(request_data))
    responce = flower.add_new_order(request_data)
    return str("ok")

@app.route('/create_product')
@cross_origin()
def create_product():
    responce = flower.addFullProd()
    return str(responce)
    
@app.route('/addFullOrd')
@cross_origin()
def addFullOrd():
    responce = flower.addFullOrd()
    return str(responce)









@app.route('/hello') # Routes you to the page with http://127.0.0.1:5000/hello/
def hello():
    return 'Hello, World'

@app.route('/projects/') # URL with trailing slash
def projects():
    return 'The project page'

@app.route('/about') 
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(host='0.0.0.0')



