#link - https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum(ar):
    # Write your code here
    res = 0
    for i in ar:
        res += i
    return res

arr = [1, 2, 3, 4, 10, 11]
print(simpleArraySum(arr))