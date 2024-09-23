#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

def diagonalDifference(arr):
    col = len(arr[0])
    row = len(arr)
    rDiagonal = 0
    lDiagonal = 0
    
    for i in range(col):
        rDiagonal += arr[i][i]
    for j in range(row):
        lDiagonal += arr[j][(row - 1) - j]
        
    return abs(lDiagonal - rDiagonal)

arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]
       ]

print(diagonalDifference(arr))