'''Write a python program which reads “n” words from the user, store it in the list and display the length of
each word and display the longest word in the list.'''

def longestLength(a):
    max1 = len(a[0])
    temp = a[0]
    for i in a:
        if(len(i) > max1):
             max1 = len(i)
             temp = i
print("The word with the longest length is:", temp," and length is ", max1)

st1=input("Enter the sentence: ")
a=list(st1)
longestLength(a)