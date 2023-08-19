from collections import defaultdict as dd
from collections import deque
#import bisect
#import sys
#sys.setrecursionlimit(1 << 20)
#import heapq
N = int(input())

cnt = dd(list)
que = list()

for i in range(N):
    f, s = map(int, input().split())
    cnt[f].append(s)
    #que.append([s,f])

for key in cnt.keys():
    cnt[key].sort()
ans = 0
for key in cnt.keys():
    if len(cnt[key]) >= 2:
        num = cnt[key][-1] + cnt[key][-2]//2
        ans = max(ans, num)
    if cnt[key]:
        que.append([cnt[key][-1], key])
que.sort(reverse=True)
que = deque(que)
n = len(que)
v = que.popleft()
for i in range(n-1):
    v2 = que.popleft()
    if v[1] == v2[1]:
        num = v[0] + v2[1]//2
        ans = max(ans, num)
        v = v2
    else:
        num = v[0] + v2[0]
        ans = max(ans, num)
        v = v2
print(ans)