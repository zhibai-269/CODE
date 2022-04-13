import networkx as nx
#Gnutella31
G=nx.read_edgelist('Gnutella31.txt', create_using=nx.DiGraph())
G=nx.to_undirected(G)
#Grutella31
# print(G.edges())
# nx.draw(G)
# print(G.degree())
print(nx.is_connected(G))