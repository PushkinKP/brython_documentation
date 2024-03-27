// Références vers les éléments HTML
const consoleInput = document.getElementById('console-input');
const consoleRun = document.getElementById('console-run');
const consoleOutput = document.getElementById('console-output');

// Fonction pour exécuter la commande saisie dans la console
function executeCommand() {
  try {
    // Récupère la commande saisie par l'utilisateur
    const command = consoleInput.value.trim();

    // Vérifie si la commande est vide
    if (command === '') {
      throw new Error('Veuillez saisir une commande.');
    }

    // Évalue la commande de manière sécurisée avec Function() plutôt que eval()
    // Cela évite l'exécution de code potentiellement dangereux
    const result = Function('"use strict";return (' + command + ')')();

    // Affiche le résultat dans la console
    consoleOutput.textContent = result;
  } catch (error) {
    // Affiche l'erreur dans la console
    consoleOutput.textContent = error.message;
  }
}

// Écouteur d'événement pour le bouton "Exécuter"
consoleRun.addEventListener('click', executeCommand);


function updateClock() {
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  const seconds = now.getSeconds().toString().padStart(2, '0');
  document.getElementById('clock').innerText = `${hours}:${minutes}:${seconds}`;
}
setInterval(updateClock, 1000);
updateClock();


