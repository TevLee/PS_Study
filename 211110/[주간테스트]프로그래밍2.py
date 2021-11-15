# 14:03 - 14:06
def solution(arr): # 0 - 9
    answer = [arr[0]]
    arr = arr[1:]
    for n in arr:
        if n != answer[-1]:
            answer.append(n)
    return answer