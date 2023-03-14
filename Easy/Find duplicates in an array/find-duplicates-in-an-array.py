class Solution:
    def duplicates(self, arr, n): 
    	
    	dic = {}
        ans = []
        for i in range(n):
            dic[i]=0
        
        for i in range(n):
            dic[arr[i]]+=1
        
        for key in range(n):
            if dic[key]>1:
                ans.append(key)
        
        return ans if ans else [-1]


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends