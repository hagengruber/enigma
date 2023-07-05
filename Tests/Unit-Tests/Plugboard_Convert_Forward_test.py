import unittest
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from controller.plugboard import PlugBoard


class PlugBoardTests(unittest.TestCase):
    """Tests multiple scenarios of converting characters from input alphabet to
    output alphabet, returns assertions"""

    def test_convert_forward1(self):
        """Sets expected int value with one plugboard pair in Enigma 1, 
        returns assertion for correct output"""
        plug = PlugBoard(["BC"], version="Enigma 1")
        expected_result = 2
        actual_result = plug.convert_forward(number=1)
        assert expected_result == actual_result

    def test_convert_forward2(self):
        """Sets expected int value with no plugboard pair in Enigma B, 
        returns assertion for correct output"""
        plug = PlugBoard([], version="Enigma B")
        expected_result = 10
        actual_result = plug.convert_forward(number=10)
        assert expected_result == actual_result

    def test_convert_forward3(self):
        """Sets expected int value with two plugboard pairs in Enigma M3, 
        returns assertion for correct output"""
        plug = PlugBoard(["AC", "OP"], version="Enigma M3")
        expected_result = 0
        actual_result = plug.convert_forward(number=2)
        assert expected_result == actual_result
