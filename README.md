# Shopping-Cart-Rest-API

This repository contains python files to perform crud operation on a shopping cart using Python/MongoDB.
api_constants is merely used to hide user passwords which is then imported in other two files.
Two files:
        api_mongo.py containts the python code for creating a rest api and performing crud operations.
        mongodbstart.py contains the python code to connect to the database which performs crud operations without calling api.
Database name =API
Collection Name= item

To run these file open any editor visual studio code, sublime or any of your choice. Since I have made use of flask you need to create an virtual environment.
Clone the files into one folder.
Open terminal and set the directory as folder name.
Then to set virtual environment perform following commands:
        py -m venv env
        env/Scripts/activate
Virtual environment is set now, import all the necessary modules and run the file.
To call the api you can use postman or httpie

HTTPie is a command line HTTP client. Its goal is to make CLI interaction with web services as human-friendly as possible.
Install HTTPie : pip install --upgrade httpie

http POST http:/.........../api/db_populate
http GET  http:/.........../api/items

