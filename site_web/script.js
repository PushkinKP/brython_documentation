const consoleBtn = document.getElementById('console-btn');
const consoleContainer = document.getElementById('console-container');
const consoleElem = document.createElement('textarea');

consoleBtn.addEventListener('click', () => {
    if (consoleContainer.style.display === 'none' || consoleContainer.style.display === '') {
        consoleContainer.style.display = 'block';
        consoleBtn.textContent = 'Fermer la console';
        consoleElem.value = '';
        appendConsole(consoleElem);
    } else {
        consoleContainer.style.display = 'none';
        consoleBtn.textContent = 'Ouvrir la console';
        removeConsole();
    }
});

function appendConsole(consoleElem) {
    consoleContainer.appendChild(consoleElem);
    consoleElem.setAttribute('id', 'console');
    consoleElem.setAttribute('rows', '10');
    consoleElem.setAttribute('cols', '50');
    consoleElem.style.width = '100%';
    consoleElem.style.height = '300px';
    consoleElem.style.resize = 'none';
    consoleElem.style.display = 'block';
    consoleElem.style.marginTop = '1rem';
    consoleElem.style.marginBottom = '1rem';
    consoleElem.focus();
}

function removeConsole() {
    const consoleElem = document.getElementById('console');
    consoleContainer.removeChild(consoleElem);
}