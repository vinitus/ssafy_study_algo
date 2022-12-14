# 우선순위 큐를 구현하기 위해서 힙 자료구조를 사용한다.
    # 힙 자료구조는 부모 노드가 자식 노드보다 작은(최소 힙) binary tree이다.
    # 힙 자료구조의 연산은 heappush, heappop이 있다.
    # 최소 힙에서 루트 노드는 항상 최솟값이 된다.
    # 최대 힙은 입력값에 -를 붙이고, 출력에 -를 붙이면 쉽게 구현할 수 있다.
# 이중 우선순위 큐는 최소 힙과 최대 힙을 동시에 사용해서 구현한다.
    # 최소 힙은 data의 최솟값을 구할 때 사용하고, 최대 힙을 data의 최댓값을 구할 때 사용한다.
    # 최소 힙과 최대 힙을 동기화시키기 위해서, visited 배열을 사용한다. 
    # 둘을 동기화시키기 위해서 id가 필요하다. 이때 id는 힙에 자료가 들어갈 때의 순서로 한다.
# 최솟값 출력 연산
    # 이미 최대 힙에서 출력된 값이 아닌지 확인한다.
    # 이미 출력된 값이라면, 다음 값도 확인한다. 
    # 출력된 값이 아니라면, 최솟값을 출력하고 연산을 마친다.
    # 최댓값 출력 연산도 마찬가지이다.
# 연산을 모두 마친 뒤 각 힙에서 지워지지 않은 쓰레기값을 처리한다.
    # visited 배열이 0이라면 최소힙, 최대힙에서 제거한다.
# 우선순위 큐 구현 완료

