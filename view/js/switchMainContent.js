const switchMainContent = document.getElementById("switchMainContent");
const outsideMainContent = document.querySelector(".initialRotor");
const insideMainContent = document.querySelector(".insideEnigma");
const initialRotor = document.querySelector(".initialRotor");

// hide the insideEnigma section initially
insideMainContent.style.display = "none";
// ToDo: wird diese Datei noch benötigt?
switchMainContent.addEventListener("click", function() {
  if (insideMainContent.style.display === "none") {
    insideMainContent.style.display = "block";
    outsideMainContent.style.display = "none";
    switchMainContent.textContent = "Enigma schließen";
    initialRotor.classList.remove("center-initial-rotor");
  } else {
    insideMainContent.style.display = "none";
    outsideMainContent.style.display = "block";
    switchMainContent.textContent = "Enigma öffnen"; 
    initialRotor.classList.add("center-initial-rotor");
  }
});
