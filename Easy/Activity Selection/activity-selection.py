#User function Template for python3
from heapq import heappop, heappush
class Solution:
    # def activitySelection(self, n, s, f):
    #     ans = []
    #     p = []
 
    #     for i, j in zip(s, f):
    #         heappush(p, (j, i))
 
    #     it = heappop(p)
    #     start = it[1]
    #     end = it[0]
    #     ans.append(it)
    #     while p:
    #         it = heappop(p)
    #         if it[1] >= end:
    #             start = it[1]
    #             end = it[0]
    #             ans.append(it)
 
    #     return ans
    def activitySelection(self,n,start,end):
        n=len(end)
        arr=[]
        for i in range(n):
            k=[start[i],end[i]]
            arr.append(k)
        arr.sort(key=lambda x:x[1])
        i=0
        p=1
        for j in range(1,n):
            if arr[j][0]>arr[i][1]:
                p+=1
                i=j
        return p
 
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends