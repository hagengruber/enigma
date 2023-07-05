import unittest
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from model.rotor import Rotor


class RotorTestBackward(unittest.TestCase):
    """Tests multiple scenarios of converting integers 
    backwards in the rotor, returns assertions"""

    def test_convert_backward1(self):
        """Sets expected integer value, returns assertion for correct 
        output after converting backward"""
        rotor = Rotor('III', 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
                      'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'D', 'V', 1)

        expected_result = 25
        actual_result = rotor.convert_backward(14)
        assert expected_result == actual_result

    def test_convert_backward2(self):
        """Sets expected integer value, returns assertion for correct 
        output after converting backward"""
        rotor = Rotor('III', 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
                      'ABCDEFGHIJKLMNOPQRSTUVWXYZ','D', 'V', 1)

        expected_result = 16
        actual_result = rotor.convert_backward(8)
        assert expected_result == actual_result

    def test_convert_backward3(self):
        """Sets expected integer value, returns assertion for correct 
        output after converting backward"""
        rotor = Rotor('III', 'ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL',
                      'ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ', 'G', 'Ä', 1)

        expected_result = 20
        actual_result = rotor.convert_backward(7)
        assert expected_result == actual_result
