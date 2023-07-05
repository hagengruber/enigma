from controller.handler import Handler
from model.rotor import Rotor


class Enigma:
    """Class for initialising and using enigma machine"""

    def __init__(self, version, rotoren, reflector):
        self.version = version
        self.rotors = []
        self.ukw = None
        self.clr_alphabet = None
        self.test = None
        self.init_rotors(rotoren, reflector)

    def init_rotors(self, rotoren, reflector):
        """Sets rotors based on data from the frontend"""

        enigma_data = Handler.get_enigma_data()[self.version]
        for rotor in rotoren:
            for name, data in rotor.items():

                self.clr_alphabet = enigma_data['etw']

                if name == 'startposition':
                    # Interrupts when rotor is set and start position is reached
                    continue
                for r_name, r_data in enigma_data['rotoren'].items():
                    if r_name == data:
                        startposition = Handler.convtoint(rotor["startposition"], self.version)
                        clr_alphabet, alphabet = Handler.init_rotation(startposition,
                                                                       self.clr_alphabet,
                                                                       r_data['alphabet'])
                        self.rotors.append(Rotor(data, alphabet, clr_alphabet,
                                                 notch=r_data['Notch'],
                                                 turnover=r_data['Turnover'], turn=r_data['nr']))

        for enigma_reflector in enigma_data['reflectoren']:
            for _, name in enigma_reflector.items():
                if name == reflector.lower():
                    self.ukw = Rotor('ukw', enigma_reflector['alphabet'],
                                     Handler.get_enigma_data()[self.version]['etw'])

    def encrypt(self, number):
        """Converts incoming number with the rotors, returns number"""
        self.rotate()
        for rotor in self.rotors:
            number = rotor.convert_forward(number)
        number = self.ukw.convert_forward(number)
        for rotor in reversed(self.rotors):
            number = rotor.convert_backward(number)
        # self.rotate()
        return number, self.rotors

    def rotate(self):
        """
            The first element of clr_alphabet is searched in the notch string,
            if matched with the notch the position is returned, otherwise -1
            (necessary for Enigma M3 Rotor 6-8 - these have two notches)
        """
        if self.rotors[0].notch.find(self.rotors[0].clr_alphabet[0]) > -1 and \
            self.rotors[1].notch.find(self.rotors[1].clr_alphabet[1]) > -1:

            self.rotors[0].rotation()
            self.rotors[1].rotation()
            self.rotors[2].rotation()
        elif self.rotors[0].notch.find(self.rotors[0].clr_alphabet[0]) > -1:
            self.rotors[0].rotation()
            self.rotors[1].rotation()
        else:
            self.rotors[0].rotation()
