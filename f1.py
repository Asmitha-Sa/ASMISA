#Perfect square or not using functions

n=int(input("Enter the number: "))

def num(n):
    i=1
    while i<=n:
        if n==i*i:
            return print("Perfect square number")
        i=i+1
    else:
        return print("not a perfect square number")
num(n)


