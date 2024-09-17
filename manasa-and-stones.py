#https://www.hackerrank.com/challenges/manasa-and-stones/problem?h_r=profile

def stones(n, a, b):
    # Write your code here
    result = set()
    
    for i in range(n):
        result.add(i * a + (n - 1 - i) * b)
        
    return sorted(result)

n,a,b = 2,3,4
print(stones(n, a, b))