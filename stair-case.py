
def staircase(n):
    # Write your code here
    for i in range(n):
        print(((" ")*(n-1-i))+(("#")*(i+1)))
        
n = 9

print(staircase(n))