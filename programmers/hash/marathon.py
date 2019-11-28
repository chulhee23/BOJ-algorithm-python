# list에서 같은 원소를 제거하는 코드

import collections

def solution1(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    print(*list(answer.keys()))
    return list(*answer.keys())

def solution2(a, b):
    aa = sorted(a)
    bb = sorted(b)
    answer = aa[-1]
    for i in range(len(sorted(b))):
        breakpoint()
        if aa[i] != bb[i]:
            answer = aa[i]
            break
    
    return(answer)




# solution1(["a","b","c"], ["a","b"])
solution2(["leo", "kiki", "eden"], ["eden", "kiki"])