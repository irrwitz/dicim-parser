import sys

import dicom


if len(sys.argv) < 2:
    print("No filename given, please provide a dicom output file as input")
    print("Example: python run.py dicom.out")
    sys.exit(1)


with open(sys.argv[1], 'r') as fileobject:
    for line in fileobject:
        if dicom.is_start(line):
            print('New Header')
        if dicom.is_valid(line):
            print(dicom.get_tag(line), dicom.get_value(line))
