
#https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    min_diff = float('inf')
    res = []
    
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
            res = [arr[i-1], arr[i]]
        elif diff == min_diff:
            res.extend([arr[i-1], arr[i]])
    return res


arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470 ]
print(closestNumbers(arr))