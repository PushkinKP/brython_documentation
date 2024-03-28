const btnToggle = document.querySelector('.btn-toggle');

btnToggle.addEventListener('click', () => {
  const body = document.body;
  if(body.classList.contains('dark')){
    body.classList.add('light')
    body.classList.remove('dark')
    btnToggle.innerHTML = ""
  } else if(body.classList.contains('light')){
    body.classList.add('dark')
    body.classList.remove('light')
    btnToggle.innerHTML = ""
  }
})

// Français
$(function() {
  $(".fr").click(function() {
    $(".navbar ul li:eq(0) a").text("Installation");
    $(".navbar ul li:eq(1) details summary a").text("Tutoriel");
    $(".navbar ul li:eq(1) details ul li:eq(0) a").text("Introduction");
    $(".navbar ul li:eq(1) details ul li:eq(1) a").text("Structure d'une page");
    $(".navbar ul li:eq(1) details ul li:eq(2) a").text("Mise en forme avec les balises HTML");
    $(".navbar ul li:eq(1) details ul li:eq(3) a").text("Gestion des événements");
    $(".navbar ul li:eq(1) details ul li:eq(4) a").text("Le programme complet");
  })
});

// Anglais
$(function() {
  $(".en").click(function() {
    $(".navbar ul li:eq(0) a").text("Installation");
    $(".navbar ul li:eq(1) details summary a").text("Tutorial");
    $(".navbar ul li:eq(1) details ul li:eq(0) a").text("Introduction");
    $(".navbar ul li:eq(1) details ul li:eq(1) a").text("Page structure");
    $(".navbar ul li:eq(1) details ul li:eq(2) a").text("Formatting with HTML tags");
    $(".navbar ul li:eq(1) details ul li:eq(3) a").text("Event management");
    $(".navbar ul li:eq(1) details ul li:eq(4) a").text("The complete program");
  })
});
