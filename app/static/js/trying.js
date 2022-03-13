let close = document.getElementById('pop');
let pop = document.getElementById('create');
let show = document.getElementById('btn');

let close2 = document.getElementById('pop2');
let pop2 = document.getElementById('create2');
let show2 = document.getElementById('com');


show.addEventListener('click', () => {
    pop.classList.toggle('none');
});
close.addEventListener('click', () => {
    pop.classList.toggle('none');
});
show2.addEventListener('click', () => {
    pop2.classList.toggle('none');
});
close2.addEventListener('click', () => {
    pop2.classList.toggle('none');
});