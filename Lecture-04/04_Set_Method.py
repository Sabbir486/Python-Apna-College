# Set Methods

collection = set() #Empty set

# Add Method
collection.add(1)
collection.add(2)
collection.add("Sabbir")
collection.add((1,2,3))  #We can add Tupple(Immutable) but can not add list or dictionary(Mutable)
print(collection)

# Remove Method
collection.remove(2)
print(collection)

# Pop Method --> Remove a random value
print(collection.pop())

# Clear Method
collection.clear()
print(collection)
print()

# Union Method

set1 = {1, 2, 3}
set2 = {3, 4, 5}

final1 = set1.union(set2)
print(final1)

# iNTERSECTION Method

final2 = set1.intersection(set2)
print(final2)


