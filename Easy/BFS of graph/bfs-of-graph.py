from typing import List
from queue import Queue
from collections import deque

class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = []
        q = deque()
        q.append(0)
        visited.append(0)
        while q:
            s = q.popleft()
            for u in adj[s]:
                if u not in visited:
                    visited.append(u)
                    q.append(u)
                    
        return visited;


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends