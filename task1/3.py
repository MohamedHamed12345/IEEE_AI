from collections import defaultdict
d=defaultdict(list)
key=-1;ans=-1
for i in d:
    a=min(d[i])
    b=max(d[i])
    if b-a>ans :
       ans=b-a
       key=i
print(key)


