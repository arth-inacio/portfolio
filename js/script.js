const menuHamburguer = document.querySelector('.menu-hamburguer');
menuHamburguer.addEventListener('click', () => {
    toggleMenu();
});

function toggleMenu() {
    const nav = document.querySelector('.nav-responsive');
    menuHamburguer.classList.toggle('change');

    nav.style.display = 'none';
    if (menuHamburguer.classList.contains('change')){
        nav.style.display = 'block';

    }

}