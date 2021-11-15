'''
3 4 5
3 2
2 2
3 1
2 3
1 1
'''
# https://www.acmicpc.net/problem/1743
import sys
from collections import deque
N,M,K = map(int,sys.stdin.readline().split())
ts = [list(map(int,sys.stdin.readline().split())) for _ in range(K)] # trashs

routes = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
#input
#동서남북
dx = [1,-1,0,0]
dy = [0,0,-1,1]
#쓰레기있는 곳 1로 표시
for t in ts:
    routes[t[0]-1][t[1]-1]=1
#####################################
#0,0넣고 쭉돌면서 최대길이 반환
q = deque()

def bfs(x,y):
    global v
    q.append([x,y])
    visited[x][y]=1
    v+=1
    while q:
        p = q.popleft()
        x,y = p[0],p[1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and routes[nx][ny]==1 and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=1
                v+=1
result = 0 #총쓰레기갯수
v = 0 # 쓰레기 갯수
for i in range(N):
    for j in range(M):
        if routes[i][j]==1: #routes 전부 돌면서
            bfs(i,j)
            result = max(result,v)
            v = 0 #다시 초기화
print(result)