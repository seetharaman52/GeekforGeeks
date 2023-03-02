#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
	    if n <= 2:
	        return max(arr)
	    arr[2] += arr[0]
	    for i in range(3,n):
	        arr[i] += max(arr[i-2], arr[i-3])
	    return max(arr[-2:])


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends