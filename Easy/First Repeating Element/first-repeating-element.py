#User function Template for python3

class Solution:
    def firstRepeated(self,arr, n):
        x = len(set(arr))
        if x == n:
            return -1
        else:
            for i in arr:
                x = arr.count(i)
                if x > 1:
                    return arr.index(i) + 1
                else:
                    pass

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends