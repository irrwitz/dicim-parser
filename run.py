import sys
import csv

import parser.dicom

if len(sys.argv) < 2:
    print("No filename given, please provide a dicom output file as input")
    print("Example: python run.py dicom.out")
    sys.exit(1)

with open(sys.argv[1], mode='r', encoding='latin_1') as fileobject:
    headers = parser.dicom.get_headers(fileobject)
    print(len(headers))
    fieldnames = [parser.dicom.PATIENT_NAME,
                  parser.dicom.PATIENT_BIRTHDATE,
                  parser.dicom.PATIENT_ID,
                  parser.dicom.PATIENT_SEX,
                  parser.dicom.STUDY_DATE,
                  parser.dicom.MODALITY,
                  parser.dicom.BODY_PART_EXAMINED,
                  parser.dicom.STUDY_DESCRIPTION,
                  parser.dicom.SERIES_DESCRIPTION,
                  parser.dicom.ACCESSION_NUMBER,
                  parser.dicom.STUDY_ID,
                  parser.dicom.SERIES_NUMBER,
                  parser.dicom.INSTANCE_NUMBER,
                  parser.dicom.REFERRING_PHYSICIAN_NAME,
                  parser.dicom.INSTANCE_AVAILABILITY,
                  parser.dicom.INSTITUTION_NAME,
                  parser.dicom.STUDY_INSTANCE_UID,
                  parser.dicom.SERIES_INSTANCE_UID,
                  parser.dicom.SPECIFIC_CHARACTER_SET,
                  parser.dicom.QUERY_RETRIEVE_LEVEL,
                  parser.dicom.RETRIEVE_AE_TITLE
                  ]
    with open('output.csv', 'w', newline='') as csvfile:
        dicom_writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                      delimiter=';', extrasaction='ignore')
        dicom_writer.writeheader()
        for header in headers:
            print(header)
            dicom_writer.writerow(header)
