# 19:09 - 19:12 (3)
def solution(n,m): #자연수
    answer = 0
    for i in range(n,m+1):
        isPal = list(str(i))
        if isPal == isPal[::-1]:
            answer+=1
    return answer