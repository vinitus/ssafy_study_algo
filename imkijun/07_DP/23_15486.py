import sys
sys.stdin = open('DP/input.txt','r')

# 접근법: dp문제들은 최적의 방법을 찾아야 한다는 사실을 머리속에 각인
# dp =[]를 선언하고 해당 인덱스마다 최적의 값을 저장해놓는 방식으로 크기를 확장시켜 나간다.

N = int(input())

#일자별 최대 금액 저장 리스트 선언
dp = [0] * (N+2) # N+2로 만드는 이유 - 0번째 인덱스=빈칸, 마지막 인덱스 - value값이 담기긴 하지만, 일자에 포함되지는 않는

#입력받을 날짜와 금액을 저장할 리스트 선언
day= [0]
price = [0]

#날짜와 금액을 리스트에 저장
for i in range(N):
    d, p = map(int,input().split())
    day.append(d)
    price.append(p)

#입력받은 날짜와 금액을 바탕으로, 최적의 값 저장
#핵심 포인트는, 2단계로 나눠서 진행하는것(전날 누적 + 최적의 값 여부 확인)
for i in range(1,N+2):
    # [1] 어제가 오늘보다 클 경우(최적이 값이 아닐 경우), 시작하기 전에 최적의 값(이전값)을 더해주기
    if dp[i] < dp[i-1]:
        dp[i] = dp[i-1]
        

    # [2] 기간 이내일 경우,
    if i + day[i] <= N+2:
        # day[i]일 후, 이전까지의 최적의 값(dp[i+day[i])이 현재 날짜에서 금액을 더한 것 보다 작을 때
        if dp[i+day[i]] < dp[i]+ price[i]:
            dp[i+day[i]] = dp[i]+ price[i]
            

print(max(dp))

