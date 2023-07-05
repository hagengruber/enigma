import unittest
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from controller.plugboard import PlugBoard


class PlugBoardTests(unittest.TestCase):
    """Tests multiple scenarios with plugboard letter swaps, returns assertions"""

    # ToDo: Enigma B Alphabet encode

    def test_swapTest1(self):
        """Sets expected alphabet for plugboard pair swap in Enigma M3, 
        returns assertion for correct alphabet"""
        plug = PlugBoard(['AX'], version="Enigma M3")
        expected_result = "XBCDEFGHIJKLMNOPQRSTUVWAYZ"
        actual_result = plug.output
        assert expected_result == actual_result

    def test_swapTest2(self):
        """Sets expected alphabet for two plugboard pair swaps in Enigma 1,
        returns assertion for correct alphabet"""
        plug = PlugBoard(['KC', 'AB'], version="Enigma 1")
        expected_result = "BAKDEFGHIJCLMNOPQRSTUVWXYZ"
        actual_result = plug.output
        assert expected_result == actual_result

    def test_swapTest3(self):
        """Sets expected alphabet for plugboard pair swap in Enigma B,
        returns assertion for correct alphabet"""
        plug = PlugBoard(['OÄ'], version="Enigma B")
        expected_result = "ABCDEFGHIJKLMNÄPQRSTUVXYZÅOÖ"
        actual_result = plug.output
        assert expected_result == actual_result

    def test_swapTest4(self):
        """Sets expected alphabet for empty plugboard pair swap in Enigma 1,
        returns assertion for correct alphabet"""
        plug = PlugBoard([], version="Enigma 1")
        expected_result = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        actual_result = plug.output
        assert expected_result == actual_result
