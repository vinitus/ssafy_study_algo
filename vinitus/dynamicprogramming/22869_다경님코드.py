N, K = map(int, input().split())
lst = list(map(int, input().split()))
b = [1] + [0]*(N-1)
ans = 'YES'
for i in range(1, N):
    for j in range(max(0,i-K),i):
        if b[j] == 1 and (i-j) * (1+abs(lst[i]-lst[j])) <= K:
            b[i] = 1
            break
        
if b[-1] == 0:
    ans = "NO"
    
print(ans)