#from collections import defaultdict
from collections import deque
#import bisect
import sys
sys.setrecursionlimit(1 << 20)
#import heapq
N = int(input())
#s = input()
#A, B = map(int, input().split())
C = list()
P = list()
P.append([])

for i in range(N):
    c, *p = map(int, input().split())
    C.append(c)
    P.append(p)
print(P)
ans = list()
seen = set()
def dfs(v):
    cnt = 0
    for v2 in P[v]:
        if v2 in seen:
            continue
        dfs(v2)
        ans.append(v2)
        seen.add(v2)
        #print(seen)
dfs(1)
print(*ans)