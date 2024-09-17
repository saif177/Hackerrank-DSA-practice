#https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true

import math

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)
    
def lcm_of_list(arr):
    l = arr[0]
    for i in arr[1:]:
        l = lcm(l, i)
    return l

def gcd_of_list(arr):
    g = arr[0]
    for i in arr[1:]:
        g = math.gcd(g, i)
    return g
    

def getTotalX(a, b):
    # Write your code here
    lcm_A = lcm_of_list(a)
    gcd_B = gcd_of_list(b)
    
    count = 0
    multiple = lcm_A
    while multiple <= gcd_B:
        if gcd_B % multiple == 0:
            count += 1
        multiple += lcm_A
    
    return count

a = [2,4]
b = [16,32,96]

print(getTotalX(a, b))