dp = [True]*10001
for i in range(1,10001):
    tmp = i
    while i>0:
        tmp += i%10
        i = i//10
    if tmp<=10000:
        dp[tmp]=False
for j in range(1,10001):
    if dp[j]==True:
        print(j)