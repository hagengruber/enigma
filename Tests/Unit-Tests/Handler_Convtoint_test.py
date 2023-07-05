import unittest
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from controller.handler import Handler


class HandlerTests(unittest.TestCase):
    """Tests multiple scenarios of converting characters 
    to integers in handler, returns assertions"""

    def test_convtoint1(self):
        """Sets expected int test value with Enigma 1, returns assertion for correct output"""
        expected_result = 4
        actual_result = Handler.convtoint("E", "Enigma 1")
        assert expected_result == actual_result

    def test_convtoint2(self):
        """Sets expected int test value with Enigma M3, returns assertion for correct output"""
        expected_result = 15
        actual_result = Handler.convtoint("P", "Enigma M3")
        assert expected_result == actual_result

    def test_convtoint3(self):
        """Sets expected int test value with Enigma B, returns assertion for correct output"""
        expected_result = 26
        actual_result = Handler.convtoint("Ä", "Enigma B")
        assert expected_result == actual_result
