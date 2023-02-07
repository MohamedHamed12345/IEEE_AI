from bisect import bisect_left

try :
    l=[int(i) for i in input().split()]
except :
    print("invalid input")
    exit()
if len(l)<2:
    print("length list is too short it should be at least 2")
    exit()

l=sorted(l)
idx=bisect_left(l,0)
l1=l[:max(idx,2)]
l2=l[min(idx+1,len(l)-2):]
print(l2)
print(l1)


# -8 -7 -3 -2 -1 5
# -8 7 3 2 1 5
# -3 -2 -1 -8 7 3 2 1 5