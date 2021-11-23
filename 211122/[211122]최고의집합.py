def solution(n, s):
    answer = []
    if s // n < 1: return [-1]

    item = s // n
    for i in range(n):
        answer.append(item)
    if s % n != 0:
        left = s % n
        for i in range(1, left + 1):
            answer[-i] += 1

    return answer