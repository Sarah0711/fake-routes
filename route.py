import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

def initialize():

	G.add_node("A")
	G.add_node("B")
	G.add_node("C")
	G.add_node("D")
	G.add_node("E")
	G.add_node("F")

	labels = {k:k for k in G.nodes()}    

	G.add_edge('A', 'F', weight=1 )
	G.add_edge('A', 'E', weight=3 )
	G.add_edge('A', 'C', weight=4 )
	G.add_edge('F', 'B', weight=3 )
	G.add_edge('F', 'E', weight=2 )
	G.add_edge('B', 'D', weight=3 )
	G.add_edge('B', 'E', weight=2 )
	G.add_edge('E', 'D', weight=4 )
	G.add_edge('E', 'C', weight=2 )
	G.add_edge('C', 'D', weight=1 )

	labels = nx.get_edge_attributes(G,'weight')
	plt.title("Single-Router Network")
	nx.draw(G,pos=nx.spectral_layout(G))
	nx.draw_networkx(G,with_labels=True,pos=nx.spectral_layout(G))
	nx.draw_networkx_edge_labels(G,pos=nx.spectral_layout(G),edge_labels=labels)
	plt.show()

def rtable():
	path = nx.all_pairs_dijkstra_path(G)
	plt.figure(1)
	plt.title("Routing Table: Hop Count & Next Hop")
	plt.axis("off")

	col_labels1 = G.nodes()
	row_labels1 = G.nodes()
	vals1 = []
	table_vals1 = []
	for node1 in G.nodes():
		for node2 in G.nodes():
			vals1.append(len(path[node1][node2])-1)
		table_vals1.append(vals1)
		vals1 = []

	the_table = plt.table(cellText = table_vals1,
	                  colWidths = [0.1]*6,
	                  rowLabels = row_labels1,
	                  colLabels = col_labels1,
	                  loc = 'upper center')
	plt.text(12,3.4,'Routing',size = 8)


	col_labels2 = G.nodes()
	row_labels2 = G.nodes()
	vals2 = []
	table_vals2 = []
	for node1 in G.nodes():
		for node2 in G.nodes():
			if node1==node2:
				vals2.append(path[node1][node2][0])
			else:
				vals2.append(path[node1][node2][1])
		table_vals2.append(vals2)
		vals2 = []

	the_table = plt.table(cellText = table_vals2,
	                  colWidths = [0.1]*6,
	                  rowLabels = row_labels1,
	                  colLabels = col_labels1,
	                  loc = 'lower center')
	plt.text(12,3.4,'Routing',size = 8)

def shortest_path(X,Y):
	b = nx.bidirectional_dijkstra(G,X,Y)
	c = G.nodes()
	d = list(set(c)-set(b[1]))
	x = G.edges()
	z = []
	a = len(b[1])
	for e in range(0,a-1):
		z.append((b[1][e+1],b[1][e]))
		z.append((b[1][e],b[1][e+1]))
	w = list(set(x)-set(z))

	labels = nx.get_edge_attributes(G,'weight')
	plt.figure(2)
	plt.title("Shortest Path Route")
	nx.draw_networkx(G,with_labels=True,pos=nx.spectral_layout(G))
	nx.draw_networkx_nodes(G,pos=nx.spectral_layout(G),nodelist=b[1],node_color='b')
	nx.draw_networkx_nodes(G,pos=nx.spectral_layout(G),nodelist=d,node_color='g')
	nx.draw_networkx_edges(G,pos=nx.spectral_layout(G),edgelist=z,edge_color='b')
	nx.draw_networkx_edges(G,pos=nx.spectral_layout(G),edgelist=w,edge_color='g')
	nx.draw_networkx_edge_labels(G,pos=nx.spectral_layout(G),edge_labels=labels)
	plt.axis("off")
	plt.show()

def router():
	s = raw_input("Enter the source node: ")
	d = raw_input("Enter the destination node: ")
	rtable()
	shortest_path(s,d)


initialize()
router()

