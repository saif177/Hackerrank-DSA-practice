#https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, k, queries):
    # Write your code here
    n = len(a)
    k = k % n
    res = []
    for q in queries:
        rotated_index = (q - k + n) % n
        res.append(a[rotated_index])
    
    return res


a = [1,2,3,4]
k = 2
queries = [1,3]
print(circularArrayRotation(a, k, queries))