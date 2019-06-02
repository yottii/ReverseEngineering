#!/usr/bin/python
import networkx

# Instantiate a network with no nodes and no edges.
network = networkx.Graph()

nodes = ["hello","world",1,2,3]
for node in nodes:
    network.add_node(node)
network.add_edge("hello","world")
network.add_edge(1,2)
network.add_edge(1,3)
network.add_node(1,myattribute="foo")
network.node[1]["myattribute"] = "foo"
print network.node[1]["myattribute"] # prints "foo"
network.add_edge("node1","node2",myattribute="attribute of an edge")
network.get_edge_data("node1","node2")["myattribute"] = "attribute of an edge"
network.get_edge_data("node1","node2")["myattribute"] = 321
print network.get_edge_data("node1","node2")["myattribute"] # prints 321
