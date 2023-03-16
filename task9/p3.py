from collections import defaultdict


class Solution:
    def numUniqueEmails(self, l) -> int:
        d=defaultdict(set)
        for elemnt in l:
            a,b=elemnt.split('@')
            a=a.split('+')[0].replace('.','')
            d[b].add(a)

        return sum([len(d[i]) for i in d])