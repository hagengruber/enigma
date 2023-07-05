import unittest
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from model.enigma import Enigma


class EnigmaEncryptTest(unittest.TestCase):
    """Tests multiple encryption scenarios, returns assertions"""

    def test_encrypt1(self):
        """Sets expected alphabets for rotors with encryption in Enigma 1, returns assertion that
        expected encryption output is correct"""

        test_enigma = Enigma('Enigma 1', [{'rotor': 'I', 'startposition': 'A'},
                                          {'rotor': 'II', 'startposition': 'B'},
                                          {'rotor': 'III', 'startposition': 'C'}],
                                          'UKW-B')

        expected_output = 20
        expected_rotor_1 = 'KMFLGDQVZNTOWYHXUSPAIBRCJE'
        expected_rotor_2 = 'JDKSIRUXBLHWTMCQGZNPYFVOEA'
        expected_rotor_3 = 'FHJLCPRTXVZNYEIWGAKMUSQOBD'
        actual_output = test_enigma.encrypt(7)

        assert expected_output == actual_output[0]
        assert expected_rotor_1 == actual_output[1][0].alphabet
        assert expected_rotor_2 == actual_output[1][1].alphabet
        assert expected_rotor_3 == actual_output[1][2].alphabet

    def test_encrypt2(self):
        """Sets expected alphabets for rotors with encryption in Enigma M3, returns assertion that
        expected encryption output is correct"""

        test_enigma = Enigma('Enigma M3', [{'rotor': 'I', 'startposition': 'A'},
                                           {'rotor': 'II', 'startposition': 'B'},
                                           {'rotor': 'III', 'startposition': 'C'}],
                                           'UKW-B')

        expected_output = 19
        actual_output = test_enigma.encrypt(2)
        expected_rotor_1 = 'KMFLGDQVZNTOWYHXUSPAIBRCJE'
        expected_rotor_2 = 'JDKSIRUXBLHWTMCQGZNPYFVOEA'
        expected_rotor_3 = 'FHJLCPRTXVZNYEIWGAKMUSQOBD'

        assert expected_output == actual_output[0]
        assert expected_rotor_1 == actual_output[1][0].alphabet
        assert expected_rotor_2 == actual_output[1][1].alphabet
        assert expected_rotor_3 == actual_output[1][2].alphabet

    def test_encrypt3(self):
        """Sets expected alphabets for rotors with encryption in Enigma B, returns assertion that
        expected encryption output is correct"""

        test_enigma = Enigma('Enigma B', [{'rotor': 'I', 'startposition': 'A'},
                                          {'rotor': 'II', 'startposition': 'B'},
                                          {'rotor': 'III', 'startposition': 'C'}],
                                          'UKW-A')

        expected_output = 19
        actual_output = test_enigma.encrypt(11)
        expected_rotor_1 = 'SBGÖXQJDHOÄUCFRTEZVÅINLYMKAP'
        expected_rotor_2 = 'HNSYÖADMOTRZXBÄIGÅEKQUPFLVJC'
        expected_rotor_3 = 'QIAÄXRJBÖZSPCFYUNTHDOMEKGLÅV'

        assert expected_output == actual_output[0]
        assert expected_rotor_1 == actual_output[1][0].alphabet
        assert expected_rotor_2 == actual_output[1][1].alphabet
        assert expected_rotor_3 == actual_output[1][2].alphabet

    def test_notch1(self):
        """Sets expected alphabets for rotors in Enigma B 
        and turns first rotor, returns assertion that
        expected encryption output with different notch 
        is correct"""

        test_notch = Enigma('Enigma B', [{'rotor': 'I', 'startposition': 'A'},
                                         {'rotor': 'II', 'startposition': 'B'},
                                         {'rotor': 'III', 'startposition': 'C'}],
                                         'UKW-A')

        expected_output = 19
        actual_output = test_notch.encrypt(11)
        expected_rotor_1 = 'SBGÖXQJDHOÄUCFRTEZVÅINLYMKAP'
        expected_rotor_2 = 'HNSYÖADMOTRZXBÄIGÅEKQUPFLVJC'
        expected_rotor_3 = 'QIAÄXRJBÖZSPCFYUNTHDOMEKGLÅV'

        assert expected_output == actual_output[0]
        assert expected_rotor_1 == actual_output[1][0].alphabet
        assert expected_rotor_2 == actual_output[1][1].alphabet
        assert expected_rotor_3 == actual_output[1][2].alphabet

    def test_notch2(self):
        """Sets expected alphabets for rotors in Enigma B 
        and turns first and second rotor, returns assertion 
        that expected encryption output with different notches 
        is correct"""

        test_notch = Enigma('Enigma B', [{'rotor': 'I', 'startposition': 'G'},
                                         {'rotor': 'II', 'startposition': 'B'},
                                         {'rotor': 'III', 'startposition': 'C'}],
                                         'UKW-A')

        expected_output = 5
        actual_output = test_notch.encrypt(11)
        expected_rotor_1 = 'JDHOÄUCFRTEZVÅINLYMKAPSBGÖXQ'
        expected_rotor_2 = 'NSYÖADMOTRZXBÄIGÅEKQUPFLVJCH'
        expected_rotor_3 = 'QIAÄXRJBÖZSPCFYUNTHDOMEKGLÅV'

        assert expected_output == actual_output[0]
        assert expected_rotor_1 == actual_output[1][0].alphabet
        assert expected_rotor_2 == actual_output[1][1].alphabet
        assert expected_rotor_3 == actual_output[1][2].alphabet

    def test_notch3(self):
        """Sets expected alphabets for rotors in Enigma B 
        and turns all three rotors, returns assertion that
        expected encryption output with different notches 
        is correct"""

        test_notch = Enigma('Enigma B', [{'rotor': 'I', 'startposition': 'G'},
                                         {'rotor': 'II', 'startposition': 'G'},
                                         {'rotor': 'III', 'startposition': 'C'}],
                                         'UKW-A')

        expected_output = 0
        actual_output = test_notch.encrypt(11)
        expected_rotor_1 = 'JDHOÄUCFRTEZVÅINLYMKAPSBGÖXQ'
        expected_rotor_2 = 'DMOTRZXBÄIGÅEKQUPFLVJCHNSYÖA'
        expected_rotor_3 = 'QIAÄXRJBÖZSPCFYUNTHDOMEKGLÅV'

        assert expected_output == actual_output[0]
        assert expected_rotor_1 == actual_output[1][0].alphabet
        assert expected_rotor_2 == actual_output[1][1].alphabet
        assert expected_rotor_3 == actual_output[1][2].alphabet
