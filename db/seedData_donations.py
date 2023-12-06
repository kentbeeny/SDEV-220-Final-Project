from getDb import get_database

dbname = get_database()

collection_name = dbname["Donations"]

item_1 = {
    "item_name": "Cash Donation",
}

item_2 = {
    "item_name": "Toy Donation",
}

item_3 = {
    "item_name": "Service Donation",
}

collection_name.insert_many([item_1, item_2, item_3])