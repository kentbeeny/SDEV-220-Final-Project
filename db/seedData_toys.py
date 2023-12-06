from getDb import get_database

dbname = get_database()

collection_name = dbname["Toys"]

item_1 = {
    "item_name": "Legos",
    "age": 12,
}

item_2 = {
    "item_name": "Action Figures",
    "age": 10,
}

item_3 = {
    "item_name": "Basketballs",
    "age": 13,
}

item_4 = {
    "id": 4,
    "item_name": "Headphones",
    "age": 8,
}

item_5 = {
    "id": 5,
    "item_name": "Books",
    "age": 5,
}

item_6 = {
    "id": 6,
    "item_name": "Stuffed Animals",
    "age": 3,
}

collection_name.insert_many([item_1, item_2, item_3, item_4, item_5, item_6])