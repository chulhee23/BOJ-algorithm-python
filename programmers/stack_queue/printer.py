    
def solution(p, l):
    cnt = 0
    while(len(p) > 1 or l > 0):
        tmp = p.pop(0)
        cnt += 1
        print("cnt: ", cnt)
        if (max(p) > tmp):
            p.append(tmp)
            l -= 1
            
            cnt -= 1
            if l < 0:
                l = len(p) - 1
        
    print(cnt)
    return cnt
        

print("=====111111======")
solution([2, 1, 3, 2], 2)
print("===========")
print("=====2222======")
solution([1, 1, 9, 1, 1, 1],0)