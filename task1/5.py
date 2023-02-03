from collections import deque


l=list(input().split())
d1=deque()
d2=deque()
for i in l:
    d1.append(i[:(len(i)+1)//2])
    d2.append(i[(len(i)+1)//2:])
print(list(d1))
print(list(d2))