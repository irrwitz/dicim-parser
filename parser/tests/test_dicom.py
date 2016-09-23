#! /usr/bin/env python
import unittest

import parser.dicom


class Test(unittest.TestCase):
    def test_start(self):
        line = 'W: # Dicom-Data-Set'
        start = parser.dicom.is_start(line)
        self.assertEqual(True, start)

    def test_tag(self):
        line = 'W: (0008,0060) CS [MR]                       #   2, 1 Modality'
        tag = parser.dicom.get_tag(line)
        self.assertEqual('(0008,0060)', tag)

    def test_value(self):
        line = 'W: (0008,0060) CS [MR]                       #   2, 1 Modality'
        tag = parser.dicom.get_value(line)
        self.assertEqual('MR', tag)

if __name__ == '__main__':
    unittest.main()
