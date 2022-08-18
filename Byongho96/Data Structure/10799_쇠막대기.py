import sys
input = sys.stdin.readline

parenthesis = input().rstrip()
# 다른사람 답안 참조 arrangement.replace('()', '0');

pipe = 1    # 시작은 항상 '('
cut = 0
for i in range(1, len(parenthesis)):
    if parenthesis[i] == '(':
        pipe += 1
    else:
        if parenthesis[i-1] == '(':
            pipe -= 1
            cut += pipe
        else:
            pipe -= 1
            cut += 1
print(cut)
