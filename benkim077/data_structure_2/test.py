from heapq import heappush, heappop

# 최소 힙과 최대 힙은 반대인가?

mn_h = list()
mx_h = list()


input_list = [16, -5643, 123, -45, 653, -642, 45, 97, 333]
for element in input_list:
    heappush(mn_h, element)
    heappush(mx_h, -element)

print(mn_h)
print(mx_h)
print(mn_h[::-1] == mx_h)
# 아니다. 힙은 부모 노드가 자식 노드보다 작다(크다)를 보장할 뿐이다.