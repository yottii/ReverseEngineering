#!/usr/bin/python

import networkx
from networkx.drawing.nx_agraph import write_dot

g = networkx.Graph()
g.add_node(1)
g.add_node(2)
g.add_edge(1,2,penwidth=10) # make the edge extra wide
write_dot(g,'network.dot')



