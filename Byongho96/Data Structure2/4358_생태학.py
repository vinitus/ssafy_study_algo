from collections import defaultdict, Counter
import sys
input = sys.stdin.readline
# Counter 모듈 사용 296ms
trees=Counter(sys.stdin.read().split('\n')[:-1])

N=sum(list(trees.values()))

for key in sorted(trees.keys()):
    print(key,"%.4f"%(trees[key]/N*100))

################################################################################
# 모듈 사용 없이
# 572ms
trees = {}
num_tree = 0
while True:
    tree = input().rstrip()
    if not tree:            # 입력값이 없으면 종료
        break
    if tree in trees:       # trees = collections.defaultdict(int); trees[tree] += 1 대체 가능
        trees[tree] += 1
    else:
        trees[tree] = 1
    num_tree += 1

tree_lst =list(trees.items())   #[(name, num), ...]
tree_lst.sort()
for name, num in tree_lst:
    print(f'{name} {num/num_tree*100:.4f}')
    
###################################################################################
# 내 원래 풀이: 이중 dict 사용. 시간이점 없음
# 672ms
# 계속 입력 받기
lines = sys.stdin.readlines()   # cmd창에서 종료시에는 Ctrl + 'D'

cnt_tt = 0      # 총 나무 갯수
tree_dic = {}   # {'A' : {'Ash': 2, 'Aspen':3, }} dict in dict 구조

for name in lines:
    name = name.rstrip()
    cnt_tt += 1

    if not name[0] in tree_dic:             # 해당 알파벳이 안나왔다면
        tree_dic[name[0]] = defaultdict(int)    # 나무의 갯수를 카운팅하기 위해 defaultdict(0) 생성
    tree_dic[name[0]][name] += 1            # 알파벳에 대응하는 2차 dict에서 카운팅
                                            # {'A' : {'Ash': 2, 'Aspen':3, }}

lst = []
for name_num in tree_dic.values():          # {'Ash': 2, 'Aspen':3, } 값만 추출
    lst.extend(list(name_num.items()))          # [('Ash', 2), ('Aspen', 3)] 형태 변환 후 lst에 extend

lst.sort()                                  # 이름 순으로 정렬
for name, num in lst:                       # 프린트
    print(f'{name} {num/cnt_tt*100:.4f}')