#User function Template for python3

class Solution:  
    def FindMaxSum(self,arr, n):
        if n <= 2:
	        return max(arr)
	    arr[2] += arr[0]
	    for i in range(3,n):
	        arr[i] += max(arr[i-2], arr[i-3])
	    return max(arr[-2:])


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends