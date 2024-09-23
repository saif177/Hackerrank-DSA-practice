#https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    resApple = 0
    resOranges = 0
    
    for i in apples:
        if (i + a) >= s and (i + a) <= t:
            resApple += 1
    
    for j in oranges:
        if (j + b) <= t and (j + b) >= s:
            resOranges +=1
            
    print(resApple)
    print(resOranges)

s, t, a, b, apples, oranges = 7, 10,  4, 12, [6,7,0], [15,10,8]

countApplesAndOranges(s, t, a, b, apples, oranges)