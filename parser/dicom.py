import re

PatientName = '(0010,0010)'
PatientBirthDate = '(0010,0030)'
PatientID = '(0010,0020)'
PatientSex = '(0010,0040)'
StudyDate = '(0008,0020)'
Modality = '(0008,0060)'
BodyPartExamined = '(0018,0015)'
StudyDescription = '(0008,1030)'
SeriesDescription = '(0008,103e)'
AccessionNumber = '(0008,0050)'
StudyID = '(0020,0010)'
SeriesNumber = '(0020,0011)'
InstanceNumber = '(0020,0013)'
ReferringPhysicianName = '(0008,0090)'
InstanceAvailability = '(0008,0056)'
InstitutionName = '(0008,0080)'
StudyInstanceUID = '(0020,000d)'
SeriesInstanceUID = '(0020,000e)'
SpecificCharacterSet = '(0008,0005)'
QueryRetrieveLevel = '(0008,0052)'
RetrieveAETitle = '(0008,0054)'


def get_headers(fileobject):
    result = []
    single_header = {}
    for line in fileobject:
        if is_valid(line):
            single_header[get_tag(line)[2]] = get_value(line)
        if is_start_or_end(line) and single_header:
            result.append(single_header.copy())
            single_header.clear()
    return result


def is_start_or_end(line):
    """ Returns True if it is the end of a DICOM header """
    return re.match('^W:\s*$', line)


def is_valid(line):
    return '(' in line and ')' in line and '[' in line and ']' in line


def get_tag_value(line):
    return get_tag(line), get_tag_value(line)


def get_tag(line):
    """
    Returns the tag value of the line, which is everything between
    the first square brackets.
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
