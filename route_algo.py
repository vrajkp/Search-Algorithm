import heapq
import sys


#take input from the users
#Source file
input_file = sys.argv[1]
#source city
start_city = sys.argv[2]
#dest city
End_city = sys.argv[3]
#heuristic file
heuristic_file_file = sys.argv[4]
#algo for finding route
algo_type = sys.argv[5] 


#method for informed search
def A_star(graph, s, goal, h):
	#variable declarations

	#queue for fringe
	queue_node = []
	#previously visited nodes
	visited_nodes = {}
	#last node visited
	previous_nodes = {}	
	#heuristic value
	h_value=0
	#temp variable
	temp=0
	#count for expanded nodes
	count = 0

	# heap for queue
	heapq.heappush(queue_node,(0,s,None,0))
	for nodes in graph:
		# intialize visited nodes and previous nodes false and change their values 
		visited_nodes[nodes] = False
		previous_nodes[nodes] = None
	d_track=0
	i = 1
	while len(queue_node) != 0:
		# Keeping track of total cost
		list2 = []
		for k in queue_node:
			list2.append(k[0])
			list2.sort()

		#print(list2)
		# Keeping fringe
		list4 = []
		for k in list2:
			for j in queue_node:
				if(k == j[0]):
					list4.append(j)
		queue_node = list4
		count = count + 1
		i = i+1
		d_track= d_track+1
		#print(queue_node)
		# pop the least cost node from heap and analyse it
		
		total_cost, current_node, prev_node, link_cost = heapq.heappop(queue_node)
		if visited_nodes[current_node] == False:
			visited_nodes[current_node] = True
			previous_nodes[current_node] = []
			previous_nodes[current_node].append(prev_node)
			previous_nodes[current_node].append(link_cost)
			
			# if goal return the total route
			if current_node == goal:
				final = []
				while current_node != s:
					temp = []
					temp.append(current_node)
					for i in previous_nodes[current_node]:
						temp.append(i)
					final.append(temp)
					current_node = previous_nodes[current_node][0]
					
				final.reverse()
				d_track = d_track + 1
				return total_cost,final,count
			# Check New Nodes
			for neighbors, path_cost in graph[current_node].items():
					if h != "":
						for rec in h:
							if((rec[0].find(current_node) != -1) & (d_track > 1)):
							#print("current: ABC ",rec,"",d_track)
								h_value=rec[1]
							if(rec[0].find(neighbors)!=-1):
								temp=rec[1]
						
					new_cost = total_cost + path_cost + int(temp) - int(h_value)
					heapq.heappush(queue_node, (new_cost, neighbors, current_node, path_cost))
					
					
	# return none if no path found
	return count

def UCS(graph, s, goal):
	
	# define dummy variables for use
	#queue for fringe
	queue_node = []
	#previously visited nodes
	visited_nodes = {}
	#last node visited
	previous_nodes = {}
	#Counting expanded nodes
	count = 0
	# using heap for mainitng a queue
	heapq.heappush(queue_node,(0,s,None,0))
	for nodes in graph:
		visited_nodes[nodes] = False
		previous_nodes[nodes] = None
	i = 1
	count = 0
	# mark all visited and previous nodes False and None
	while len(queue_node) != 0:
		count = count + 1
		# pop the least cost node from heap and analyse it
		i = i+1
		total_cost, current_node, prev_node, link_cost = heapq.heappop(queue_node)
		if visited_nodes[current_node] == False:
			visited_nodes[current_node] = True
			previous_nodes[current_node] = []
			previous_nodes[current_node].append(prev_node)
			previous_nodes[current_node].append(link_cost)
			
			# if goal return the total route
			if current_node == goal:
				final = []
				while current_node != s:
					temp = []
					temp.append(current_node)
					for i in previous_nodes[current_node]:
						temp.append(i)
					final.append(temp)
					current_node = previous_nodes[current_node][0]
					
				final.reverse()
				# retrn total cost and final path
				return total_cost,final,count
			# else explore neighbours
			for neighbors, path_cost in graph[current_node].items():
					new_cost = total_cost + path_cost
					heapq.heappush(queue_node, (new_cost, neighbors, current_node, path_cost))
					
	# return none if no path found
	return count

def main(file, arg1, arg2,arg4,arg5):
	# open file and make data ready for analysis
	file = open(input_file, 'r')
	filedata = file.readlines()
	# make a dictionary of graph
	filedata = [x.strip().split() for x in filedata]
	# if end of file then remove the last line
	if filedata[-1:][0][0] == 'END':
		filedata.pop()

	#open heuristic_file_file file and make data ready for analysis 
	file = open(heuristic_file_file, 'r')
	heuristic_file_filedata = file.readlines()
	# make a dictionary of heuristic_file_file 
	heuristic_file_filedata = [x.strip().split() for x in heuristic_file_filedata]
	# if end of file then remove the last line
	if heuristic_file_filedata[-1:][0][0] == 'END':
		heuristic_file_filedata.pop()

	# empty graph
	G = {}
	for rec in filedata:
		src = rec[0]
		dest = rec[1]
		cst = rec[2]
		if src not in G:
			G[src] = {}
		if dest not in G:
			G[dest] = {}
		# create src and dest nodes with its length from input file
		G[src][dest] = int(cst)
		G[dest][src] = int(cst)

	# This will call method for informed search
	if algo_type == "inf":
		inf = A_star(G,start_city,End_city,heuristic_file_filedata)
		print ("\n-----------------Final output-----------------\n")
		nodes = "nodes expanded: "
		distance = "distance: "
		# If there is no path between two nodes
		if isinstance(inf,int):
			print("%s%i"%(nodes,inf))
			print("distance: infinity")
			print("route: \nNone")
		# If there is path between two nodes	
		else:
			print("%s%i"%(nodes,inf[2]))
			print("%s%i km"%(distance,inf[0]))
			print("route:\nNone ")
			for line in inf[1]:
				print ("%s to %s, %s km" % (line[1],line[0],line[2]))
			
	# This will call method for uninformed search		
	else:
		uninf = UCS(G,start_city,End_city)
		print ("\n-----------------Final output-----------------\n")
		nodes = "nodes expanded: "
		distance = "distance: "
		# If there is no path between two nodes
		if isinstance(uninf,int):
			print("%s%i"%(nodes,uninf))
			print("distance: infinity")
			print("route: \n None")
		# If there is path between two nodes		
		else:
			print("%s%i"%(nodes,uninf[2]))
			print("%s%i km"%(distance,uninf[0]))
			print("route: \nNone")
			for line in uninf[1]:
				print ("%s to %s, %s km" % (line[1],line[0],line[2]))
			
	pass
#Main method
main(input_file,start_city,End_city,heuristic_file_file,algo_type)
