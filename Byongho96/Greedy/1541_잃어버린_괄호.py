# 100ms
from functools import reduce
import sys
input = sys.stdin.readline

def add(string):
    lst = string.split('+')
    result = reduce(lambda x, y: x + int(y), lst, 0)
    return result

formula = input().rstrip().split('-')   # 마이너스를 기호를 기준으로 분할하여 리스트 형성

result = add(formula[0])                # 첫번째 항은 무조건 더하고 시작
if len(formula)> 1:                     # '-'항이 하나 이상일 경우, 빼주기 시작
    for section in formula[1:]:
        result -= add(section)
print(result)
