def solution(phone_book):
    answer = True
    arr  = sorted(phone_book)
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            tmp = arr[i] in arr[j]

            if tmp:
                answer = False
                return answer

    return answer
solution(["119", "97674223", "1195524421"])