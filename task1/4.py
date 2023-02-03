from collections import defaultdict

n=int(input())
l=[int(i) for i in input().split()]
t=int(input())
d=defaultdict(int)
for i ,j in enumerate(l):
    d[j]=i
ans=(n,n)
for i,j in enumerate(l):
    if t-j in d and d[t-j]<ans[1] :
        ans=(i,d[t-j])
print(ans)
