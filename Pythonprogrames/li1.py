'''Write a python program which reads “n” number of integers from the user and generates a separate list containing even and odd numbers.
'''

n=int(input("Enter no.of elemnts: "))
list1=[]
list2=[]
for i in range(0,n+1):
    num=int(input("Enter: "))
    if num%2==0:
        x=list1.append(i)
    else:
        y=list2.append(i)
print("The odd elements: ",list1)
print("The even elements: ",list2)
