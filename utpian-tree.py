
#https://www.hackerrank.com/challenges/utopian-tree/problem

def utopianTree(n):
    # Write your code here
    h = 1
    for i in range(1, n+1):
        if (i % 2 == 0):
            h += 1
        else:
            h *= 2
    return h

h = 10
print(utopianTree(h))