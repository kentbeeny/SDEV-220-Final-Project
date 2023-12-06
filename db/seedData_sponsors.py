from getDb import get_database

dbname = get_database()

collection_name = dbname["Sponsors"]

item_1 = {
    "item_name": "Companies",
}

item_2 = {
    "item_name": "Individuals",
}

item_3 = {
    "item_name": "Corporations",
}

collection_name.insert_many([item_1, item_2, item_3])