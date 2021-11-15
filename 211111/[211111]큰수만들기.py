def solution(number, k):
    answer = ''
    stack = []
    stack.append(number[0])
    #
    for i in number[1:]:
        while len(stack)>0 and k>0 and stack[-1] < i : #스택에 있는수가 더 작고 k남아있으면 하나씩 줄이면서 스택에 바꾸기
            k-=1
            stack.pop()
        stack.append(i)
    if k>0 :
        stack = stack[:-k]
    #print(stack)
    answer = "".join(stack)
    return answer