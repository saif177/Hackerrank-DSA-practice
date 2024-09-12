#https://www.hackerrank.com/challenges/chocolate-feast/problem?h_r=profile

def chocolateFeast(n, c, m):
    # Write your code here
    chocolates = n // c
    wrappers = chocolates

    while wrappers >= m:
        new_chocolates = wrappers // m
        chocolates += new_chocolates
        wrappers = wrappers % m + new_chocolates

    return chocolates

n = 6
c = 2
m = 2
print(chocolateFeast(n, c, m))