num = int(input("Enter the number: "))

if(num % 2 == 0):
    print("Even")

else:
    print("Odd")

print()

num1 = int(input("1st Number: "))
num2 = int(input("2nd Number: "))
num3 = int(input("3rd Number: "))

if(num1 > num2):
    if(num1 > num3):
        print("1st one is greatest")

elif(num3 > num2):
    if(num3 > num1):
        print("3rd one is greatest")

else:
    print("2nd one is greatest")