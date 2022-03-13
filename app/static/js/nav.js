//Js that handles nav functionality
let hamburger = document.querySelector('.hamburger');
let menu = document.querySelector('.nav-menu');


hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    menu.classList.toggle('active');
});