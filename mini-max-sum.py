
def miniMaxSum(arr):
    # Write your code here
    sumVal = sum(arr)
    print(sumVal- max(arr), sumVal-min(arr))

arr = [1, 2, 3, 4, 5]
print(miniMaxSum(arr))