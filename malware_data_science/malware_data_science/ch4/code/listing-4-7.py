#!/usr/bin/python

import networkx
from networkx.drawing.nx_agraph import write_dot

g = networkx.Graph()
g.add_node(1,label="first node")
g.add_node(2,label="second node")
g.add_edge(1,2,label="link between first and second node")

write_dot(g,'network.dot')


