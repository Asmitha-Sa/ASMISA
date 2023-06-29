'''Positive and Negative Indexing
Write a python program which reads a list of “n” numbers from the user, finds whether a particular number is present in the list or not, if present, then stores its
positive and negative index in two different lists and displays the occurrence of the number.
Sample Input
[2, 6, 7, 12, 17, 7, 8, 2, 6, 20, 3, 5]
Enter the element to be found : 7
Sample Output
Element 7 occurs 2 times in the list.
Positive Index : 2, 5
Negative Index : -7, -10'''

n=int(input("Enter number of elements: "))
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)
print("List: ",nums)
a=int(input("Enter the number to be found: "))

def index(nums,a):
    pindex=[]
    nindex=[]
    ncount=0
    c=len(nums)
    for i in range(0,c):
        if nums[i]==a:
            pindex.append(i)
            nindex.append(-c+i)
            ncount+=1
    return(pindex,nindex,ncount)

print("The Positive index , Negative index and no.of times occured:")
print(index(nums,a))