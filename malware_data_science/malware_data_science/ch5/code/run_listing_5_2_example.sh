#!/bin/bash

# load the APT1 dataset into the sample similarity search engine and search for a sample's nearest neighbors
python listing_5_2.py -l ../data
python listing_5_2.py -s ../data/APT1_MALWARE_FAMILIES/GREENCAT/GREENCAT_sample/GREENCAT_sample_AB208F0B517BA9850F1551C9555B5313
