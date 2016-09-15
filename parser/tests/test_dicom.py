#! /usr/bin/env python
import unittest

from parser import dicom


class Test(unittest.TestCase):
    def test_start(self):
        line = 'W: # Dicom-Data-Set'
        start = dicom.is_start(line)
        self.assertEqual(True, start)

    def test_tag(self):
        line = 'W: (0008,0060) CS [MR]                                     #   2, 1 Modality'
        tag = dicom.get_tag(line)
        self.assertEqual('(0008,0060)', tag)

    def test_value(self):
        line = 'W: (0008,0060) CS [MR]                                     #   2, 1 Modality'
        tag = dicom.get_value(line)
        self.assertEqual('MR', tag)

if __name__ == '__main__':
    unittest.main()
