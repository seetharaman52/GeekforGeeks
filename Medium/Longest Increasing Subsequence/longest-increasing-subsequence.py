#User function Template for python3

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        lis = [1]*(n) # --> Integer * n = size of List
        for i in range(n):
            for j in range(i):
                if a[i] > a[j] and lis[i] <= lis[j]:
                    lis[i] = 1 + lis[j]
        return max(lis)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends