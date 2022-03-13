let close = document.getElementById('pop-close');
let pop = document.getElementById('create');
let show = document.getElementById('show');
let flash = document.getElementById('closemsg');
let flashparent = document.getElementById('flashed');

flash.addEventListener('click', () => {
    flashparent.style.display = 'none';
});

close.addEventListener('click', () => {
    pop.classList.toggle('none');
});

show.addEventListener('click', () => {
    pop.classList.toggle('none');

});