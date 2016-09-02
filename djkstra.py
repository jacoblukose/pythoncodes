
# graph = {'A': ['B', 'C'],
#          'B': ['A', 'D', 'E'],
#          'C': ['A', 'F'],
#          'D': ['B'],
#          'E': ['B', 'F'],
#          'F': ['C', 'E']}

# g={'A': ['B', 'C'],'B':['A'],'C':['A']}

finalans=[]

#nonrecursive using adjclist
def nonrecur_bfs(graph,start,no):
	dist={}

	for ele in graph:
		dist[ele]=-1

	q=[start]
	s=0
	dist[start]=0
	while q:
		v=q.pop(0)
		for ele in graph[v]:
			if dist[ele] == -1:
				dist[ele] = dist[v]+6
				q.append(ele)
	temp=[]
	for k in dist:
		if k != start:
			temp.append(dist[k])
	finalans.append(temp)


testcase=input()
for testno in range(0,testcase):
	graph={}
	nodes,edges=map(int,raw_input().split(" "))
	for i in range(0,edges):
		edge_points=map(int,raw_input().split(" "))

		if edge_points[0] not in graph.keys():
			graph[edge_points[0]]=[edge_points[1]]
		else:
			graph[edge_points[0]].append(edge_points[1])

		if edge_points[1] not in graph.keys():
			graph[edge_points[1]]=[edge_points[0]]
		else:
			graph[edge_points[1]].append(edge_points[0])

	start=input()

	for j in range(1,nodes+1):
		if j not in graph.keys():
			graph[j]=[]

	nonrecur_bfs(graph,start,testno)


for eachans in finalans:
	for i in eachans:
		print i,
	print ""