function findLableForControl(el) {
  var idVal = el.id;
  labels = document.getElementsByTagName('label');
  for (var i = 0; i < labels.length; i++) {
    if (labels[i].htmlFor == idVal)
      return labels[i];
  }
}

function getPlugBoard() {
  // prepare the plugboard data for transmitting (i.a. [AE, TL])
  let first_element = true;
  let plugboard = '[';
  let i = 0;

  while (i !== pairedCheckboxes.length) {
    if (!first_element) {
      plugboard += ', ';
    } else {
      first_element = false;
    }

    plugboard += "'" + findLableForControl(pairedCheckboxes[i++]).innerHTML +
      findLableForControl(pairedCheckboxes[i++]).innerHTML + "'";
  }
  return plugboard + ']';
}

function check_plugboard() {
  // Check if the Plugboard is valid

  let el = document.getElementsByClassName('checkbox');
  let dict = {};
  let dump;

  for (let item of el) {
    try {
      dump = item.attributes.style.nodeValue;
      if (item.attributes.style.nodeValue === '') { continue; }
      if (dict[item.attributes.style.nodeValue] === undefined) {
        dict[item.attributes.style.nodeValue] = 1;
      } else {
        dict[item.attributes.style.nodeValue] += 1;
      }
    } catch (error) {
      continue;
    }
  }

  // if the counter in the color-code dict. is odd, the plugboard is incorrect
  for (let key in dict) {
    if (dict[key] % 2 === 1) {
      return -1;
    }
  }
}

function getData(key) {

  // Check if the Plugboard is valid
  if (check_plugboard() === -1) {
    alert("Plugboard fehlerhaft 2");
    return -1;
  }

  let version = document.getElementById('version').getElementsByTagName('h1')[0].innerHTML;

  let erg = getRotorsAndPositions()
  let rotors = erg[0]
  let rotors_startPosition = erg[1]

  let reflector = document.getElementById('reflector').value;

  let lol = "{'character': '" + key + "', 'plugboard': " + getPlugBoard() +
  ", 'version': '" + version + "','rotors':["

  for(let i=0; i<rotors.length; i++){
    lol += "{'rotor': '" + rotors[i] + "', 'startposition': '" + rotors_startPosition[i] + "'}"
    
    if(i<rotors.length-1){
      lol+=","
    }
  }

  lol += "], 'reflector': '" + reflector + "'}"
  
  return lol
}

function shiftParagraphs(paraList) {
  let previousText = "";
  for (let i = 0; i < paraList.length; i++) {
    let currentPara = paraList[i];
    let currentText = currentPara.textContent;
    currentPara.textContent = previousText;

    // add a space every 5 characters in the paragraph
    let len = currentPara.textContent.replace(/\s/g, "").length;
    if (len > 5) {
      let extraSpaces = Math.floor(len / 5);
      for (let j = 1; j <= extraSpaces; j++) {
        let index = (j * 6) - 1;
        currentPara.textContent = currentPara.textContent.slice(0, index) + " " + currentPara.textContent.slice(index);
      }
    }
    previousText = currentText;
  }
}

function change_initial_rotor(json_data) {
  // changes the start position

  let id = '';

  for (let i = 0; i !== json_data['rotor_starting_point'].length; i++) {
    id = 'rotor' + (i + 1) + 'InitialPosition'
    document.getElementById(id).value = json_data['rotor_starting_point'][i];
  }
}

function write_history(key, character) {
  let plaintextPara = document.querySelector("#plaintext > p");
  let plaintextContent = plaintextPara.textContent;

  // append the clicked character into the plaintext
  plaintextContent += key;

  // display the last 140 characters in the plaintext div
  if (plaintextContent.length > 140) {
    plaintextContent = plaintextContent.substring(plaintextContent.length - 140);
  }

  plaintextPara.textContent = plaintextContent;

  // update the ciphertext paragraph with the received character
  let ciphertextPara = document.querySelector("#ciphertext > p");

  ciphertextPara.textContent += character;

  // limit the ciphertext to 140 characters
  if (ciphertextPara.textContent.length > 140) {
    ciphertextPara.textContent = ciphertextPara.textContent.substring(ciphertextPara.textContent.length - 140);
  }

  // shift paragraphs if necessary
  if (plaintextPara.textContent.replace(/\s/g, "").length >= 5) {
    shiftParagraphs(document.querySelectorAll("#plaintext > p"));
  }

  if (ciphertextPara.textContent.replace(/\s/g, "").length >= 5) {
    shiftParagraphs(document.querySelectorAll("#ciphertext > p"));
  }
}

