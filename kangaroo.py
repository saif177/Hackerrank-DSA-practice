#https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 < v2:
        return 'NO'
    else:
        if v1!=v2 and (x2-x1) % (v1-v2) == 0:
            return 'YES'
        else:
            return 'NO'

x1, v1, x2, v2 = 0, 2, 5, 3    
print(kangaroo(x1, v1, x2, v2))