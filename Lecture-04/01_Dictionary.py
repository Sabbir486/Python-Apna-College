# Dictionary is mutable

# key : value

info = {
    "key" : "value",
    "name" : "Sabbir",
    "CGPA" : "3.81",
    "age" : 25,
    95.5 : "Marks"
}
print(info)

print(info[95.5])

info[95.5] = "Highest Marks"
print(info[95.5])

print()

# Can also store list and tupple
# Tupple is immutable. That's why it will be only key

store = {
    "name" : ["sa", "ra", "ta"],
    "sub" : ("dict", "python")
}
print(store)
print(type(store))
print(store["sub"])
print()

# Creating empty dictionary

null_dict = {

}
print(null_dict)
null_dict["name"] = "Sabbir Ahmed"
print(null_dict)
