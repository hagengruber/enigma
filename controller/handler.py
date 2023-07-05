import pathlib
import json
import os


class Handler:
    """Controller Class"""

    @staticmethod
    def get_enigma_data(app = None):
        """Reads rotor data from json file, returns data"""
        # try:
        if os.path.isfile(str(pathlib.Path(__file__).parent.parent.resolve()) +
                        '/files/rotors.json'):
            with open(str(pathlib.Path(__file__).parent.parent.resolve()) +
                        '/files/rotors.json', 'r', encoding='UTF-8') as data:
                return json.load(data)
        # except FileNotFoundError:
            # app.send_response(500)
            # app.end_headers()
            # app.wfile.write(bytes("Internal Server Error", 'UTF-8'))
            # return False

    @staticmethod
    def convtoint(char, version):
        """Converts character to integer, returns integer"""

        alphabet = Handler.get_enigma_data()[version]['etw']
        return alphabet.find(char)

    @staticmethod
    def convtochar(number, version):
        """Converts integer to character, returns character"""

        alphabet = Handler.get_enigma_data()[version]['etw']
        return alphabet[number]

    @staticmethod
    def init_rotation(position, clr_alphabet, alphabet):
        """Does initial rotation after setting rotors, returns alphabets"""
        for _ in range(position):
            alphabet = alphabet[1:] + alphabet[0]
            clr_alphabet = clr_alphabet[1:] + clr_alphabet[0]
        return clr_alphabet, alphabet
