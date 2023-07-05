import unittest
import os
import requests


class AppTest(unittest.TestCase):
    """Tests different scenarios of posts to the website, returns assertions"""

    def test_post1(self):
        """Posts different test variables for Enigma 1,
        returns assertion that variables are correct"""

        post_var = {'character': 'Q', 'plugboard': [], 'reflector': 'ukw-b',
                    'rotors': [{'rotor': 'I', 'startposition': 'A'},
                               {'rotor': 'II', 'startposition': 'B'},
                               {'rotor': 'III', 'startposition': 'C'}],
                    'version': 'Enigma 1'}

        if "CI" in os.environ.keys():
            x = requests.post('http://enigma:8080', json=post_var, timeout=10)
        else:
            x = requests.post('http://localhost:8080', json=post_var, timeout=10)

        assert x.text == '{"character": "L", "rotor_starting_point": ["B", "B", "C"]}'

    def test_post2(self):
        """Posts different test variables for Enigma M3, 
        returns assertion that variables are correct"""

        post_var = {'character': 'A', 'plugboard': [], 'reflector': 'ukw-b',
                    'rotors': [{'rotor': 'I', 'startposition': 'A'},
                               {'rotor': 'II', 'startposition': 'B'},
                               {'rotor': 'III', 'startposition': 'C'}],
                    'version': 'Enigma M3'}

        if "CI" in os.environ.keys():
            x = requests.post('http://enigma:8080', json=post_var, timeout=10)
        else:
            x = requests.post('http://localhost:8080', json=post_var, timeout=10)

        assert x.text == '{"character": "I", "rotor_starting_point": ["B", "B", "C"]}'

    def test_post3(self):
        """Posts different test variables for Enigma B, 
        returns assertion that variables are correct"""

        post_var = {'character': 'Å', 'plugboard': [], 'reflector': 'ukw-a',
                    'rotors': [{'rotor': 'I', 'startposition': 'A'},
                               {'rotor': 'II', 'startposition': 'B'},
                               {'rotor': 'III', 'startposition': 'C'}],
                    'version': 'Enigma B'}

        if "CI" in os.environ.keys():
            x = requests.post('http://enigma:8080', json=post_var, timeout=10)
        else:
            x = requests.post('http://localhost:8080', json=post_var, timeout=10)

        assert x.text == '{"character": "U", "rotor_starting_point": ["B", "B", "C"]}'
