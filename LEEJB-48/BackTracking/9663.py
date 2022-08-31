import sys


def input():
    return sys.stdin.readline().rstrip()


def n_queen(row, sero, diag1, diag2, n):
    global answer
    if row == n:
        answer += 1
        return None
    for column in range(n):
        if not sero[column] and not diag1[row - column + n - 1] and not diag2[row + column]:
            tmp_sero, tmp_diag1, tmp_diag2 = sero[:], diag1[:], diag2[:]
            tmp_sero[column], tmp_diag1[row - column + n - 1], tmp_diag2[row + column] = 1, 1, 1
            n_queen(row + 1, tmp_sero, tmp_diag1, tmp_diag2, n)
    return None


def solution(n):
    global answer
    answer = 0
    n_queen(0, [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1), n)
    return answer


print(solution(int(input())))
