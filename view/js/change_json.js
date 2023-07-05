function send_json(json_string) {

    let xhttp = new XMLHttpRequest();

      xhttp.onload = function () {
        // Nothing
      };

      xhttp.open("POST", "/change_json");
      xhttp.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
      xhttp.send(json_string);

}

function add_enigma_variant() {

    let json_string = '{\n' +
        '    "Enigma B" : { \n' +
        '        "etw" : "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ",\n' +
        '        "rotoren": {\n' +
        '            "I" : {"alphabet": "PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA", "Notch":"G","Turnover": "Ä","nr":1},\n' +
        '            "II" : {"alphabet": "CHNSYÖADMOTRZXBÄIGÅEKQUPFLVJ", "Notch":"G","Turnover": "Ä","nr":1},\n' +
        '            "III" : {"alphabet": "ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL", "Notch":"G","Turnover": "Ä","nr":1}\n' +
        '        },\n' +
        '        "used_rotors": 3,\n' +
        '        "reflectoren": [\n' +
        '            {"name": "ukw-a", "alphabet": "LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY"}\n' +
        '        ],\n' +
        '        "plugboard": false\n' +
        '    },\n' +
        '\n' +
        '    "Enigma 1" : {\n' +
        '        "etw" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",\n' +
        '        "rotoren": {\n' +
        '            "I": {\n' +
        '                "alphabet": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",\n' +
        '                "Notch": "Y",\n' +
        '                "Turnover": "Q",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "II": {\n' +
        '                "alphabet": "AJDKSIRUXBLHWTMCQGZNPYFVOE",\n' +
        '                "Notch": "M",\n' +
        '                "Turnover": "E",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "III": {\n' +
        '                "alphabet": "BDFHJLCPRTXVZNYEIWGAKMUSQO",\n' +
        '                "Notch": "D",\n' +
        '                "Turnover": "V",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "IV": {\n' +
        '                "alphabet": "ESOVPZJAYQUIRHXLNFTGKDCMWB",\n' +
        '                "Notch": "R",\n' +
        '                "Turnover": "J",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "V": {\n' +
        '                "alphabet": "VZBRGITYUPSDNHLXAWMJQOFECK",\n' +
        '                "Notch": "H",\n' +
        '                "Turnover": "Z",\n' +
        '                "nr": 1\n' +
        '            }\n' +
        '        },\n' +
        '        "used_rotors": 3,\n' +
        '        "reflectoren": [\n' +
        '            {"name": "ukw-a", "alphabet": "EJMZALYXVBWFCRQUONTSPIKHGD"},\n' +
        '            {"name": "ukw-b", "alphabet": "YRUHQSLDPXNGOKMIEBFZCWVJAT"},\n' +
        '            {"name": "ukw-c", "alphabet": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}\n' +
        '        ],\n' +
        '        "plugboard": true\n' +
        '    },\n' +
        '\n' +
        '    "Enigma M3" : { \n' +
        '        "etw" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",\n' +
        '        "rotoren": {\n' +
        '            "I": {\n' +
        '                "alphabet": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",\n' +
        '                "Notch": "Y",\n' +
        '                "Turnover": "Q",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "II": {\n' +
        '                "alphabet": "AJDKSIRUXBLHWTMCQGZNPYFVOE",\n' +
        '                "Notch": "M",\n' +
        '                "Turnover": "E",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "III": {\n' +
        '                "alphabet": "BDFHJLCPRTXVZNYEIWGAKMUSQO",\n' +
        '                "Notch": "D",\n' +
        '                "Turnover": "V",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "IV": {\n' +
        '                "alphabet": "ESOVPZJAYQUIRHXLNFTGKDCMWB",\n' +
        '                "Notch": "R",\n' +
        '                "Turnover": "J",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "V": {\n' +
        '                "alphabet": "VZBRGITYUPSDNHLXAWMJQOFECK",\n' +
        '                "Notch": "H",\n' +
        '                "Turnover": "Z",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "VI": {\n' +
        '                "alphabet": "JPGVOUMFYQBENHZRDKASXLICTW",\n' +
        '                "Notch": "HU",\n' +
        '                "Turnover": "ZM",\n' +
        '                "nr": 2\n' +
        '            },\n' +
        '            "VII": {\n' +
        '                "alphabet": "NZJHGRCXMYSWBOUFAIVLPEKQDT",\n' +
        '                "Notch": "HU",\n' +
        '                "Turnover": "ZM",\n' +
        '                "nr": 2\n' +
        '            },\n' +
        '            "VIII": {\n' +
        '                "alphabet": "FKQHTLXOCBJSPDZRAMEWNIUYGV",\n' +
        '                "Notch": "HU",\n' +
        '                "Turnover": "ZM",\n' +
        '                "nr": 2\n' +
        '            }\n' +
        '        },\n' +
        '        "used_rotors": 3,\n' +
        '        "reflectoren": [\n' +
        '            {"name": "ukw-b", "alphabet": "YRUHQSLDPXNGOKMIEBFZCWVJAT"},\n' +
        '            {"name": "ukw-c", "alphabet": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}\n' +
        '        ],\n' +
        '        "plugboard": true\n' +
        '    },\n' +
        '\n' +
        '    "TEST" : { \n' +
        '        "etw" : "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ",\n' +
        '        "rotoren": {\n' +
        '            "I" : {"alphabet": "PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA", "Notch":"G","Turnover": "Ä","nr":1},\n' +
        '            "II" : {"alphabet": "CHNSYÖADMOTRZXBÄIGÅEKQUPFLVJ", "Notch":"G","Turnover": "Ä","nr":1},\n' +
        '            "III" : {"alphabet": "ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL", "Notch":"G","Turnover": "Ä","nr":1},\n' +
        '            "IV" : {"alphabet": "ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL", "Notch":"G","Turnover": "Ä","nr":1},\n' +
        '            "V" : {"alphabet": "ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL", "Notch":"G","Turnover": "Ä","nr":1}\n' +
        '        },\n' +
        '        "used_rotors": 5,\n' +
        '        "reflectoren": [\n' +
        '            {"name": "ukw-a", "alphabet": "LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY"}\n' +
        '        ],\n' +
        '        "plugboard": false\n' +
        '    }\n' +
        '}';

    send_json(json_string);

}

