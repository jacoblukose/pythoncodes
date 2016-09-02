#-------------------------------------------------------------------------------------------------------------------------
#bfs using adjacency matrix as raw_input
# num=input("enter the number of nodes ")
a=[]
r=0
visited=[]
q=[]

#adj matrix input
# for i in range(1,num+1):
# 	a.append(raw_input().split())
	

#nonrecursvie bfs with adjacncy matrix as input
def bfs(graph,start):
	q=[start]
	while q:
		temp=q.pop(0)
		if temp not in visited:
			visited.append(temp)
		for i in range(0,num):
			if graph[temp-1][i] == '1' and i+1 not in visited :
				q.append(i+1)

	print visited

#----------------------------------------------------------------------------------------------------------------------------

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
g={'A': ['B', 'C'],'B':['A'],'C':['A']}

#nonrecursive using adjclist
def nonrecur_bfs(graph,start,end):
	q,visited=[start],[]
	s=0
	while q:
		v=q.pop(0)
		if v not in visited:
			visited.append(v)
			q.extend(graph[v])
	
	print visited


#recursive using adjlist
visitlist=[]
def recur_bfs(graph,start):
	flag =0
	if start not in visitlist:
		visitlist.append(start)

	for neighbour in graph[start]:
		if neighbour not in visitlist:
			visitlist.append(neighbour)
			flag=1

	if flag == 1:
		for neighbour in graph[start]:
			recur_bfs(graph,neighbour) 	
		
	return visitlist


# print recur_bfs(graph,'A')
nonrecur_bfs(graph,'A','F')
# bfs(a,1)