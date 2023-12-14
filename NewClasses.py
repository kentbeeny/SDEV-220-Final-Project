from getDb import get_database

dbname = get_database()

# for item in items:
    # st.write(f"{item}")

class Kids:
    def __init__(self, kidName, toy, age):
        self.name = kidName
        self.age = age
        self.toy = toy


# creating list
list = []

# appending instances to list
list.append(Kids('kidName','Legos', 12))
list.append(Kids('kidName','Action Figures', 10))
list.append(Kids('kidName','Basketballs', 13))
list.append(Kids('kidName', 'Headphones', 8))
list.append(Kids('kidName', 'Books', 5))
list.append(Kids('kidName','Stuffed Animals', 3))

# Accessing object value using a for loop
for obj in list:
    #print(obj.kidName, obj.toy, obj.age, sep=' ')
    #changing the above to test ##########################################
    #the below fixed the error-> 'Kids' object has no attribute 'kidName'"
    print(obj.name, obj.toy, obj.age, sep=' ')

print("")

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
