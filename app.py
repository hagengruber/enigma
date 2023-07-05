from http.server import BaseHTTPRequestHandler, HTTPServer
from os import chdir
from os import path
import urllib.parse
import pathlib
import json
import ast

from controller.plugboard import PlugBoard
from controller.handler import Handler
from model.website import Website
from model.enigma import Enigma


class App(BaseHTTPRequestHandler):
    """Class for webserver"""

    def get_error(self, error):
        """Handles invalid requests"""

        if error == 404:
            # Wenn 404 not found Fehler auftritt
            self.send_response(301)
            # redirect Benutzer zur Enigma 1
            self.send_header('Location', '/?version=Enigma 1')
            self.end_headers()
        elif error == 400:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(bytes("Bad Request", 'UTF-8'))

    def get_allowed_path(self):
        """Checks, if the given Path is in view"""
        if len(self.path.split('..')) > 1:
            return False
        return '.' + self.path

    def get_static(self):
        """Handles static requests"""

        valid_path = self.get_allowed_path()

        if not valid_path:
            self.get_error(404)
            return

        try:
            if path.isfile(valid_path):
                # Wenn angeforderter Pfad eine Datei ist
                file_extension = path.splitext(self.path)[-1]
                content_type = ''
                if file_extension == '.png':
                    content_type = 'image/png'
                elif file_extension == '.jpeg' or file_extension == '.jpg':
                    content_type = 'image/jpeg'
                elif file_extension == '.js':
                    content_type = 'text/javascript'

                if content_type != '':
                    with open(valid_path, 'rb') as file:
                        # Sendet Datei
                        self.send_response(200)
                        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
                        self.send_header('Pragma', 'no-cache')
                        self.send_header('Expires', '0')
                        self.send_header('Content-type', content_type)
                        self.end_headers()

                        self.wfile.write(file.read())
                        return
                else:
                    with open(valid_path, encoding='UTF-8') as file:
                        # Sendet Datei
                        self.send_response(200)
                        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
                        self.send_header('Pragma', 'no-cache')
                        self.send_header('Expires', '0')
                        self.end_headers()

                        for content in file.readlines():
                            self.wfile.write(bytes(content, 'utf-8'))
                        return

            else:
                # Wenn Verzeichnis angefordert wurde
                self.get_error(404)
                return

        except FileNotFoundError:
            # Wenn angeforderte Datei nicht existiert
            self.get_error(404)

    def handle_get_par(self, version):
        """Sends index.html to browser"""

        my_website = Website(version)
        helper = my_website.create_website()

        # if not helper:
        # self.get_error(500)

        self.wfile.write(bytes(helper, "utf-8"))

    def check_enigma_variants(self, version):
        """Checks if the required enigma version exists in the rotors.json file"""
        enigma_data = Handler.get_enigma_data(self)
        if not enigma_data:
            return -1

        try:
            return enigma_data[version]
        except KeyError:
            return False

    @staticmethod
    def get_version(decoded_version):
        """Unquote the url to normal letters (i.e. %C3%B6 -> ö)"""
        return urllib.parse.unquote(decoded_version.replace('%20', ' '))

    def handle_request(self):
        """Handles get-requests"""

        if self.path.split('?')[0] == '/':
            # Wenn root-Verzeichnis / angefordert wurde

            try:
                if self.path.split('?')[1].split('=')[0] == 'version':
                    # Wenn get-Parameter 'version' existiert

                    version = App.get_version(self.path.split('?')[1].split('=')[1])

                    helper = self.check_enigma_variants(version)
                    # if helper == -1:
                    # self.get_error(500)

                    if helper:
                        self.send_response(200)
                        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
                        self.send_header('Pragma', 'no-cache')
                        self.send_header('Expires', '0')
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.handle_get_par(version)

                    else:
                        # Wenn fehlerhafte Version angefordert wurde

                        self.send_response(301)
                        # redirect Benutzer zur Enigma 1
                        self.send_header('Location', '/?version=Enigma 1')
                        self.end_headers()

            except IndexError:
                # Wenn kein version get-Parameter existiert
                self.send_response(301)
                # redirect Benutzer zur Enigma 1
                self.send_header('Location', '/?version=Enigma 1')
                self.end_headers()

        elif self.path.split('/')[1] == 'view':
            # Nur die Dateien im view Ordner können ausgelesen werden
            self.get_static()

        else:
            # Fehlerhafte Anfrage -> 404 not found
            self.get_error(404)

    def handle_json_request(self):
        """Called from http.server when a get-request is received"""
        self.send_response(200)
        self.end_headers()

        json_file = str(pathlib.Path(__file__).parent.resolve()) + '/files/rotors.json'

        with open(json_file, 'wb') as f:
            f.write(self.rfile.read(int(self.headers['Content-Length'])))

        self.wfile.write(bytes('Ok lol', "utf-8"))

    def do_GET(self):
        """Called from http.server when a get-request is received"""
        self.handle_request()

    def do_POST(self):
        """
            Called from http.server, when a post-request is received
            Handles post-requests
        """

        self.send_response(200)
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        if self.path == '/change_json':
            self.handle_json_request()
            return

        # Hole get-request
        data = ast.literal_eval(self.rfile.read(int(self.headers['Content-Length'])).decode())

        if not App.input_validation(data):
            self.get_error(400)
            return

        plug = PlugBoard(data['plugboard'], version=data['version'])

        rotors = []
        for element in data['rotors']:
            rotors.append(element)

        current = Enigma(data['version'], rotors, data['reflector'])

        # encrypt
        number = plug.convert_forward(Handler.convtoint(data['character'], data['version']))
        number, current.rotors = current.encrypt(number)
        character = Handler.convtochar(plug.convert_backward(number), data['version'])
        rotor = []

        for enigma_rotor in current.rotors:
            rotor.append(enigma_rotor.clr_alphabet[0])

        send_data = {'character': character, 'rotor_starting_point': rotor}
        self.wfile.write(bytes(json.dumps(send_data), "utf-8"))

    @staticmethod
    def input_validation(data):
        """Validates the Input send by the FrontEnd"""
        valid_reflector = False
        try:
            # prüfen auf vorhandene Version
            version = Handler.get_enigma_data()[data['version']]

            # prüfen auf gültige Eingabe
            alphabet = Handler.get_enigma_data()[data['version']]['etw']

            if not data['character'] in alphabet:
                return False

            # prüfen auf richtige rotoren
            for element in data['rotors']:
                if element['rotor'] not in version['rotoren']:
                    return False

            # prüfen auf reflektoren
            for element in version['reflectoren']:
                if element['name'] == data['reflector']:
                    valid_reflector = True

            if not valid_reflector:
                return False
            else:
                return True

        except KeyError:
            return False


if __name__ == '__main__':
    HOST = "0.0.0.0"
    PORT = 8080

    # Ändert working directory zum Pfad der app.py Datei
    chdir(str(pathlib.Path(__file__).parent.resolve()))

    webServer = HTTPServer((HOST, PORT), App)
    print("Server started http://localhost:" + str(PORT))
    webServer.serve_forever()
