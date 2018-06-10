N, W = map(int, input().split())    # n: 物の個数 w: 重さの限界

def p(dp):
    for i in dp:
        print(i)


weight = [0]*N
value = [0]*N

dp = [[0 for i in range(W+1)] for j in range(N+1)]

for i in range(N):
    value[i], weight[i] = map(int, input().split())
print(value, weight)

# DPループ
for i in range(N):
    for w in range(W+1):
        print(w, weight[i])
        if(weight[i] <= w):
            dp[i+1][w] = max(dp[i][w-weight[i]] + value[i], dp[i][w])
            p(dp)
        else:
            dp[i+1][w] = dp[i][w]
            p(dp)

print(dp[N][W])
