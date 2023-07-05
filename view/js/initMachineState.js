// if cookies exists(a state of the machine)
if(document.cookie !== '') {
    set_machine_state();
}

function set_machine_state() {
    let cookies = document.cookie;

    // cookie is just a dict.-like string, seperated with ';'
    let plaintext = cookies.split('plaintext=')[1].split(';')[0];
    let ciphertext = cookies.split('ciphertext=')[1].split(';')[0];
    let reflector = cookies.split('reflector=')[1].split(';')[0];

    let i = 1;
    
    do {
        try {
            document.getElementById('rotor'+i+'Select').value = cookies.split('rotor_pos'+i+'=')[1].split(';')[0];
            document.getElementById('rotor'+i+'InitialPosition').value = cookies.split('start_pos'+i+'=')[1].split(';')[0];
            i++   
          } catch (e) {
            break
          } 
    } while (true);

    let s_plugboard = cookies.split('plugboard=')[1].split(';')[0];
    let plugboard = JSON.parse(s_plugboard);

    document.getElementById('plaintext').innerHTML = plaintext;
    document.getElementById('ciphertext').innerHTML = ciphertext;
    document.getElementById('reflector').value = reflector;

    // set plugboard
    for (const [key, value] of Object.entries(plugboard)) {
        let bgColor = key.split(':')[1];
        // set the color
        document.getElementById('checkbox' + value[0]).parentElement.style.backgroundColor = bgColor;
        document.getElementById('checkbox' + value[1]).parentElement.style.backgroundColor = bgColor;
        document.getElementById('checkbox' + value[0]).parentElement.getElementsByClassName('checkboxInput')[0].style.backgroundColor = 'black';
        document.getElementById('checkbox' + value[1]).parentElement.getElementsByClassName('checkboxInput')[0].style.backgroundColor = 'black';

        // set the variable pairedCheckboxes defined in plugboardPairs.js
        pairedCheckboxes.push(document.getElementById('checkbox' + value[0]).parentElement.getElementsByClassName('checkboxInput')[0]);
        pairedCheckboxes.push(document.getElementById('checkbox' + value[1]).parentElement.getElementsByClassName('checkboxInput')[0]);
    }

    // set the variable pairCounter defined in plugboardPairs.js
    pairCounter = Object.keys(plugboard).length
}