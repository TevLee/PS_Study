#19:25 - 19:38 (60점)
#19:45 - 19:56
def solution(n,a,b):
    answer =  0
    if a>b : a,b = b,a
    while a!=b:
        a = a//2 if a%2==0 else (a+1)//2
        b = b//2 if b%2==0 else (b+1)//2
        answer+=1
    return answer