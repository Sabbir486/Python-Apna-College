# Range

idx = range(5)
print(idx[0])
print(idx[3])
print()


for el in range(1,10, 2): #Start Val, End Val(Exclude), Difference
    print(el)

print("End Loop")


# Practice Question:

n = int(input("Enter Number: "))

for num in range(1,11):
    val = n * num
    print("Value ", num, " : ",val)