# Listed List 구현
from ast import Delete


class Node:
    def __init__(self, data, nxt):
        self.data = data
        self.nxt = nxt

# 어떤 연결 리스트를 만들지?
# 1 -> 2 -> 3 -> 4 -> 5

# 노드 생성

node1 = Node(1, None)   # node1 생성
head = node1
node2 = Node(2, None)   # node2 생성

# 노드 연결
node1.nxt = node2       # node1, node2 연결

# 노드 추가 및 연결
node4 = Node(4, None)
node2.nxt = node4       # n1 -> n2 -> n4

# 노드 삽입
node3 = Node(3, None)
node2.nxt = node3
node3.nxt = node4   # n1 -> n2 -> n3 -> n4


# 노드 삭제
# 값이 2인 노드를 삭제해라
cur = head
while True:
    if cur.nxt.data == 2:
        tobedeleted = cur.nxt   # 삭제해야 할 노드
        cur.nxt = cur.nxt.nxt
        del tobedeleted
        break
    else:
        cur = cur.nxt


# 연결 리스트 출력하기
temp = node1
print(temp.data, end='>')
while temp.nxt != None:
    temp = temp.nxt
    print(temp.data, end='>')
else:
    print(temp.nxt)
print()



