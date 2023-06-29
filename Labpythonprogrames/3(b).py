'''CHECK FOR ASCENDING ORDER IN LIST
Read the list of numbers and find whether the list is in ascending order or not.'''

n=int(input("Enter  number of elements: "))
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)
print("List: ",nums)

print ("Original list : " + str(nums)) 

flag = 0
list1 = nums[:]
list1.sort()
if (list1 == nums):
    flag = 1
     
if (flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")
