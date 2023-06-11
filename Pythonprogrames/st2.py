'''Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample Input
Mike
Dice
Sample Output
Dike
Mice
'''
st1=input("Enter the 1st string: ")
st2=input("Enter the 2nd string: ")
st=st1+" "+st2
print(st)
x=st2[0:2]+st1[2:]+" "+st1[0:2]+st2[2:]
print(x)
