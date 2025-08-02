# Nested Dictionary

student = {
    "name" : "Sabbir",
    "sub" : {
        "phy" : 90,
        "che" : 90,
        "math" : 100
    }
}
print(student)
print(student["sub"])
print(student["sub"]["math"])
print()

# Methods in Dictionary

# Printing All keys
print(list(student.keys()))

# Length of Dictionary
print(len(student))

# Return all values
print(list(student.values()))

# Return all (key, value)pairs as tuples
print(list(student.items()))

# Returns the key according to value
print(student.get("name")) #Give us None value
print(student["name"]) #Give us Error

# Inserts the specified items to the dictionaries
new_dict = {"city" : "Dhaka", "village" : "Brahmanbaria"}
student.update(new_dict)
print(student)
