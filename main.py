def helper(self,adj,visited,curr,par):
        visited[curr] = 1
        neg = adj[curr]
        for j in range(len(adj[curr])):
            if visited[neg[j]]==0:
                flag = self.helper(adj,visited,neg[j],curr)
                if flag == 1:
                    return 1
            elif neg[j] != par:
                return 1
        return 0
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
	    visited= [0]*V
	    for i in range(V):
	        if visited[i]==0:
	            flag = self.helper(adj,visited,i,-1)
	            if flag ==1:
	                return 1
	    return 0
