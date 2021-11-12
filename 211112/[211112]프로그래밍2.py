# 19:00 - 19:03 (효율성 1,3 실패)
# 19:41 - 19:45
def solution(arr):
    answer = True
    dp = [0]*(max(arr)+1)
    for n in arr:
        dp[n]=1
    if dp[1:len(arr)+1].count(1) != len(arr):
        answer=False
    return answer