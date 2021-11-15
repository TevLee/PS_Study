from collections import deque
def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    visited = [[0 for _ in range(col)] for _ in range(row)]

    def bfs(x,y):
        count = 1
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        queue = deque([[x,y,count]]) # 현재 노드 넣고
        visited[x][y] = 1 #방문
        while queue:
            x, y, count = queue.popleft()
            if x == row -1 and y == col -1 : #맵끝에 도착
                return count
            for i in range(4):
                nx , ny = x + dx[i] , y + dy[i]
                if 0 <= nx < row and 0 <= ny < col and visited[nx][ny]==0: #방문안했으면
                    if maps[nx][ny] == 1: #이동가능하면
                        queue.append([nx, ny , count+1])
                        visited[nx][ny] = 1
        return -1
    return bfs(0,0)