from controller.handler import Handler


class PlugBoard:
    """Class for initialising and using plugboard"""

    def __init__(self, pairs, version):
        self.input = Handler.get_enigma_data()[version]['etw']
        self.output = self.input
        self.swap(pairs)

    def swap(self, pairs):
        """Swaps the letters in self.output alphabet based on the var pairs"""

        for pair in pairs:
            char1 = pair[0]
            char2 = pair[1]
            pos_char1 = self.input.find(char1)
            pos_char2 = self.input.find(char2)
            self.output = self.output[:pos_char1] + char2 + self.output[pos_char1+1:]
            self.output = self.output[:pos_char2] + char1 + self.output[pos_char2+1:]

    def convert_forward(self, number):
        """Converts number from self.input alphabet to self.output alphabet, returns integer"""

        char = self.input[number]
        return self.output.find(char)

    def convert_backward(self, number):
        """Converts number from self.output alphabet to self.input alphabet, returns integer"""

        char = self.output[number]
        return self.input.find(char)
