#19:00 - 19:07
from itertools import combinations
def isPrime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else :
        return True
def solution(nums):
    answer = 0
    coms = list(combinations(nums,3))
    for com in coms:
        num = sum(com)
        if isPrime(num) :
            print(num, com)
            answer+=1
    return answer