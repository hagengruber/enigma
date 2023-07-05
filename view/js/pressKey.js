let currentKey = null;
let lampPanel = null;

function keydownHandler(event) {
  // check if the key pressed by user is a letter

  if (event.keyCode >= 65 && event.keyCode <= 90) {
    let key = String.fromCharCode(event.keyCode);

    if (currentKey === key) {
      return;
    }

    currentKey = key;
    // clickVK("virtualKeyboard" + currentKey);
    let virtual_key = document.getElementById('virtualKeyboard' + currentKey);
    virtual_key.classList.add('key_active_for_js');

    virtual_key.click();

    setTimeout(function() {
      virtual_key.classList.remove('key_active_for_js');
    }, 100);
  }
  else{
    alert("Ungültige Eingabe");
  }
}

function keyupHandler(event) {
  // chek if the key released by user is the same key that was pressed
  
  if (event.keyCode >= 65 && event.keyCode <= 90 && String.fromCharCode(event.keyCode) === currentKey) {
    currentKey = null;

    // unhgilight lamp panel
    // ToDo: Ist der Code nötig?
    if (lampPanel) {
      lampPanel.style.backgroundColor = "";
      lampPanel = null;
    }
  }
}

document.addEventListener("keydown", keydownHandler);
document.addEventListener("keyup", keyupHandler);
