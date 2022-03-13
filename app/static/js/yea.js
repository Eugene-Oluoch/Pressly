let popClose = document.getElementById('pop-close');
let create = document.getElementById('create');
let showform = document.getElementById('show');

showform.addEventListener('click', () => {
    create.classList.toggle('none');
});

popClose.addEventListener('click', () => {
    create.classList.toggle('none');
});