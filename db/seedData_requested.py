from getDb import get_database

dbname = get_database()

collection_name = dbname["Requested"]

item_1 = {
    "parent_name": "John Smith",
    "child_name": "Johnny",
    "child_age": 12,
    "toy_requested": "Legos"
}

item_2 = {
    "parent_name": "Carla Lopez",
    "child_name": "Sofia",
    "child_age": 3,
    "toy_requested": "Blocks"
}

item_3 = {
    "parent_name": "Michael Jones",
    "child_name": "Michelle",
    "child_age": 5,
    "toy_requested": "Doll"
}

collection_name.insert_many([item_1, item_2, item_3])