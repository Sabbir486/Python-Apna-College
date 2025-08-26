# While Loop Practice:

# Q-1

n = int(input("Enter Number: "))
i = 1

while(i<=10):
    print("Value ", i, " : ",i*n)
    i += 1

print()


# Q-2

nums = [1,4,9,16,25,36,49,81,100]
idx = 0

while (idx <= len(nums)-1): #Index 0 to 9; total = 10
    print(nums[idx])
    idx += 1