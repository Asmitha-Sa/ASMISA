'''Write a Python function that takes a sentence and returns the longest word and the length of the longest one.
'''
def longestLength(a):
    max1 = len(a[0])
    temp = a[0]
    for i in a:
        if(len(i) > max1):
 
            max1 = len(i)
            temp = i
 
print("The word with the longest length is:", temp," and length is ", max1)
st1=input("Enter the sentence: ")
a=st1.split()
longestLength(a)
    
