T = int(input())

for _ in range(T):
    N = int(input())
    # lst는 자식의 부모 정보를 담은 lst
    lst = [0] * (N + 1)     # index 서칭 편의상 +1
    for _ in range(N - 1):
        parent, child = map(int, input().split())
        lst[child] = parent
    
    A, B = map(int, input().split())
    # lst 자체가 값 자체로 인덱싱하기 위해서 +1을 해줬기 때문에 0을 넣어줘야함
    A_lst, B_lst = [0, A], [0, B]
    while lst[A]:
        A_lst.append(lst[A])
        A = lst[A]          # 계속 트리를 타고 올라감
    while lst[B]:
        B_lst.append(lst[B])
        B = lst[B]
        
    idx = 1
    while A_lst[-idx] == B_lst[-idx]:
        idx += 1
        
    print(A_lst[-idx + 1])