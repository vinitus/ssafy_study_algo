# print(ord('A'))  # 65
# print(ord('Z'))  # 90

N = int(input())  # 5
post = input()  # ABC*+DE/-
lst = [int(input()) for _ in range(N)]

dt = {}  # 알파벳 값을 저장한 dictionary
for i in range(N):
    dt[chr(65+i)] = lst[i]

# post -> dt -> new_lst
new_lst = []
ans = float(0)
for i in range(len(post)):
    if 65 <= ord(post[i]) <= 90:
        new_lst.append(dt[post[i]])
    else:
        new_lst.append(post[i])

        # 넣으면서 바로 계산
        opertor = new_lst.pop()
        right = new_lst.pop()
        left = new_lst.pop()
        if opertor == '+':
            new_lst.append(left + right)
        elif opertor == '-':
            new_lst.append(left - right)
        elif opertor == '*':
            new_lst.append(left * right)
        elif opertor == '/':
            new_lst.append(left / right)

print(f'{new_lst[0]:.2f}')
