from controller.handler import Handler
import pathlib


class Website:
    """Creates a dynamic website and adds dynamic build feature to frontend"""

    def __init__(self, version):
        self.version = version
        self.site = ''

    @staticmethod
    def get_file(file):
        """Opens required file and returns it"""
        try:
            with open(str(pathlib.Path(__file__).parent.parent.resolve()) + '/files/' + file, 'r',
                  encoding='UTF-8') as file:
                return file.read().replace('\n', '')
        except FileNotFoundError:
            return False

    def create_header(self):
        """Creates header for the website"""
        enigma_data = Handler.get_enigma_data()

        helper = Website.get_file('header.html')
        if not helper:
            return False

        self.site += helper

        # navigation menu
        for variants, _ in enigma_data.items():
            self.site += '<li><a href="?version=' + variants + '">' + variants + '</a></li>'

        self.site += '</ul> </nav> </div>'

        return True

    def add_reflector(self):
        """Creates reflector for the website"""
        enigma_data = Handler.get_enigma_data()
        reflectors = enigma_data[self.version]['reflectoren']
        helper = Website.get_file('rotorset_reflector.html')

        if not helper:
            return False

        self.site += helper

        # adds all reflectors to the selection menu
        for reflector in reflectors:
            self.site += '<option value="' + reflector['name'] + '">' + \
                reflector['name'] + '</option>'

        self.site += '</select> </td>'

        return True

    def add_start_position(self):
        """Creates start positions for the website"""
        enigma_data = Handler.get_enigma_data()
        start_position = enigma_data[self.version]['etw']
        used = enigma_data[self.version]['used_rotors']+1
        helper = Website.get_file('rotorset_startposition.html')

        if not helper:
            return False

        self.site += helper

        # set the start position for all 3 rotors
        for rotor in range(1, used):

            # opening tag
            self.site += '<td> <select id="rotor' + str(rotor) + 'InitialPosition">'

            # the first character should have the attribute 'selected'
            selected = False

            for start in start_position:
                # if yet no character was selected
                if not selected:
                    # add attribute 'selected' to character
                    self.site += '<option selected id="rotor' + str(
                        rotor) + 'InitialPositionOption' + start + '">' + start + '</option>'
                    selected = True
                else:
                    self.site += '<option id="rotor' + str(
                        rotor) + 'InitialPositionOption' + start + '">' + start + '</option>'

            self.site += '</select> </td>'

        self.site += '</tr> </tbody> </table> <div id="outer_button">' \
                     '<button id="button" onclick="cancelSettings()">Reset</button></div> </div>'

        return True

    def add_rotor(self):
        """Creates rotors for the website"""
        enigma_data = Handler.get_enigma_data()

        rotoren = enigma_data[self.version]['rotoren']
        # disabled -> all rotors which get selected in the initial state
        disabled = []

        used = enigma_data[self.version]['used_rotors']+1

        # get all rotors which get selected in the initial state and save them into disabled
        for rotor_count in range(1, used):
            self.site += "<td>Position "+ str(rotor_count)+"</td>"
            selected = False
            for rotor, _ in rotoren.items():
                if not selected and rotor not in disabled:
                    disabled.append(rotor)
                    selected = True

        self.site += "</tr><tr><td>Rotor</td>"

        # select -> all rotors which have been selected in the initial state
        # difference to 'disabled': the rotors in 'disabled'
        # have to be disabled on all rotor positions,
        # 'select' handles the behavior for the initial selected elements
        # (i.a rotor 1: I, rotor 2: II, rotor 3: III)
        select = []

        for rotor_count in range(1, used):
            self.site += '<td> <select id="rotor' + str(rotor_count) + 'Select">'
            selected = False

            for rotor, _ in rotoren.items():
                # if yet no rotor was selected and the rotor is not in use (not in select)
                if not selected and rotor not in select:
                    self.site += '<option disabled selected>' + rotor + '</option>'
                    selected = True
                    select.append(rotor)
                # if the rotor has to be disabled (because its in 'disabled')
                elif rotor in disabled:
                    self.site += '<option disabled>' + rotor + '</option>'
                else:
                    self.site += '<option>' + rotor + '</option>'

            self.site += '</select> </td>'

        self.site += '</tr>'

    def print_alphabet(self, alphabet, is_kind):
        """
        Creates div container based on the given alphabet and type
        (lamp panel, keyboard, plugboard)
        """

        alphabet = self.sort_qwertz(alphabet)

        # define layers
        div_container = ['upperRow', 'middleRow', 'lowerRow']
        # starting tag
        self.site += '<div class="' + div_container[0] + '">'
        # first layer was used, so remove it
        div_container.pop(0)
        row_counter = 0

        for character in alphabet:
            # if there are still layers and 9 elements in the current row
            if len(div_container) != 0 and row_counter == 10:
                # close row and open new layer
                self.site += '</div> <div class="' + div_container[0] + '">'

                # layer was used, so remove it and reset the row counter
                row_counter = 0
                div_container.pop(0)

            # print the elements for the lamp panel
            if is_kind == 'lamp_panel':
                self.site += '<div id="lampPanel_' + character + '" class="bulb">' \
                    + character + '</div>'
            # print the elements for the virtual keyboard
            elif is_kind == 'virtual_keyboard':
                self.site += '<div id = "virtualKeyboard' + character + \
                    '" onclick="clickVK(this.id);" class="key">'\
                             + character + '</div>'
            # print the elements for the plugboard
            elif is_kind == 'plugboard':
                self.site += '<div class="checkbox">'\
                    '<label for="checkbox' + character + '" class="checkboxLabel">' \
                        + character + '</label>''<input type="checkbox" name="checkbox' \
                            + character +'" id="checkbox' + character + '"' \
                    'class="checkboxInput" value="' + character + '"' \
                    'color="undefined"> </div>'

            row_counter += 1

        self.site += '</div></div>'

    def add_lamp_panel(self):
        """Creates lamp panel for the website"""
        enigma_data = Handler.get_enigma_data()

        alphabet = enigma_data[self.version]['etw']

        self.site += '<div class="lampPanel">'

        self.print_alphabet(alphabet, 'lamp_panel')

    def add_virtual_keyboard(self):
        """Creates virtual keyboard for the website"""
        enigma_data = Handler.get_enigma_data()

        alphabet = enigma_data[self.version]['etw']

        self.site += '<div class="virtualKeyboard">'

        self.print_alphabet(alphabet, 'virtual_keyboard')

    def add_plugboard(self):
        """Creates plugboard for the website"""
        enigma_data = Handler.get_enigma_data()

        alphabet = enigma_data[self.version]['etw']

        self.site += '<div class="plugBoard">'

        self.print_alphabet(alphabet, 'plugboard')

    def add_history(self):
        """Creates history container for the website"""
        helper = Website.get_file('history.html')

        if not helper:
            return False

        self.site += '</div>' + helper

        return True

    def create_body(self):
        """Creates whole body for the website"""

        helper = self.add_reflector()
        self.add_rotor()
        helper2 = self.add_start_position()

        self.add_lamp_panel()
        self.add_virtual_keyboard()

        enigma_data = Handler.get_enigma_data()

        # if the plugboard is required
        if enigma_data[self.version]['plugboard']:
            self.add_plugboard()

        helper3 = self.add_history()

        if not helper or not helper2 or not helper3:
            return False

        return True

    def create_website(self):
        """Creates website and returns it"""

        helper = self.create_header()
        helper2 = self.create_body()

        if not helper or not helper2:
            return False

        return self.site

    def sort_qwertz(self, alphabet):
        """Sorts the alphabet to QWERTZ layout"""
        qwertz_layout = "QWERTZUIOPÜASDFGHJKLÖÄYXCVBNM"
        return sorted(alphabet.upper(), key=lambda x: qwertz_layout.index(x) \
                      if x in qwertz_layout else len(qwertz_layout))
