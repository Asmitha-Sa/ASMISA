'''15 + 30 + 45 + 60 + …… + N
Sample Input
N = 5 (Number of terms)
Then the series will be 15 + 30 + 45 + 60 +75
'''
n=int(input("Enter no.of terms: "))
def ser(n):
    res=0
    r=15
    su=0
    for i in range(1,n+1):
        res=res+r
        su=su+res
    print(su)
ser(n)
    