function cancelSettings() {
  let version = document.getElementById('version').getElementsByTagName('h1')[0].innerHTML;

  // expire date -> current date - 10 years
  let expire = new Date(new Date().setFullYear(new Date().getFullYear() - 10)).toUTCString();

  // reset cookies
  document.cookie = 'plaintext="";SameSite=Lax;expires=' + expire;
  document.cookie = 'ciphertext="";SameSite=Lax;expires=' + expire;
  document.cookie = 'reflector="";SameSite=Lax;expires=' + expire;

  let i = 1;
  let dump = '';

  while(true) {
    try{
      dump = document.cookie.split('rotor_pos' + i + '=')[1].split(';')[0];
      dump = document.cookie.split('start_pos' + i + '=')[1].split(';')[0];
      document.cookie = 'rotor_pos' + i + '="";SameSite=Lax;expires=' + expire;
      document.cookie = 'start_pos' + i + '="";SameSite=Lax;expires=' + expire;
      i++;
    } catch (e) {
      break;
    }
  }

  document.cookie = 'plugboard="";SameSite=Lax;expires=' + expire;

  window.location = '/?version=' + version;
}

// if a rotor get changed
document.getElementById('rotor1Select').addEventListener('change', (event) => {
  handle_rotor_options();
});

// Handle the change events for the rotor2Select element
document.getElementById('rotor2Select').addEventListener('change', (event) => {
  handle_rotor_options();
});

// handle the change event for the rotor3Select element
document.getElementById('rotor3Select').addEventListener('change', (event) => {
  handle_rotor_options();
});

function handle_rotor_options() {
  let rotor_in_use = [];
  let rotoren = [
    document.getElementById('rotor1Select'),
    document.getElementById('rotor2Select'),
    document.getElementById('rotor3Select')
  ];

  // saves all rotors which are currently in use in the array 'rotor_in_use'
  rotoren.forEach(function(rotor) {
    rotor_in_use.push(rotor.value);
  });

  rotoren.forEach(function(rotor) {
    for(let i = 0; i !== rotor.length; i++) {
      // if the current rotor in iteration is also in the array 'rotor_in_use' -> disabled = true
      // else disabled = false
      rotor[i].disabled = rotor_in_use.includes(rotor[i].value);
    }
  });
}