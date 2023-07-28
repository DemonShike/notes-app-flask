function toggleSearch() {
  var searchBar = document.getElementById("box-bar");
  searchBar.classList.toggle("show");
  
  if (searchBar.classList.contains("show")) {
    // Mostrar el teclado en dispositivos móviles
    document.querySelector("input[type='text']").focus();
  }
}

// Variables  del form register/login
const inputElement = document.getElementById('my-input');
const labelElement = document.getElementById('soymy-input');
const inputElementEmail = document.getElementById('email')
const LabelElementEmail = document.getElementById('labelEmail')
const inputElementTwo = document.getElementById('password');
const labelElementTwo = document.getElementById('soypassword')


// Logica que cambia los colores de los label
inputElement.addEventListener('click', function() {
  labelElement.classList.toggle("colors")
  if (labelElement.classList.contains("colors") && labelElementTwo.classList.contains("colors")) {
    labelElementTwo.classList.toggle("colors")
  }

});

inputElementEmail.addEventListener('click', function(){
  LabelElementEmail.classList.toggle("colors")
  if (labelElement.classList.contains("colors")){
    labelElement.classList.toggle("colors")}
});

inputElementTwo.addEventListener('click', function() {
  labelElementTwo.classList.toggle("colors")
  if (LabelElementEmail.classList.contains("colors")) {
    LabelElementEmail.classList.toggle("colors")
  }
    
  });



/*
// Añadimos un evento click al input
inputElement.addEventListener('click', function() {
  // Cambiamos el color del label a amarillo (o el color que desees)
  labelElement.classList.toggle("colors")
  labelElementTwo.classList.toggle("colors")
});


inputElementTwo.addEventListener('click', function() {
  // Cambiamos el color del label a amarillo (o el color que desees)

  labelElementTwo.classList.toggle("colors")
});
*/

// Script que cambia el tipo de la etiqueta password y el texto del boton que lo cambia

const mostrar = document.getElementById('togglePassword');
const password = document.getElementById('password')

mostrar.addEventListener('click', function () {
  const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
  password.setAttribute('type', type)
  mostrar.textContent = type === 'password' ? 'Mostrar contraseña' : 'Ocultar contraseña';
});