function getPlugBoardPairs() {
  // prepares the plugboard-data for the cookies (i.a. {"background-color: rgb(255, 193, 7)":"AB"})
  let el = document.getElementsByClassName('checkbox');
  let dump;
  let plugboard = {}

  for (let item of el) {
    try {
      dump = item.attributes.style.nodeValue;
      if (item.attributes.style.nodeValue === '') { continue; }
      if (plugboard[item.attributes.style.nodeValue] === undefined) {
        plugboard[item.attributes.style.nodeValue] = item.innerText;
      } else {
        plugboard[item.attributes.style.nodeValue] += item.innerText;
      }
    } catch (error) {
      continue;
    }
  }
  return plugboard;
}

function save_cookie() {
  // saves the cookies (current state of the machine)

  let plaintext = document.getElementById('plaintext').innerHTML;
  let ciphertext = document.getElementById('ciphertext').innerHTML;

  plaintext = plaintext.replaceAll(/\n/g, '');
  ciphertext = ciphertext.replaceAll(/\n/g, '');

  let reflector = document.getElementById('reflector').value;

  // the function returns a dict., but the cookie requires a string AND the character ; is not allowed in cookies
  let plugboard = JSON.stringify(getPlugBoardPairs()).replaceAll(';', '');

  // expire date -> current date + 10 years
  let expire = new Date(new Date().setFullYear(new Date().getFullYear() + 10)).toUTCString();

  let erg = getRotorsAndPositions()
  let rotors = erg[0]
  let rotors_startPosition = erg[1]

  document.cookie = 'plaintext=' + plaintext + ';SameSite=Lax;expires=' + expire;
  document.cookie = 'ciphertext=' + ciphertext + ';SameSite=Lax;expires=' + expire;
  document.cookie = 'reflector=' + reflector + ';SameSite=Lax;expires=' + expire;

  for(i=0; i<rotors.length; i++){
    document.cookie = 'rotor_pos'+ (i+1) +'=' + rotors[i] + ';SameSite=Lax;expires=' + expire;
    document.cookie = 'start_pos'+ (i+1) +'=' + rotors_startPosition[i] +';SameSite=Lax;expires=' + expire;
  }
  document.cookie = 'plugboard=' + plugboard + ';SameSite=Lax;expires=' + expire;
}

function clickVK(id) {
  // Handles the communication

  let xhttp = new XMLHttpRequest();

  let key = document.getElementById(id).innerHTML;

  // Checks if the plugboard has invalid entries
  if (pairedCheckboxes.length % 2 !== 0) {
    alert('Plugboard fehlerhaft! 1');
    return;
  }

  let data = getData(key);

  if (data === -1) { return; }

  xhttp.onload = function () {

    let json_data = JSON.parse(xhttp.responseText);

    let character = json_data['character'];

    // highlight lamp panel character
    let lampPanel = document.getElementById("lampPanel_" + character);
    if (lampPanel) {
      lampPanel.style.backgroundColor = "yellow";
      setTimeout(function () {
        lampPanel.style.backgroundColor = "white";
      }, 500);
    }

    change_initial_rotor(json_data);

    write_history(key, character)
    save_cookie();
  };

  xhttp.open("POST", "/");
  xhttp.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
  xhttp.send(data);
}
function getRotorsAndPositions(){
  i = 1
  let erg= []
  let rotors = [];
  let rotors_startPosition = [];
  
  do {
    try {
      rotors.push(document.getElementById('rotor'+i+'Select').value);
      rotors_startPosition.push(document.getElementById('rotor'+i+'InitialPosition').value);
      i++   
    } catch (e) {
      break
    } 
  } while (true);

  return [rotors, rotors_startPosition]

}