from pymongo import MongoClient
import certifi
ca=certifi.where()

def get_database():
    CONNECTION_STRING = "mongodb+srv://ahask93:finalproject@cluster1.itmbuuh.mongodb.net/"
    client = MongoClient(CONNECTION_STRING, tlsCAFile=ca)

    return client['TFT']

if __name__ == "__main__":
    dbname = get_database()