import unittest
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from controller.handler import Handler


class HandlerTests(unittest.TestCase):
    """Tests multiple scenarios of converting integers 
    to characters in handler, returns assertions"""

    def test_convtochar1(self):
        """Sets expected char test value with Enigma 1, returns assertion for correct output"""
        expected_result = "C"
        actual_result = Handler.convtochar(2, "Enigma 1")
        assert expected_result == actual_result

    def test_convtochar2(self):
        """Sets expected char test value with Enigma M3, returns assertion for correct output"""
        expected_result = "Z"
        actual_result = Handler.convtochar(25, "Enigma M3")
        assert expected_result == actual_result

    def test_convtochar3(self):
        """Sets expected char test value with Enigma B, returns assertion for correct output"""
        expected_result = "Å"
        actual_result = Handler.convtochar(25, "Enigma B")
        assert expected_result == actual_result
