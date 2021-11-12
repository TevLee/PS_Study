#19:15 - 19:25
def solution(v):
    answer = []
    p = list(zip(v[0],v[1],v[2]))
    for i in range(3):
        if p[0].count(v[i][0])==1:
            answer.append(v[i][0])
    for i in range(3):
        if p[1].count(v[i][1])==1:
            answer.append(v[i][1])
    return answer