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
    print(obj.kidName, obj.toy, obj.age, sep=' ')

print("")

class Sponsors:
    def __init__(self, moneyAmount, toy, fName, lName):
        self.moneyAmount = moneyAmount
        self.toy = toy
        self.fName = fName
        self.lName = lName


# creating list
list = []

# appending instances to list
list.append(Sponsors('moneyAmount','toy', 'fName', 'lName'))


# Accessing object value using a for loop
for obj in list:
    print(obj.moneyAmount, obj.toy, obj.fName, obj.lName, sep=' ')

print("")


class Requestor:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName



# creating list
list = []

# appending instances to list
list.append(Requestor('fName', 'lName'))


# Accessing object value using a for loop
for obj in list:
    print(obj.fName, obj.lName, sep=' ')

print("")
