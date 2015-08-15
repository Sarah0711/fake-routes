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

	subnodelist = ["A","B","C","D","E","F"]
	labels = {k:k for k in subnodelist}    

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
	nx.draw(G,pos=nx.spectral_layout(G))
	nx.draw_networkx(G,with_labels=True,pos=nx.spectral_layout(G))
	nx.draw_networkx_edge_labels(G,pos=nx.spectral_layout(G),edge_labels=labels)
	plt.show()

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
	shortest_path(s,d)


initialize()
router()

