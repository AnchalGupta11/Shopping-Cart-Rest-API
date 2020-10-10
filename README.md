# Shopping-Cart-Rest-API

This repository contains python files to perform crud operation on a shopping cart using Python/MongoDB.

api_constants is merely used to hide user passwords which is then imported in other two files.

Two files:
       
       api_mongo.py containts the python code for creating a rest api and performing crud operations.
        
        mongodbstart.py contains the python code to connect to the database which performs crud operations without calling api.
        
Database name =API

Collection Name= item

Sample:       [
    {
        "_id": {
            "$oid": "5f8129737f764cb4702e9b9b"
        },
        "item_id": 1,
        "name": "Football",
        "price": 100,
        "seller": "Gopal Sports Store"
    },
    {
        "_id": {
            "$oid": "5f8129767f764cb4702e9b9d"
        },
        "item_id": 1,
        "name": "Football",
        "price": 100,
        "seller": "Gopal Sports Store"
    },
    {
        "_id": {
            "$oid": "5f8129777f764cb4702e9b9e"
        },
        "item_id": 2,
        "name": "Utensil",
        "price": 760,
        "seller": "Harbhajan Gift Shop"
    }
]

To run these file open any editor visual studio code, sublime or any of your choice. Since I have made use of flask you need to create an virtual environment.

Clone the files into one folder.

Open terminal and set the directory as folder name.

Then to set virtual environment perform following commands:

        py -m venv env
        
        env/Scripts/activate
        
Virtual environment is set now, import all the necessary modules and run the file.
(If you recieve 500 internal error while calling api of api_mongo.py then try to run mongodbstart.py and see whether desired operations are printed or not.)

To call the api you can use postman or httpie

HTTPie is a command line HTTP client. Its goal is to make CLI interaction with web services as human-friendly as possible.

        Install HTTPie : pip install --upgrade httpie

        http POST http:/.........../api/db_populate

        http GET  http:/.........../api/items
      
While working on POSTMAN you have to make sure what request you use with the desired api:

[POST] http://127.0.0.1.5000/api/db_populate                       #Creating a cart

[GET,POST]   http://127.0.0.1:5000/api/itmes                       # to get the list of all items using Get request and POST to insert you can use post with echo

              echo '{"item_id":"","name":"","seller":"","price":""}'|http://127.0.0.1:5000/api/item

[GET,PUT,DELETE]  http://127.0.0.1:5000/api/items/<item_id>        #use GET to get the desired item_id item
                                                                   #use PUT to update the desired item
                                                                   #use DELETE to delete the desired item
