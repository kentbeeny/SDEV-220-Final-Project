from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb+srv://ahask93:finalproject@cluster1.itmbuuh.mongodb.net/"
    client = MongoClient(CONNECTION_STRING, ssl_cert_reqs=ssl.CERT_NONE)

    return client['TFT']

if __name__ == "__main__":
    dbname = get_database()