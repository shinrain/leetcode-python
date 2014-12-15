class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node==None:
            return None
        st = [node]
        map={}
        map[node]= UndirectedGraphNode(node.label)

        while len(st)!=0:
        	cur = st.pop()
        	cp = map[cur]
        	for nd in cur.neighbors:
        		if nd not in map:
        			nd_cp = UndirectedGraphNode(nd.label)
        			cp.neighbors.append(nd_cp)
        			map[nd]=nd_cp
        			st.append(nd)
        		else:
        			cp.neighbors.append(map[nd])
        return map[node]
