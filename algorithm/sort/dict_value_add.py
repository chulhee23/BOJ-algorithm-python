
import operator
n= int(input())

count={}
for i in range(n):
    a= input()

    if (count.get(a) == None):
        count[a] = 1
    else:
        count[a] += 1

sortedCount = sorted(count.items(), key= operator.itemgetter(1))
for word, cnt in sortedCount:
    print(word)




