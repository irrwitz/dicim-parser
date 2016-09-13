
import sys

HEADER_START = 'W: # Dicom-Data-Set'

if len(sys.argv) < 2:
    print "No filename given, please provide a dicom output file as input"
    print "Example: python parser.py dicom.out"
    sys.exit(1)

def isHeaderStart(line):
   "returns True if it is the start of a new header"
   return line.startswith(HEADER_START)

with open(sys.argv[1], 'r') as fileobject:
    for line in fileobject:
        if isHeaderStart(line):
            print '.'




