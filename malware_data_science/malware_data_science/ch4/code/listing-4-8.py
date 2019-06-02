#!/usr/bin/python

import pefile
import sys
import argparse
import os
import pprint
import networkx
import re
from networkx.drawing.nx_agraph import write_dot
import collections
from networkx.algorithms import bipartite

args = argparse.ArgumentParser("Visualize shared hostnames between a directory of malware samples")
args.add_argument("target_path",help="directory with malware samples")
args.add_argument("output_file",help="file to write DOT file to")
args.add_argument("malware_projection",help="file to write DOT file to")
args.add_argument("hostname_projection",help="file to write DOT file to")
args = args.parse_args()
network = networkx.Graph()

valid_hostname_suffixes = map(lambda string: string.strip(), open("domain_suffixes.txt"))
valid_hostname_suffixes = set(valid_hostname_suffixes)
def find_hostnames(string):
    possible_hostnames = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', string)
    valid_hostnames = filter(
            lambda hostname: hostname.split(".")[-1].lower() in valid_hostname_suffixes,
            possible_hostnames
    )
    return valid_hostnames

# search the target directory for valid Windows PE executable files
for root,dirs,files in os.walk(args.target_path):
    for path in files:
        # try opening the file with pefile to see if it's really a PE file
        try:
            pe = pefile.PE(os.path.join(root,path))
        except pefile.PEFormatError:
            continue
        fullpath = os.path.join(root,path)
        # extract printable strings from the target sample
        strings = os.popen("strings '{0}'".format(fullpath)).read()

        # use the search_doc function in the included reg module to find hostnames
        hostnames = find_hostnames(strings)
        if len(hostnames):
            # add the nodes and edges for the bipartite network
            network.add_node(path,label=path[:32],color='black',penwidth=5,bipartite=0)
        for hostname in hostnames:
            network.add_node(hostname,label=hostname,color='blue',
               penwidth=10,bipartite=1)
            network.add_edge(hostname,path,penwidth=2)
        if hostnames:
            print "Extracted hostnames from:",path
            pprint.pprint(hostnames)
# write the dot file to disk
write_dot(network, args.output_file)
malware = set(n for n,d in network.nodes(data=True) if d['bipartite']==0)
hostname = set(network)-malware

# use NetworkX's bipartite network projection function to produce the malware
# and hostname projections
malware_network = bipartite.projected_graph(network, malware)
hostname_network = bipartite.projected_graph(network, hostname)

# write the projected networks to disk as specified by the user
write_dot(malware_network,args.malware_projection)
write_dot(hostname_network,args.hostname_projection)
