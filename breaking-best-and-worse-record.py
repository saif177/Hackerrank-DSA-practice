#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

def breakingRecords(scores):
    # Write your code here
    max_record = scores[0]
    min_record = scores[0]
    max_record_count = 0
    min_record_count = 0
    
    for i in scores:
        if i > max_record:
            max_record_count += 1
            max_record = i
        elif i < min_record:
            min_record_count += 1
            min_record = i
            
    return [max_record_count, min_record_count]
    
scores = [4, 5, 2, 25, 1]
print(breakingRecords(scores))