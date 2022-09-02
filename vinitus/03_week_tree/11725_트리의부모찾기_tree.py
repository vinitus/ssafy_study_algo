import sys
def input():
    return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, data, left = None, rigth = None):
        self.data = data
        self.left = left
        self.rigth = rigth


N = int(input())

