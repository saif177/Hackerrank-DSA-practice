#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

def timeConversion(s):
    if 'PM' in s:
        ss=s[0]+ s[1]
        if ss >='12':
            x=s.replace('PM', '')
            return x
        else:
            c=int(ss)+12
            a=s.replace(ss, str(c))
            b=a.replace('PM', '')
            return b
    if 'AM' in s:
        ss=s[0]+ s[1]
        if ss <'12':
            # a=s.replace(ss, str(ss))
            x=s.replace('AM', '')
            return x
        else:
            c=int(ss)-12
            a=s.replace(ss, str(c))
            b=a.replace('AM', '')
            bb=b.split(":")
            # print(bb)
            if len(bb[0])<=1:
                bb[0]='0'+bb[0]
                cc=':'.join(bb)
                return cc
            

s = '07:05:45PM'

print(timeConversion(s))