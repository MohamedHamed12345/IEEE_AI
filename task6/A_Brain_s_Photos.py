# ﷽
#https://codeforces.com/contest/707/submission/196086883
import sys
input = lambda: sys.stdin.readline().strip()

def solve():
    n,m=[int(i) for i in input().split()]
    ans='#Black&White'
    for i in range(n):
          for j in input().split():
                if j in ['C', 'M', 'Y']:ans='#Color'
    print(ans)

    

if __name__ == "__main__":
    # for i in range(int(input())):
        solve()
