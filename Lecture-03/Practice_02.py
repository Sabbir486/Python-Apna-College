list1 = [1, 2, 3]
list2 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("Palindrome")

else:
    print("Not Palindrome")


copy_list2 = list2.copy()
copy_list2.reverse()


if(list2 == copy_list2):
    print("Palindrome")

else:
    print("Not Palindrome")



