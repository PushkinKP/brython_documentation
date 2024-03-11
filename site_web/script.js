// Références vers les éléments HTML
const consoleInput = document.getElementById('console-input');
const consoleRun = document.getElementById('console-run');
const consoleOutput = document.getElementById('console-output');

// Écouteur d'événement pour le bouton "Exécuter"
consoleRun.addEventListener('click', () => {
  try {
    // Évalue la commande et récupère le résultat
    const result = eval(consoleInput.value);

    // Affiche le résultat dans la console
    consoleOutput.textContent = result;
  } catch (error) {
    // Affiche l'erreur dans la console
    consoleOutput.textContent = error.message;
  }
});
