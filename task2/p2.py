l=[int(i) for i in input().split()]
cnt=len(list(filter(lambda x:x%2==0,l)))
print(cnt)