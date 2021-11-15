# 14:06 - 14:15
def solution(nums): #항상짝수
    max = len(nums)//2
    answer = max if len(set(nums)) > max else len(set(nums))
    return answer