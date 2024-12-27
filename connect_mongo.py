from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
 
def connect_mongo():
    uri = "mongodb+srv://paramaguruvh:Guru1910@cluster0.m5ten.mongodb.net/database?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    db=client["Appian_Ai_Application"]
    return db
