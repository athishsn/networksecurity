from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://athishsn:Admin123@cluster0.0ad1j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    database_names = client.list_database_names()
    print(database_names)
    
    db = client["sample_mflix"]  # Replace "myDatabase" with your database name
    collection_names = db.list_collection_names()
    print("Collections in myDatabase:", collection_names)
except Exception as e:
    print(e)
    
    
