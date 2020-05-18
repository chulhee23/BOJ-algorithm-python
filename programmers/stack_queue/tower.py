import collections

def solution(h):
    h=[[i,v] for i, v in enumerate(h)]
    h=sorted(h, reverse= True)
    print(h)
    deq = []
    ans =[]
    for item in h:
        deq.append(item)
        for ay in deq:
            if ay[1] < item[1]:
                print(item[0])
                ans.append(item[0])
                deq.pop(0)
    print(ans)
    return ans

solution([6,9,5,7,4])