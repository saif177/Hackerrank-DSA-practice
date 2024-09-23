#https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] > 37:
            diff = grades[i] % 5
            if diff != 0 and diff >= 3:
                grades[i] += (5 - diff)
    return grades

grades = [73,67,38,33]
print(gradingStudents(grades))