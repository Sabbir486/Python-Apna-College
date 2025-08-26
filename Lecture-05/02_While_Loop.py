# While Loop

count = 0
while(count < 5):
    print("Hello", count)
    count += 1

print(count)
print()


# Break 

i = 1
while (i<5):
    print(i)

    if(i == 3):
        break
    i += 1
print("End Of Loop")
print()


# Continue

i = 1
while (i<5):

    if(i == 3):
        i += 1
        continue  #Skip

    print(i)
    i += 1
print("End Of Loop")
print()