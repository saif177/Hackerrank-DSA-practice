#https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
from collections import Counter

def missingNumbers(arr, brr):
    # Write your code here
    arr_count = Counter(arr)
    brr_count = Counter(brr)
    missing = [num for num in brr_count if brr_count[num] > arr_count[num]]
    return sorted(missing)
    
arr = [1,2,3,4,5,6]
brr = [1,2,4,5,6,7,8]
print(missingNumbers(arr, brr))