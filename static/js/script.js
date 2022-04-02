document.addEventListener('DOMContentLoaded', () => {

    const btnMobile = document.getElementById("btn-mobile");

    function toggleMenu(event) {
        if (event.type === 'touchstart') {
            event.preventDefault();
        }
        const nav = document.getElementById('nav');
        nav.classList.toggle('active');
        const active = nav.classList.contains('active');
        event.currentTarget.setAttribute('aria-expanded', active);

        if (active) {
            event.currentTarget.setAttribute('aria-label', 'Close menu')
        } else {
            event.currentTarget.setAttribute('aria-label', 'Open menu')
        }
    }

    btnMobile.addEventListener('click', toggleMenu);
    btnMobile.addEventListener('touchstart', toggleMenu);


    $('.current_year').text(new Date().getFullYear());

});

function changeImage(imgs) {
    let expandImg = document.getElementById("first");
    expandImg.src = imgs.src;
    expandImg.parentElement.style.display = "flex";
}