#https://www.hackerrank.com/challenges/strange-code/problem?h_r=profile

def strangeCounter(t):
    # Write your code here
    time = 3
    
    while True:
        t -= time
        if t <= 0:
            t += time
            return time - t + 1
        time *= 2
# set time = 3
# first itteration minus time with t and add to t
#   if time <= 0 
#   add time to t and return time - t + 1
#   second itteration multiply time by 2 and double it

t = 4      
print(strangeCounter(t))