import sys
def input():
    return sys.stdin.readline().rstrip()

villiage = []
population = 0

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    villiage.append([a, b])
    population += b

villiage.sort(key= lambda x: x[0])

count = 0
for i in range(N):
    count += villiage[i][1]
    if count >= population/2:
        print (villiage[i][0])
        break