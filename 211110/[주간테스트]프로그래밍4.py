# 14:38 - 14:53 (테스트 8부터 실패)
# 14:53 - 15:01 (반대방향 이동 중복체크로 실패했었음)
def solution(dirs): # UDRL
    answer = 0 #처음걸어본 길의 길이
    s = [0,0] #start
    e = [0,0]
    routes = []
    ds = {'U':[0,1],'D':[0,-1],'R':[1,0],'L':[-1,0]} # directions
    for dir in dirs:
        e = [s[0] + ds[dir][0], s[1]+ds[dir][1]]
        if e[0] >= -5 and e[0] <= 5 and e[1] >= -5 and e[1] <= 5: # 맵안에있으면
            if [s,e] not in routes and [e,s] not in routes:
                routes.append([s,e])
                #print([s,e])
            s = e
            #print(routes)
    answer = len(routes)
    return answer