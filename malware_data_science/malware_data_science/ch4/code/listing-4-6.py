#!/usr/bin/python

import networkx
from networkx.drawing.nx_agraph import write_dot

g = networkx.Graph()
g.add_node(1,shape='diamond')
g.add_node(2,shape='egg')
g.add_edge(1,2)

write_dot(g,'network.dot')


