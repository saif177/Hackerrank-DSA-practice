#https://www.hackerrank.com/challenges/find-digits/

def findDigits(n):
    # Write your code here
    s=str(n)
    c=0
    for i in s:
        if i != '0' and n % int(i)==0:
            c+=1
    return c

n = 12240
print(findDigits(n))