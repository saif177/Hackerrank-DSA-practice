#https://www.hackerrank.com/challenges/kaprekar-numbers/problem

def kaprekarNumbers(p, q):
    # Write your code here
    res = []
    for i in range(p, q+1):
        sqrt = str(i**2)
        n = len(sqrt)
        if i == 1:
            res.append(i)
        elif n > 1 and i == int(sqrt[:n//2]) + int(sqrt[n//2:]):
            res.append(i)
            
    if len(res) == 0:
        print('INVALID RANGE')
    else:
        print(*res)


p = 1
q = 100
print(kaprekarNumbers(p, q))