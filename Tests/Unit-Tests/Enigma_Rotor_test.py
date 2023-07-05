import unittest
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from model.enigma import Enigma


class EnigmaRotorTest(unittest.TestCase):
    """Tests the rotors of the enigma, returns assertions"""

    def test_init_rotors1(self):
        """Sets values to initialise rotors with Enigma 1, returns assertion that
        default individual rotor settings are correct"""

        test_enigma = Enigma('Enigma 1', [{'rotor': 'I', 'startposition': 'A'},
                                          {'rotor': 'II', 'startposition': 'B'},
                                          {'rotor': 'III', 'startposition': 'C'}],
                                          'UKW-B')

        assert test_enigma.rotors[0].alphabet == 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        assert test_enigma.rotors[0].name == 'I'
        assert test_enigma.rotors[0].notch == 'Y'
        assert test_enigma.rotors[0].turn == 1
        assert test_enigma.rotors[0].turnover == 'Q'

        assert test_enigma.rotors[1].alphabet == 'JDKSIRUXBLHWTMCQGZNPYFVOEA'
        assert test_enigma.rotors[1].name == 'II'
        assert test_enigma.rotors[1].notch == 'M'
        assert test_enigma.rotors[1].turn == 1
        assert test_enigma.rotors[1].turnover == 'E'

        assert test_enigma.rotors[2].alphabet == 'FHJLCPRTXVZNYEIWGAKMUSQOBD'
        assert test_enigma.rotors[2].name == 'III'
        assert test_enigma.rotors[2].notch == 'D'
        assert test_enigma.rotors[2].turn == 1
        assert test_enigma.rotors[2].turnover == 'V'

    def test_init_rotors2(self):
        """Sets values to initialise rotors with Enigma M3, returns assertion that
        default individual rotor settings are correct"""

        test_enigma = Enigma('Enigma M3', [{'rotor': 'I', 'startposition': 'A'},
                                           {'rotor': 'II', 'startposition': 'B'},
                                           {'rotor': 'III', 'startposition': 'C'}],
                                           'UKW-B')

        assert test_enigma.rotors[0].alphabet == 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        assert test_enigma.rotors[0].name == 'I'
        assert test_enigma.rotors[0].notch == 'Y'
        assert test_enigma.rotors[0].turn == 1
        assert test_enigma.rotors[0].turnover == 'Q'

        assert test_enigma.rotors[1].alphabet == 'JDKSIRUXBLHWTMCQGZNPYFVOEA'
        assert test_enigma.rotors[1].name == 'II'
        assert test_enigma.rotors[1].notch == 'M'
        assert test_enigma.rotors[1].turn == 1
        assert test_enigma.rotors[1].turnover == 'E'

        assert test_enigma.rotors[2].alphabet == 'FHJLCPRTXVZNYEIWGAKMUSQOBD'
        assert test_enigma.rotors[2].name == 'III'
        assert test_enigma.rotors[2].notch == 'D'
        assert test_enigma.rotors[2].turn == 1
        assert test_enigma.rotors[2].turnover == 'V'

    def test_init_rotors3(self):
        """Sets values to initialise rotors with Enigma B, returns assertion that
        default individual rotor settings are correct"""

        test_enigma = Enigma('Enigma B', [{'rotor': 'I', 'startposition': 'A'},
                                          {'rotor': 'II', 'startposition': 'B'},
                                          {'rotor': 'III', 'startposition': 'C'}],
                                          'UKW-A')

        assert test_enigma.rotors[0].alphabet == 'PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA'
        assert test_enigma.rotors[0].name == 'I'
        assert test_enigma.rotors[0].notch == 'G'
        assert test_enigma.rotors[0].turn == 1
        assert test_enigma.rotors[0].turnover == 'Ä'

        assert test_enigma.rotors[1].alphabet == 'HNSYÖADMOTRZXBÄIGÅEKQUPFLVJC'
        assert test_enigma.rotors[1].name == 'II'
        assert test_enigma.rotors[1].notch == 'G'
        assert test_enigma.rotors[1].turn == 1
        assert test_enigma.rotors[1].turnover == 'Ä'

        assert test_enigma.rotors[2].alphabet == 'QIAÄXRJBÖZSPCFYUNTHDOMEKGLÅV'
        assert test_enigma.rotors[2].name == 'III'
        assert test_enigma.rotors[2].notch == 'G'
        assert test_enigma.rotors[2].turn == 1
        assert test_enigma.rotors[2].turnover == 'Ä'

    def test_rotation1(self):
        """Sets necessary test values for rotation with Enigma M3, returns assertion that
         output after rotation is correct"""

        test_rotation = Enigma('Enigma M3', [{'rotor': 'I', 'startposition': 'A'},
                                             {'rotor': 'II', 'startposition': 'B'},
                                             {'rotor': 'III', 'startposition': 'C'}],
                                             'UKW-B')

        expected_rotor_1 = 'KMFLGDQVZNTOWYHXUSPAIBRCJE'
        expected_rotor_2 = 'JDKSIRUXBLHWTMCQGZNPYFVOEA'
        expected_rotor_3 = 'FHJLCPRTXVZNYEIWGAKMUSQOBD'
        actual_output = test_rotation.encrypt(2)

        assert expected_rotor_1 == actual_output[1][0].alphabet
        assert expected_rotor_2 == actual_output[1][1].alphabet
        assert expected_rotor_3 == actual_output[1][2].alphabet

    def test_rotation2(self):
        """Sets necessary test values for rotation with Enigma B, returns assertion that
        output after rotation is correct"""

        test_rotation = Enigma('Enigma B', [{'rotor': 'I', 'startposition': 'A'},
                                            {'rotor': 'II', 'startposition': 'B'},
                                            {'rotor': 'III', 'startposition': 'C'}],
                                            'UKW-A')

        expected_rotor_1 = 'SBGÖXQJDHOÄUCFRTEZVÅINLYMKAP'
        expected_rotor_2 = 'HNSYÖADMOTRZXBÄIGÅEKQUPFLVJC'
        expected_rotor_3 = 'QIAÄXRJBÖZSPCFYUNTHDOMEKGLÅV'
        actual_output = test_rotation.encrypt(11)

        assert expected_rotor_1 == actual_output[1][0].alphabet
        assert expected_rotor_2 == actual_output[1][1].alphabet
        assert expected_rotor_3 == actual_output[1][2].alphabet
