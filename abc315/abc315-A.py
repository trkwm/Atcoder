#from collections import defaultdict
#from collections import deque
#import bisect
#import sys
#sys.setrecursionlimit(1 << 20)
#import heapq
#N = int(input())
s = input()
#A, B = map(int, input().split())
#P = list(map(int, input().split()))

dis = [ "a","e","i", "o", "u"]
ans = ""
for i in range(len(s)):
    if s[i] in dis:
        pass
    else:
        ans += s[i]
print(ans)