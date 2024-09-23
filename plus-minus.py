#https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

def plusMinus(arr):
    # Write your code here
    posNum = 0
    nagNum = 0
    zeroNum = 0
    baseLen = len(arr)
    for i in arr:
        if i == 0 : 
            zeroNum += 1
        elif i > 0 :
            posNum += 1
        elif i < 0 :
            nagNum += 1
    print(round(posNum/baseLen, 6))
    print(round(nagNum/baseLen, 6))
    print(round(zeroNum/baseLen, 6))

arr = [-4, 3, -9, 0, 4, 1]

print(plusMinus(arr))