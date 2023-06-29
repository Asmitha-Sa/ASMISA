'''STRINGS AND ITS OPERATIONS
Given two strings, PRINT (YES or NO) whether the second string can be obtained from the first
by deletion of none, one or more characters'''


def isfun(s1, s2):
    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1
    return i == n
 
s1=input("Enter sub string: ")
s2=input("Enter main string: ")

if (isfun(s1, s2)):
    print(s1,"is a substring of",s2)
else:
    print(s1,"is not a substring of",s2)
    