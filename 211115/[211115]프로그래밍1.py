# 19:09 - 19:17 (실패2개)
# 19:18 - 19:23 (효율성실패)
# 19:42 - 19:46
def solution(no, works):
    for _ in range(no):
        works.sort()
        if works[-1]!=0:
            works[-1]-=1
    return sum([i**2 for i in works])