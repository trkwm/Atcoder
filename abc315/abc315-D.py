#from collections import defaultdict
#from collections import deque
#import bisect
#import sys
#sys.setrecursionlimit(1 << 20)
#import heapq

H, W = map(int, input().split())
c = [ list(input()) for _ in range(H) ]

while True:
    temph = False;tempw = False
    remh = list()
    remw = list()
    for i in range(H):
        key = c[i][0]
        cnt = 0
        for j in range(W):
            if c[i][j] == key:
                cnt += 1
        if cnt == W:
            remh.append(i)
            temph = True
    for i in range(W):
        cnt = 0
        for j in range(H):
            if c[j][i] == key:
                cnt += 1
        if cnt == H:
            remw.append(i)
            tempw = True
    #print(remh)
    #print(remw)
    if H < 2 or W < 2:
        print(H*W)
        break
    else:
        temp = list()
        temph = list()
        for i in range(H):
            tempw = list()
            for j in range(W):
                if j in remw:
                    continue
                else:
                    tempw.append(c[i][j])
            temph.append(tempw)
        #print(temph)
        for i in range(H):
            if i in remh:
                continue
            else:
                temp.append(temph[i])
        if temph:
            H -= len(remh)
        if tempw:
            W -= len(remw)
        c = temp.copy()
        #print(c)