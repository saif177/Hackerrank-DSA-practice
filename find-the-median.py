#https://www.hackerrank.com/challenges/find-the-median/problem?h_r=profile

def findMedian(arr):
    # Write your code here
    arr = sorted(arr)
    return arr[len(arr)//2]

arr = [0, 1, 2, 4, 6, 5, 3]

print(findMedian(arr))