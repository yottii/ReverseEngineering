#!/bin/bash
python listing_5_1.py ../data similarity_graph.dot
fdp -Tpng -o similarity_graph.png similarity_graph.dot
