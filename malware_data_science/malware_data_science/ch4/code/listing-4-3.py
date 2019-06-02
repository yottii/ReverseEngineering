#!/usr/bin/python
import networkx
from networkx.drawing.nx_agraph import write_dot

# instantiate a network, add some nodes, and connect them
nodes = ["hello","world",1,2,3]
network = networkx.Graph()
for node in nodes:
    network.add_node(node)
network.add_edge("hello","world")
write_dot(network, "network.dot")

