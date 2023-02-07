from bisect import bisect_left, bisect_right


l=[int(i) for i in input().split()]
t=int(input())
l=sorted(l)
i=bisect_left(l,t)
j=bisect_right(l,t)-1

print(i,j)

'''
1 4 5 4 4 1 2 3
4
'''