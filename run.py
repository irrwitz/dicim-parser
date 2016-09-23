import sys
import csv

import parser.dicom


if len(sys.argv) < 2:
    print("No filename given, please provide a dicom output file as input")
    print("Example: python run.py dicom.out")
    sys.exit(1)


with open(sys.argv[1], 'r') as fileobject:
    headers = parser.dicom.get_headers(fileobject)
    print(len(headers))
    fieldnames = [parser.dicom.AccessionNumber,
                  parser.dicom.PatientSex,
                  parser.dicom.BodyPartExamined]
    with open('output.csv', 'w', newline='') as csvfile:
        dicom_writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                      delimiter=';', extrasaction='ignore')
        dicom_writer.writeheader()
        for header in headers:
            dicom_writer.writerow(header)
