from flask import Flask

from pymongo import MongoClient

app=Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")

db = client.test_database

collection = db.test_collection

@app.route("/")
def index():
   data = collection.find_one()

   return str(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
