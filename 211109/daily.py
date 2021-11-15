def solution(citations):
    answer = 0
    citations.sort() #[0,1,2,5,6] 3의 index는 -3
    for i in range(1,len(citations)+1):
        if citations[-i] >= i:
            answer = i
    return answer