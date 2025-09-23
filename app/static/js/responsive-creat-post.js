// Testing functions

function delMain() {
    const newElement = window.document.createElement('p');
    newElement.textContent = 'Olá, Mundo!';
    window.document.body.appendChild(newElement)
}

delMain()