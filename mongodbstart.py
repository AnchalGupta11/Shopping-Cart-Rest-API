import mongoengine as db
from api_constants import mongo_passwords


database_name="API"
password= mongo_passwords
DB_URL="mongodb+srv://dbadmin:{}@cluster0.l40iw.mongodb.net/{}?retryWrites=true&w=majority".format(password,database_name)
db.connect(host=DB_URL)

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

print("\nCreate a cart")
item = Item(item_id=1,name="Football",seller="Gopal Sports Store",price=100)
item.save()
print("\n Fetch an item")
item =Item.objects(item_id=1).first()
print(item.to_json())



item3 = Item(item_id=4,name="toys",seller="Arvind Toy Store",price=200)
item3.save()
print("\n Fetch an item")
item3 =Item.objects(item_id=4).first() #Creates duplicate item
print(item3.to_json())

print("\nUpdate an item")
item3.update(name="food item",price="175")
print(item3.to_json())
print("\n add another book")

item4=Item(item_id=5,name="ludo",seller=" Toy Store",price=200)
item4.save()

print("\n Fetch all items")
items=[]
for item in Item.objects():
    items.append(item.to_json())
print(items)


print("\nFind items whose name contains The")
items = []
for item in Item.objects(name__contains='ball'):
    items.append(item.to_json())
print(items)

print("\nHow many items are in a collection?")
print(Item.objects.count())

print("\nOrder by seller field")
items = []
for item in Item.objects().order_by('seller'):
    items.append(item.to_json())
print(items)

print("\nDelete an item")
item = Item.objects(item_id=2).first()
item.delete()
print(Item.objects.count())

print("\nDelete all books in a collection")
for item in Item.objects():
    item.delete()
print(Item.objects.count())