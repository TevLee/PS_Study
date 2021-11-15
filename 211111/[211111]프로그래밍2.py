# 다익스트라
from collections import deque

def solution(N, road, K):
    nodes = {}
    dist = { i:float('inf') if i > 1 else 0 for i in range(1, N+1) }
    for s, e, d in road:
        nodes[s] = nodes.get(s, []) + [(e, d)]
        nodes[e] = nodes.get(e, []) + [(s, d)]
    que = deque([1])
    while que:
        cur_node = que.popleft()
        for nxt_node, d in nodes[cur_node]:
            if dist[nxt_node] > dist[cur_node] + d: # inf > cur까지 길이 + cur->nxt길이
                dist[nxt_node] = dist[cur_node] + d
                que.append(nxt_node)

    return len([True for dist in dist.values() if dist <= K]) # 거리가 K이하인 마을 갯수