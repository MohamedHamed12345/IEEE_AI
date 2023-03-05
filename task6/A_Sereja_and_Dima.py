# ﷽
#https://codeforces.com/contest/381/submission/196086454
from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def solve():
    n=int(input())
    l=deque([int(i) for i in input().split()])
    a=0;b=0
    while l:
          if l[0]>l[-1]:a+=l.popleft()
          else:a+=l.pop()
          if l:
                if l[0]>l[-1]:b+=l.popleft()
                else:b+=l.pop()
          
    print(a,b)
    
    

if __name__ == "__main__":
    # for i in range(int(input())):
        solve()
