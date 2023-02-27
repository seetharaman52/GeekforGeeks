class Solution:
    def dfsOfGraph(self, V, adj):
        visited = []
        def dfs(currnode):
            if currnode not in visited:
                visited.append(currnode)
                for u in adj[currnode]:
                    dfs(u)
        dfs(0)
        return visited


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends