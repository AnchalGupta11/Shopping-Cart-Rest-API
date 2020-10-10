from flask import Flask , make_response, request, jsonify
from flask_mongoengine import MongoEngine
from api_constants import mongo_passwords


app = Flask(__name__)

database_name="API"
DB_URL="mongodb+srv://dbadmin:{}@cluster0.l40iw.mongodb.net/{}?retryWrites=true&w=majority".format(mongo_passwords,database_name)

app.config["MONGODB_HOST"] = DB_URL

db = MongoEngine()
db.init_app(app)

'''
Sample Request Body
{
    "item_id":1,
    "name":"Football",
    "seller":"Gopal Sports Store",
    "price":100
}
'''
class Item(db.Document):

    item_id = db.IntField()
    name = db.StringField()
    seller = db.StringField()
    price = db.IntField()

    def to_jason(self):
        #converts this document to JSON
        return{
            "item_id":self.item_id,
            "name" :self.name,
            "seller" : self.seller,
            "price" :self.price

        }



@app.route('/api/db_populate',methods=['POST'])
def db_populate():
    item1 = Item(item_id=1,name="Football",seller="Gopal Sports Store",price=100)
    item2 = Item(item_id=2,name="Utensil",seller="Harbhajan Gift Shop",price=760)
    item1.save()
    item2.save()
    

    return make_response(" ", 201)
    #elif request.method="POST"
'''
Let's go over what each of the HTTP methods for our API does -

POST /api/db_populate + Populates the db and returns 201 success code(empty response body)
'''



@app.route('/api/items',methods=['GET','POST'])
def api_items():
    if request.method =="GET":
        print(request.method)
        items =[]
        for item in Item.objects:
            items.append(item)
        #print(items)
        return make_response(jsonify(items),200)

    elif request.method=="POST":
        content = request.json()
        item= Item(item_id=content['item_id'],name=content['name'],seller=content['seller'],price=content['price'])
        item.save()
        return request.method(" ",201)
'''

GET /api/items + Returns the details of all items (with code 200 success code)

POST /api/items + Creates a new item and returns 201 success code (empty response body)
'''

@app.route('/api/items/<item_id>',methods=['GET','PUT','DELETE'])
def api_each_item(item_id):
    if request.method=="GET":
        item_object= Item.objects(item_id=item_id).first()
        if item_object:
            return make_response(jsonify(item_object.to_json()),200)
        else:
            return make_response("",404)
    elif request.method=="PUT":
        content=request.json
        item_object= Item.objects(item_id=item_id).first()
        item_object.update(seller=content['seller'],name=content['name'])
        return make_response("",204)


    elif request.method=="DELETE":
        item_object= Item.objects(item_id=item_id).first()
        item_object.delete()
        return make_response("",204)

    
'''

GET /api/items/3 + Returns the details of item 3 (with 200 success code if document found, 404 if not found)

PUT /api/items/3 +  Update seller and name fields of item 3 (with 284 success cade)

DELETE /api/items/3 + Deletes item 3 (with 204 success code)

'''

if __name__== '__main__':
    app.run(debug=True)
