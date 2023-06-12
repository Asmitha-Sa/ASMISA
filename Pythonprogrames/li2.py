'''The python program should read the list of 5 numbers, and generate the new list which
contains the factorial of each number in the given list. 
Sample Input
[2, 4, 8, 7, 5]
Sample Output
[2, 24, 40320, 5040, 120]
'''
n=int(input("Enter no.of elemnts: "))
l1=[]
for i in range(0,n):
    l1.append(int(input("Enter: ")))
print(l1)
l2=[]
fact=1
for j in l1:
    fact=fact*j
    l2.append(fact)
print(l2)