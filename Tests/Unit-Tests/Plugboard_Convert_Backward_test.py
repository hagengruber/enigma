import unittest
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from controller.plugboard import PlugBoard


class PlugBoardTests(unittest.TestCase):
    """Tests multiple scenarios of converting characters from output alphabet to
    input alphabet, returns assertions"""

    def test_convert_backward1(self):
        """Sets expected int value with no plugboard pair in Enigma 1,
        returns assertion for correct output"""
        plug = PlugBoard([], version="Enigma 1")
        expected_result = 2
        actual_result = plug.convert_backward(number=2)
        assert expected_result == actual_result

    def test_convert_backward2(self):
        """Sets expected int value with one plugboard pair in Enigma M3,
        returns assertion for correct output"""
        plug = PlugBoard(["BE"], version="Enigma M3")
        expected_result = 1
        actual_result = plug.convert_backward(number=4)
        assert expected_result == actual_result

    def test_convert_backward3(self):
        """Sets expected int value with two plugboard pairs in Enigma M3,
        returns assertion for correct output"""
        plug = PlugBoard(["BE", "AC"], version="Enigma M3")
        expected_result = 0
        actual_result = plug.convert_backward(number=2)
        assert expected_result == actual_result
