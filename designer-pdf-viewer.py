#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


def designerPdfViewer(h, word):
    # Write your code here
    maxVal = 0
    for i in word:
        maxVal = max(maxVal, h[ord(i) - 97])
    return maxVal * len(word)
    

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,55]
word = 'abc'
print(designerPdfViewer(h, word))