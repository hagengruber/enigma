class Rotor:
    """Class for initialising and using rotor"""

    def __init__(self, name, alphabet, clr_alphabet, notch=None, turnover=None, turn=None):
        self.name = name
        self.alphabet = alphabet
        self.notch = notch
        self.turnover = turnover
        self.turn = turn
        self.clr_alphabet = clr_alphabet

    def convert_forward(self, number):
        """Sends number through clr_alphabet and then alphabet, returns number"""
        character = self.alphabet[number]
        number = self.clr_alphabet.find(character)
        return number

    def convert_backward(self, number):
        """Sends number through alphabet and then clr_alphabet, returns number"""
        character = self.clr_alphabet[number]
        number = self.alphabet.find(character)
        return number

    def rotation(self):
        """Shifts the clr_alphabet and alphabet by one"""
        self.alphabet = self.alphabet[1:] + self.alphabet[0]
        self.clr_alphabet = self.clr_alphabet[1:] + self.clr_alphabet[0]
