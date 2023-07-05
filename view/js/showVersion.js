window.onload = function (){
    let queryString = window.location.search;
    let urlParams = new URLSearchParams(queryString);
    let version = urlParams.get('version')

    document.getElementById('version').getElementsByTagName('h1')[0].innerText = version;
  };