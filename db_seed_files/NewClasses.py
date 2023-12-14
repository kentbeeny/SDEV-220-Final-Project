import streamlit as st
from getDb import get_database

dbname = get_database()

class Kids:
    def __init__(self, parentName, kidName, toy, age):
        self.parentName = parentName
        self.kidName = kidName
        self.age = age
        self.toy = toy


# creating list
kid_list = []

# appending instances to list
kid_list.append(Kids('John Smith','Johnny','Legos', 12))
kid_list.append(Kids('Carla Lopez','Sofia','Blocks', 3))
kid_list.append(Kids('Michael Jones','Michelle','Doll', 5))
kid_list.append(Kids('Michael Jones','Tiffany', 'Headphones', 8))
kid_list.append(Kids('Paula Davis','Davis', 'Books', 5))
kid_list.append(Kids('Paula Davis','Paul','Stuffed Animals', 3))

for obj in kid_list:
    collection_name = dbname["Requested"]
    collection_name.insert_one({
        "parent_name": obj.parentName,
        "child_name": obj.kidName,
        "child_age": obj.age,
        "toy_requested": obj.toy
    })



# print("")

class Sponsors:
    def __init__(self, flName, moneyAmount, toy):
        self.flName = flName
        self.moneyAmount = moneyAmount
        self.toy = toy
       

# creating list
donor_list = []

# appending instances to list
donor_list.append(Sponsors('Company','$10,000', None ))
donor_list.append(Sponsors('Anonymous', None, 'Legos' ))
donor_list.append(Sponsors('Corporation','$5,000', None ))
donor_list.append(Sponsors('Rich Mann','$25,000', None ))
donor_list.append(Sponsors('Anonymous','$50','Legos' ))
donor_list.append(Sponsors('Local Bank','$5,000', None ))
donor_list.append(Sponsors('Local Toy Store',None, 'Stuffed Animals' ))


# Accessing object value using a for loop
for obj in donor_list:
    collection_name = dbname["Donated"]
    collection_name.insert_one({
        "donor": obj.flName,
        "money_donated": obj.moneyAmount,
        "toy_donated": obj.toy
    })


class Requestor:
    def __init__(self, flName):
        self.flName = flName
        

# creating list
list = []

# appending instances to list
list.append(Requestor('flName'))


# Accessing object value using a for loop
for obj in list:
    print(obj.flName, sep=' ')

print("")
