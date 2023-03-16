class Solution:
    def replaceElements(self, arr):
        tmp=-1
        for i in range(len(arr)-1,-1,-1):
            element=arr[i]
            arr[i]=tmp
            tmp=max(tmp,element)
        return arr