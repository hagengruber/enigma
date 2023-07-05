const checkboxes = document.querySelectorAll('input[type="checkbox"]');
let lastChecked = null;
let pairCounter = 0;
const colors = [
  "#4CAF50",
  "#FFC107",
  "#2196F3",
  "#9C27B0",
  "#FF5722",
  "#00BCD4",
  "#673AB7",
  "#FF9800",
  "#3F51B5",
  "#CDDC39",
  "#FFEB3B",
  "#E91E63",
  "#795548"
];

// array to keep track of already paired checkboxes
const pairedCheckboxes = [];

checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', function(e) {
    this.parentNode.classList.add('clicked')

    // check if maximum number of pairs has been teached
    const selectedPairs = pairedCheckboxes.filter(cb => cb.checked);
    if (selectedPairs.length === 20) {
      unpairCheckbox(this);
      return;
    }

    if (lastChecked && lastChecked !== this && this.checked) {
      // check if lastChecked is already paired with another checkbox
      if (pairedCheckboxes.includes(lastChecked)) {
        unpairCheckbox(lastChecked);
      }

      const pairs = document.querySelectorAll(`input[name="${lastChecked.name}"]:checked`);
      if (pairs.length === 1) {
        const color = colors[pairCounter % colors.length];
        pairs[0].parentNode.style.backgroundColor = color;
        pairs[0].parentNode.querySelector('.checkboxInput').style.backgroundColor = 'black';
        this.parentNode.style.backgroundColor = color;
        this.parentNode.querySelector('.checkboxInput').style.backgroundColor = 'black';

        // add both checkboxes to pairedCheckboxes array
        pairedCheckboxes.push(lastChecked, this);
        pairCounter++;
      } else {
        unpairCheckbox(lastChecked);
        unpairCheckbox(this);
      }
      lastChecked = null;
    } else if (!this.checked) {
      unpairCheckbox(this);
    } else {
      lastChecked = this;
    }

    let plugboardPairs = getPlugBoardPairs();

    for (const [key, value] of Object.entries(plugboardPairs)) {
      if(value.length % 2 !== 0) {
        for (let container of value) {
          let element = document.getElementById('checkbox' + container)
          element.style['background-color'] = '#fff'
          element.parentElement.style['background-color'] = ""
          let index = pairedCheckboxes.indexOf(element);
          if (index > -1) {
            pairedCheckboxes.splice(index, 1);
          }
        }
      }
    }

  });
});

function unpairCheckbox(checkbox) {
  checkbox.parentNode.classList.remove('clicked');
  checkbox.parentNode.style.backgroundColor = '';
  checkbox.parentNode.querySelector('.checkboxInput').style.backgroundColor = '';
  checkbox.checked = false;
  // remove checkbox from pairedCheckboxes array
  const index = pairedCheckboxes.indexOf(checkbox);
  if (index > -1) {
    pairedCheckboxes.splice(index, 1);
  }
}
