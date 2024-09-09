#https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a, b):
    # Write your code here
    res = [0, 0]
    for a, b in zip(a, b):
        if a > b:
            res[0] += 1
        if b > a:
            res[1] += 1
    return res

a, b = [5,6,7], [3,6,10]

print(compareTriplets(a,b))