#https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

def birthdayCakeCandles(candles):
    # Write your code here
    st = {}
    for i in candles:
        if i in st:
            st[i] += 1
        else:
            st[i] = 1
    resMax = 0
    for i in st:
        if st[i] > resMax:
            resMax = st[i]
    return resMax

callable = [3, 2, 1, 3]
print(birthdayCakeCandles(callable))