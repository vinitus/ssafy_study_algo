def solve():
    rlt = 0
    s, r = divmod(n, 5)
    if r % 2 == 1:
        if s == 0:
            rlt = -1
            return rlt
        else:
            s -= 1
            r += 5
            rlt += s
            s, r = divmod(r, 2)
            rlt += s
    else:
        rlt += s
        s, r = divmod(r, 2)
        rlt += s
    return rlt


n = int(input())

print(solve())
