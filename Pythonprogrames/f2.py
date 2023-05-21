name=input("Enter your name: ")
age=int(input("Enter your age: "))
gen=input("Enter gender(M/F): ")
p=int(input("Enter Principal amount: "))
n=int(input("Enter number of years: "))

def SI(p,n,r):
    si=(p*r*n)/100
    print("SI is",si)
    
if age>=60:
    r=12
    SI(p,n,r)
elif age<60 and gen=='F':
    r=10
    SI(p,n,r)
elif age<60 and gen=='M':
    r=9
    SI(p,n,r)
else:
    print("Invalid entry")
    
