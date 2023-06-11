'''Write a Python function which finds the length of the string, if the length of the string is multiple of 5, reverse the string and capitalize all the characters.
'''
str1=input("Enter the string: ")
x=len(str1)
if x%5==0:
    print("The string is multiple of 5.")
    str2=str1.upper()
    print(str2[::-1])
else:
    print("Not divisible by 5")
    
