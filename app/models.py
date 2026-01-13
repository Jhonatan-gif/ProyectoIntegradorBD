from app import mongo
from bson import ObjectId

def all(col):
    return list(mongo.db[col].find())

def get(col, id):
    return mongo.db[col].find_one({"_id": ObjectId(id)})

def insert(col, data):
    return mongo.db[col].insert_one(data)

def update(col, id, data):
    return mongo.db[col].update_one({"_id": ObjectId(id)}, {"$set": data})

def delete(col, id):
    return mongo.db[col].delete_one({"_id": ObjectId(id)})
