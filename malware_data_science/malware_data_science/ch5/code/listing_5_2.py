#!/usr/bin/python

import argparse
import os
import murmur
import shelve
import sys
from numpy import *
from listing_5_1 import *

"""
Copyright (c) 2015, Joshua Saxe
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name 'Joshua Saxe' nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL JOSHUA SAXE BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


NUM_MINHASHES = 256
NUM_SKETCHES = 8

def wipe_database():
    """
    This problem uses the python standard library 'shelve' database to persist
    information, storing the database in the file 'samples.db' in the same
    directory as the actual Python script.  'wipe_database' deletes this file
    effectively reseting the system.
    """
    dbpath = "/".join(__file__.split('/')[:-1] + ['samples.db'])
    os.system("rm -f {0}".format(dbpath))

def get_database():
    """
    Helper function to retrieve the 'shelve' database, which is a simple
    key value store.
    """
    dbpath = "/".join(__file__.split('/')[:-1] + ['samples.db'])
    return shelve.open(dbpath,protocol=2,writeback=True)

def minhash(attributes):
    """
    This is where the minhash magic happens, computing both the minhashes of
    a sample's attributes and the sketches of those minhashes.  The number of
    minhashes and sketches computed is controlled by the NUM_MINHASHES and
    NUM_SKETCHES global variables declared at the top of the script.
    """
    minhashes = []
    sketches = []
    for i in range(NUM_MINHASHES):
        minhashes.append(
            min([murmur.string_hash(`attribute`,i) for attribute in attributes])
        )
    for i in xrange(0,NUM_MINHASHES,NUM_SKETCHES):
        sketch = murmur.string_hash(`minhashes[i:i+NUM_SKETCHES]`)
        sketches.append(sketch)
    return array(minhashes),sketches

def store_sample(path):
    """
    Function that stores a sample and its minhashes and sketches in the
    'shelve' database
    """
    db = get_database()
    attributes = getstrings(path)
    minhashes,sketches = minhash(attributes)

    for sketch in sketches:
        sketch = str(sketch)
        if not sketch in db:
            db[sketch] = set([path])
        else:
            obj = db[sketch]
            obj.add(path)
            db[sketch] = obj
        db[path] = {'minhashes':minhashes,'comments':[]}
        db.sync()

    print "Extracted {0} attributes from {1} ...".format(len(attributes),path)

def comment_sample(path):
    """
    Function that allows a user to comment on a sample.  The comment the
    user provides shows up whenever this sample is seen in a list of similar
    samples to some new samples, allowing the user to reuse her or his
    knowledge about their malware database.
    """
    db = get_database()
    comment = raw_input("Enter your comment:")
    if not path in db:
        store_sample(path)
    comments = db[path]['comments']
    comments.append(comment)
    db[path]['comments'] = comments
    db.sync()
    print "Stored comment:",comment

def search_sample(path):
    """
    Function searches for samples similar to the sample provided by the
    'path' argument, listing their comments, filenames, and similarity values
    """
    db = get_database()
    attributes = getstrings(path)
    minhashes,sketches = minhash(attributes)
    neighbors = []

    for sketch in sketches:
        sketch = str(sketch)

        if not sketch in db:
            continue

        for neighbor_path in db[sketch]:
            neighbor_minhashes = db[neighbor_path]['minhashes']
            similarity = (neighbor_minhashes == minhashes).sum() / float(NUM_MINHASHES)
            neighbors.append((neighbor_path,similarity))

    neighbors = list(set(neighbors))
    neighbors.sort(key=lambda entry:entry[1],reverse=True)
    print ""
    print "Sample name".ljust(64),"Shared code estimate"
    for neighbor, similarity in neighbors:
        short_neighbor = neighbor.split("/")[-1]
        comments = db[neighbor]['comments']
        print str("[*] "+short_neighbor).ljust(64),similarity
        for comment in comments:
            print "\t[comment]",comment

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""
Simple code-sharing search system which allows you to build up a database of malware samples (indexed by file paths) and
then search for similar samples given some new sample
"""
    )

    parser.add_argument(
        "-l","--load",dest="load",default=None,
        help="Path to directory containing malware, or individual malware file, to store in database"
    )

    parser.add_argument(
        "-s","--search",dest="search",default=None,
        help="Individual malware file to perform similarity search on"
    )

    parser.add_argument(
        "-c","--comment",dest="comment",default=None,
        help="Comment on a malware sample path"
    )

    parser.add_argument(
        "-w","--wipe",action="store_true",default=False,
        help="Wipe sample database"
    )

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
    if args.load:
        malware_paths = [] # where we'll store the malware file paths
        malware_attributes = dict() # where we'll store the malware strings
 
        for root, dirs, paths in os.walk(args.load):
            # walk the target directory tree and store all of the file paths
            for path in paths:
                full_path = os.path.join(root,path)
                malware_paths.append(full_path)

        # filter out any paths that aren't PE files
        malware_paths = filter(pecheck, malware_paths)

        # get and store the strings for all of the malware PE files
        for path in malware_paths:
            store_sample(path)

    if args.search:
        search_sample(args.search)

    if args.comment:
        comment_sample(args.comment)

    if args.wipe:
        wipe_database()
