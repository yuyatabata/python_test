import sys
sys.setrecursionlimit(10**8)
#input=sys.stdin.readline  #危険！基本オフにしろ！

n=int(input())
a=[int(x) for x in sys.stdin.readline().split()]


def solve(n,a):
    return (min(abs(sum(a[:i])-sum(a[i:]))for i in range(n)))

