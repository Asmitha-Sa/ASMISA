'''x/2 + x/4 + x/8 + x/16 + ….. + N
 	Sample Input
N = 7 (Number of terms)
X = 2
Then the series will be 2/2 + 2/4 + 2/8 + 2/16 + 2/32 + 2/64 + 2/128
'''
n=int(input("Enter no.of terms: "))
x=int(input("Enter x value: "))

def ser(n,x):
    res=0
    for i in range(1,n+1):
        res=res+(x/(2**i))
    print(res)

ser(n,x)
