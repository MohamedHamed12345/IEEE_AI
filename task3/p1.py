from collections import Counter

# 💡here i import Counter 
# but if you don't want  to import counter you can use function   Counter below  it will do 
# the same thing 

# def Counter(it):
#     counts = {}
#     for item in it:
#         counts[item] = counts.get(item, 0) + 1
#     return counts

def get_means(l,n): return round(sum(l)/n,2)

def get_median(l,n):return round((l[n//2]+ l[-(n//2+1)])/2  ,2)

def get_mode(c):return filter(lambda x: c[x]==max(c.values()),c)   
if __name__ == "__main__":
   

    try:
        l=[float(i) for i in input().split()]
    except ValueError:
        print('invalid input')
        exit()
    print('*'*20)
    print('means: ',get_means(l,len(l)))
    print('median: ',get_median(sorted(l),len(l)))
    print('mode: ',*get_mode(Counter(l)))






''''
1 1  2 2 3 
1 3 4 10
5 8 15 7 10 22 3 1  15
8,12.32.10,3,4,4,4.4,5,12.20
'''