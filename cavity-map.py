#https://www.hackerrank.com/challenges/cavity-map/problem?isFullScreen=false

def cavityMap(grid):
    # Write your code here
    n = len(grid)
    grid = [list(rows) for rows in grid]
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            current = grid[i][j]
            if current > grid[i-1][j] and current > grid[i+1][j] and current > grid[i][j-1] and current > grid[i][j+1]:
                grid[i][j] = 'X'
    return [''.join(rows) for rows in grid]

grid = ['1112', '1912', '1892', '1234']
print(cavityMap(grid))

#start from index 1 till len -1 
#look around up-down left-right if they all are less than current
#set = 'x'