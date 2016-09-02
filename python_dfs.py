


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}



visited=[]
q=[]


def dfs_search(graph,start):
		
	q.append(start)
	temp = q.pop(0)
	print temp,
	if temp not in visited:
		visited.append(temp)

	for child in graph[temp]:
		if child not in visited:
			visited.append(temp)
			dfs_search(graph,child)




dfs_search(graph,'A')