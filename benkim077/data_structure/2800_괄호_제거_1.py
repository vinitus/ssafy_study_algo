# 인덱스 저장을 위해서 enumerate 사용
data = list(enumerate(input()))  # (2+(2*2)+2)

# 괄호의 짝을 찾은 과정
stack = []
sett = []  # 괄호의 짝을 sett
for idx, value in data:
    if value == '(':
        stack.append((idx, value))  # 시작 인덱스와 값을 저장
    elif value == ')':  
        # if stack[-1][1] == '(':
        # '('와 ')'를 연결
        sett.append((stack[-1][0], idx))  # (, ) 쌍 인덱스값을 저장
        stack.pop()
    else:
        pass

# 괄호 짝에 대한 부분집합을 찾는 과정
print_lst = []
n = len(sett)
for bit in range(1, 2**n):
    subset = []
    for i in range(n):
        if bit & (1<<i):
            subset.append(i)  # 부분집합(subset)을 찾았다.

    # 부분집합에 대한 괄호 위치를 파악한다.
    ans_lst = []
    for i in range(len(subset)):
        ans_lst.append(sett[subset[i]][0])
        ans_lst.append(sett[subset[i]][1])
    
    # 괄호 위치를 저장한 리스트를 역순으로 정렬
    ans_lst.sort(reverse=True)

    # 카피한 data에서 부분집합을 뺀다. pop()
    ans = data[:]
    for i in range(len(ans_lst)):
        ans.pop(ans_lst[i])
    
    # 뺀 결과를 출력 리스트에 옮긴다.
    temp = ''
    for i in range(len(ans)):
        temp += ans[i][1]
    print_lst.append(temp)

# 중복 제거  (((1)))(2)
print_lst = list(set(print_lst))

# 사전순으로 정렬 후 출력
print_lst.sort()
for i in range(len(print_lst)):
    print(print_lst[i])
