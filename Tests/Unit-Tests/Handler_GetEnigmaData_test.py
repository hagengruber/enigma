import unittest
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from controller.handler import Handler


class HandlerTests(unittest.TestCase):
    """Test that enigma gets correct data from json file"""

    def test_getenigmadata(self):
        """Sets expected data values for all Enigma variants, 
        returns assertion for correct values"""
        expected_result = {
            "Enigma B": {
                "etw": "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ",
                "rotoren": {
                    "I": {"alphabet": "PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA", "Notch": "G", "Turnover": "Ä", "nr": 1},
                    "II": {"alphabet": "CHNSYÖADMOTRZXBÄIGÅEKQUPFLVJ", "Notch": "G", "Turnover": "Ä", "nr": 1},
                    "III": {"alphabet": "ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL", "Notch": "G", "Turnover": "Ä", "nr": 1}
                },
                "used_rotors": 3,
                "reflectoren": [
                    {"name": "ukw-a", "alphabet": "LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY"}
                ],
                "plugboard": False
            },

            "Enigma 1": {
                "etw": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "rotoren": {
                    "I": {
                        "alphabet": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                        "Notch": "Y",
                        "Turnover": "Q",
                        "nr": 1
                    },
                    "II": {
                        "alphabet": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                        "Notch": "M",
                        "Turnover": "E",
                        "nr": 1
                    },
                    "III": {
                        "alphabet": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                        "Notch": "D",
                        "Turnover": "V",
                        "nr": 1
                    },
                    "IV": {
                        "alphabet": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
                        "Notch": "R",
                        "Turnover": "J",
                        "nr": 1
                    },
                    "V": {
                        "alphabet": "VZBRGITYUPSDNHLXAWMJQOFECK",
                        "Notch": "H",
                        "Turnover": "Z",
                        "nr": 1
                    }
                },
                "used_rotors": 3,
                "reflectoren": [
                    {"name": "ukw-a", "alphabet": "EJMZALYXVBWFCRQUONTSPIKHGD"},
                    {"name": "ukw-b", "alphabet": "YRUHQSLDPXNGOKMIEBFZCWVJAT"},
                    {"name": "ukw-c", "alphabet": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}
                ],
                "plugboard": True
            },

            "Enigma M3": {
                "etw": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "rotoren": {
                    "I": {
                        "alphabet": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                        "Notch": "Y",
                        "Turnover": "Q",
                        "nr": 1
                    },
                    "II": {
                        "alphabet": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                        "Notch": "M",
                        "Turnover": "E",
                        "nr": 1
                    },
                    "III": {
                        "alphabet": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                        "Notch": "D",
                        "Turnover": "V",
                        "nr": 1
                    },
                    "IV": {
                        "alphabet": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
                        "Notch": "R",
                        "Turnover": "J",
                        "nr": 1
                    },
                    "V": {
                        "alphabet": "VZBRGITYUPSDNHLXAWMJQOFECK",
                        "Notch": "H",
                        "Turnover": "Z",
                        "nr": 1
                    },
                    "VI": {
                        "alphabet": "JPGVOUMFYQBENHZRDKASXLICTW",
                        "Notch": "HU",
                        "Turnover": "ZM",
                        "nr": 2
                    },
                    "VII": {
                        "alphabet": "NZJHGRCXMYSWBOUFAIVLPEKQDT",
                        "Notch": "HU",
                        "Turnover": "ZM",
                        "nr": 2
                    },
                    "VIII": {
                        "alphabet": "FKQHTLXOCBJSPDZRAMEWNIUYGV",
                        "Notch": "HU",
                        "Turnover": "ZM",
                        "nr": 2
                    }
                },
                "used_rotors": 3,
                "reflectoren": [
                    {"name": "ukw-b", "alphabet": "YRUHQSLDPXNGOKMIEBFZCWVJAT"},
                    {"name": "ukw-c", "alphabet": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}
                ],
                "plugboard": True
            }

        }

        actual_result = Handler.get_enigma_data()
        assert expected_result == actual_result
