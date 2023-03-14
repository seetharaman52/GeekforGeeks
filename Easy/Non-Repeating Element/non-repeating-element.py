class Solution:
    def firstNonRepeating(self, arr, n):
        
        hashmap = {}

        for i in arr:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] =1
        for i in arr:
            if hashmap[i]<2:
                return i
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends