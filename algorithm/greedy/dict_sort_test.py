import operator

dict={"a":7, "c":3, "b":5}
sortedDict = sorted(dict.items(), key = operator.itemgetter(0))
print(sortedDict)
sortedDict2 = sorted(dict.items(), key = operator.itemgetter(1))

print(sortedDict2)