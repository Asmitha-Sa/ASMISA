'''PROGRAMS ON SELECTION AND ITERATION OPERATION
Get an integer input from a user. If the number is odd, then find the factorial of the number and find the number
of digits in the factorial of the number. If the number is even, then check if the given number is a palindrome or not.
'''

n=int(input("Enter a number: "))
if n%2!=0:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    count=0
    while fact!=0:
        x=fact%10
        count=count+1
        fact=fact//10
    print("No.of digits in of given number factorial is ",count)
else:
    temp=n
    rev=0
    while n!=0:
        x=n%10
        rev=(rev*10)+x
        n=n//10
    if temp==rev:
        print("Even and Palindrome")
    else:
        print("Even and not a palindrome")
        
    
