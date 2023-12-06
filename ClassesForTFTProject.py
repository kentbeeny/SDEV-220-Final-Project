class toys:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# creating list
list = []

# appending instances to list
list.append(toys('Legos', 12))
list.append(toys('Action Figures', 10))
list.append(toys('Basketballs', 13))
list.append(toys('Headphones', 8))
list.append(toys('Books', 5))
list.append(toys('Stuffed Animals', 3))

# Accessing object value using a for loop
for obj in list:
    print(obj.name, obj.age, sep=' ')

print("")

class sponsors:
    def __init__(self, name):
        self.name = name


# creating list
list = []

# appending instances to list
list.append(sponsors('Companies'))
list.append(sponsors('Individuals'))
list.append(sponsors('Corporations'))

# Accessing object value using a for loop
for obj in list:
    print(obj.name, sep=' ')

print("")


class donation:
    def __init__(self, type):
        self.type = type



# creating list
list = []

# appending instances to list
list.append(donation('Cash Donation'))
list.append(donation('Toy Dontations'))
list.append(donation('Donate a Service'))

# Accessing object value using a for loop
for obj in list:
    print(obj.type, sep=' ')

print("")