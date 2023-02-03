l=[int(i) for i in input().split()]
val=int(input())
val=min(val,len(l))
l=l[-val:][::-1]+l[:-val]
print(l)