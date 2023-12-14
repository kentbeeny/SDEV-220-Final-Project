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
kid_list.append(Kids('parent1','kidName1','Legos', 12))
kid_list.append(Kids('parent1','kidName2','Action Figures', 10))
kid_list.append(Kids('parent2','kidName1','Basketballs', 13))
kid_list.append(Kids('parent3','kidName1', 'Headphones', 8))
kid_list.append(Kids('parent3','kidName2', 'Books', 5))
kid_list.append(Kids('parent3','kidName3','Stuffed Animals', 3))

for obj in kid_list:
    collection_name = dbname["Requested"]
    collection_name.insert_one({
        "parent_name": obj.parentName,
        "child_name": obj.kidName,
        "child_age": obj.age,
        "toy_requested": obj.toy
    })

# Accessing object value using a for loop
@st.cache_data(ttl=600) # Annotation to refresh the data every 5 minutes
def seeReq():
    collection_name.find()

# print("")

class Sponsors:
    def __init__(self, moneyAmount, toy, flName):
        self.moneyAmount = moneyAmount
        self.toy = toy
        self.flName = flName
       

# creating list
list = []

# appending instances to list
list.append(Sponsors('moneyAmount','toy', 'flName'))


# Accessing object value using a for loop
for obj in list:
    print(obj.moneyAmount, obj.toy, obj.flName, sep=' ')

print("")


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
