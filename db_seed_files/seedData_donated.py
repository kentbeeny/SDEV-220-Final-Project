from getDb import get_database

dbname = get_database()

collection_name = dbname["Donated"]

item_1 = {
    "donor": "Company",
    "money_donated": "$10,000",
    "toys_donated": None
}

item_2 = {
    "donor": "Anonymous",
    "money_donated": None,
    "toys_donated": "Legos"
}

item_3 = {
    "donor": "Corporation",
    "money_donated": "$5000",
    "toys_donated": None
}

collection_name.insert_many([item_1, item_2, item_3])