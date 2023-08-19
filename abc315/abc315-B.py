#from collections import defaultdict
#from collections import deque
#import bisect
#import sys
#sys.setrecursionlimit(1 << 20)
#import heapq
M = int(input())
#s = input()
#A, B = map(int, input().split())
D = list(map(int, input().split()))
import math
s = sum(D)
s /= 2
s = math.ceil(s)

for i in range(M):
    if s > D[i]:
        s -= D[i]
    else:
        print(i+1, s)
        exit()