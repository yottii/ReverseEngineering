#!/usr/bin/python

import networkx
from networkx.drawing.nx_agraph import write_dot

g = networkx.Graph()
g.add_node(1,color="blue") # make the node outline blue
g.add_node(2,color="pink") # make the node outline pink
g.add_edge(1,2,color="red") # make the edge  red
write_dot(g,'network.dot')



