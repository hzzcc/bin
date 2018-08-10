#!/usr/bin/env python

import sys,getopt
import mapbox_vector_tile

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputfile == '':
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit()

    with open(inputfile, 'rb') as f:
        data = f.read();

    decoded_data = decoded_data = mapbox_vector_tile.decode(data)

    if outputfile == '':
        print decoded_data
    else:
        with open(outputfile, 'w') as f:
            f.write(repr(decoded_data))

if __name__ == "__main__":
   main(sys.argv[1:])