function recover_origin_enigma() {

    let json_string = '{\n' +
        '    "Enigma B" : { \n' +
        '        "etw" : "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ",\n' +
        '        "rotoren": {\n' +
        '            "I" : {"alphabet": "PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA", "Notch":"G","Turnover": "Ä","nr":1},\n' +
        '            "II" : {"alphabet": "CHNSYÖADMOTRZXBÄIGÅEKQUPFLVJ", "Notch":"G","Turnover": "Ä","nr":1},\n' +
        '            "III" : {"alphabet": "ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL", "Notch":"G","Turnover": "Ä","nr":1}\n' +
        '        },\n' +
        '        "used_rotors": 3,\n' +
        '        "reflectoren": [\n' +
        '            {"name": "ukw-a", "alphabet": "LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY"}\n' +
        '        ],\n' +
        '        "plugboard": false\n' +
        '    },\n' +
        '\n' +
        '    "Enigma 1" : {\n' +
        '        "etw" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",\n' +
        '        "rotoren": {\n' +
        '            "I": {\n' +
        '                "alphabet": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",\n' +
        '                "Notch": "Y",\n' +
        '                "Turnover": "Q",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "II": {\n' +
        '                "alphabet": "AJDKSIRUXBLHWTMCQGZNPYFVOE",\n' +
        '                "Notch": "M",\n' +
        '                "Turnover": "E",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "III": {\n' +
        '                "alphabet": "BDFHJLCPRTXVZNYEIWGAKMUSQO",\n' +
        '                "Notch": "D",\n' +
        '                "Turnover": "V",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "IV": {\n' +
        '                "alphabet": "ESOVPZJAYQUIRHXLNFTGKDCMWB",\n' +
        '                "Notch": "R",\n' +
        '                "Turnover": "J",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "V": {\n' +
        '                "alphabet": "VZBRGITYUPSDNHLXAWMJQOFECK",\n' +
        '                "Notch": "H",\n' +
        '                "Turnover": "Z",\n' +
        '                "nr": 1\n' +
        '            }\n' +
        '        },\n' +
        '        "used_rotors": 3,\n' +
        '        "reflectoren": [\n' +
        '            {"name": "ukw-a", "alphabet": "EJMZALYXVBWFCRQUONTSPIKHGD"},\n' +
        '            {"name": "ukw-b", "alphabet": "YRUHQSLDPXNGOKMIEBFZCWVJAT"},\n' +
        '            {"name": "ukw-c", "alphabet": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}\n' +
        '        ],\n' +
        '        "plugboard": true\n' +
        '    },\n' +
        '\n' +
        '    "Enigma M3" : { \n' +
        '        "etw" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",\n' +
        '        "rotoren": {\n' +
        '            "I": {\n' +
        '                "alphabet": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",\n' +
        '                "Notch": "Y",\n' +
        '                "Turnover": "Q",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "II": {\n' +
        '                "alphabet": "AJDKSIRUXBLHWTMCQGZNPYFVOE",\n' +
        '                "Notch": "M",\n' +
        '                "Turnover": "E",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "III": {\n' +
        '                "alphabet": "BDFHJLCPRTXVZNYEIWGAKMUSQO",\n' +
        '                "Notch": "D",\n' +
        '                "Turnover": "V",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "IV": {\n' +
        '                "alphabet": "ESOVPZJAYQUIRHXLNFTGKDCMWB",\n' +
        '                "Notch": "R",\n' +
        '                "Turnover": "J",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "V": {\n' +
        '                "alphabet": "VZBRGITYUPSDNHLXAWMJQOFECK",\n' +
        '                "Notch": "H",\n' +
        '                "Turnover": "Z",\n' +
        '                "nr": 1\n' +
        '            },\n' +
        '            "VI": {\n' +
        '                "alphabet": "JPGVOUMFYQBENHZRDKASXLICTW",\n' +
        '                "Notch": "HU",\n' +
        '                "Turnover": "ZM",\n' +
        '                "nr": 2\n' +
        '            },\n' +
        '            "VII": {\n' +
        '                "alphabet": "NZJHGRCXMYSWBOUFAIVLPEKQDT",\n' +
        '                "Notch": "HU",\n' +
        '                "Turnover": "ZM",\n' +
        '                "nr": 2\n' +
        '            },\n' +
        '            "VIII": {\n' +
        '                "alphabet": "FKQHTLXOCBJSPDZRAMEWNIUYGV",\n' +
        '                "Notch": "HU",\n' +
        '                "Turnover": "ZM",\n' +
        '                "nr": 2\n' +
        '            }\n' +
        '        },\n' +
        '        "used_rotors": 3,\n' +
        '        "reflectoren": [\n' +
        '            {"name": "ukw-b", "alphabet": "YRUHQSLDPXNGOKMIEBFZCWVJAT"},\n' +
        '            {"name": "ukw-c", "alphabet": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}\n' +
        '        ],\n' +
        '        "plugboard": true\n' +
        '    }\n' +
        '\n'+
        '}';

    send_json(json_string);

}