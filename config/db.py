from pymongo import MongoClient
from protected import mongo_passwd
connection_string = f"mongodb+srv://topo-user:{mongo_passwd}@topo.u7rtq.mongodb.net/?retryWrites=true&w=majority&appName=Topo"
connection = MongoClient(connection_string)