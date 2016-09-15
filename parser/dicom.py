import re

START_HEADER = 'W: # Dicom-Data-Set'
END_HEADER = 'W:'
SPECIFIC_CHAR_SET = '(0008,0005)'
STUDY_DATE = '(0008,0020)'
ACCESSION_NUMBER = '(0008,0050)'
MODALITY = '(0008,0060)'
INSTITUTION_NAME = '(0008,0080)'
REFERRING_PHYSICIAN_NAME = '(0008,0090)'
STUDY_DESCRIPTION = '(0008,1030)'
SERIES_DESCRIPTION = '(0008,103e)'
PATIENT_BIRTH_DATE = '(0010,0030)'
PATIENT_SEX = '(0010,0040)'
BODY_PART_EXAMINED = '(0018,0015)'
STUDY_INSTANCE_UID = '(0020,000d)'
SERIES_INSTANCE_UID = '(0020,000e)'
STUDY_ID = '(0020,0010)'
SERIES_NUMBER = '(0020,0011)'


def is_start(line):
    """returns True if it is the start of a DICOM header"""
    return line.startswith(START_HEADER)


def is_end(line):
    """Returns True if it is the end of a DICOM header"""
    return line.endwith(END_HEADER)


def is_valid(line):
    return '(' in line and ')' in line and '[' in line and ']' in line


def get_tag(line):
    """
    Returns the tag value of the line, which is everything between
    the first brackets.
    For example on this line
        W: (0010,0040) CS [F ]
    tag value would be (0010,0040)
    """
    result = re.search('(\(.*\))', line)
    return result.group(0) if result else ''


def get_value(line):
    """
    Returns the value of the line, which is everything between
    the first and last square bracket.
    :param line: a line of the dicom file
    :return: value
    """
    result = re.search('\[(.*)\]', line)
    return result.group(1) if result else ''
