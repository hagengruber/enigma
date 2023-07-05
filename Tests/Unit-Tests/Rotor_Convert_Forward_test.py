import unittest
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from model.rotor import Rotor


class RotorTestForward(unittest.TestCase):
    """Tests multiples scenarios of converting integers 
    forward in the rotor, returns assertions"""

    def test_convert_forward1(self):
        """Sets expected integer value, returns assertion for 
        correct output after converting forward"""

        rotor = Rotor('I', 'PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA',
                      'ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ', 'G', 'Ä', 11)

        expected_result = 16
        actual_result = rotor.convert_forward(6)
        assert expected_result == actual_result

    def test_convert_forward2(self):
        """Sets expected integer value, returns assertion for 
        correct output after converting forward"""

        rotor = Rotor('I', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
                      'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'Y', 'Q', 1)

        expected_result = 23
        actual_result = rotor.convert_forward(16)
        assert expected_result == actual_result


    def test_convert_forward3(self):
        """Sets expected integer value, returns assertion for 
        correct output after converting forward"""

        rotor = Rotor('I', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
                      'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'Y', 'Q', 1)

        expected_result = 13
        actual_result = rotor.convert_forward(10)
        assert expected_result == actual_result
