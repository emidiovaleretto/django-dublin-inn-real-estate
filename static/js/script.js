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

const galery = document.querySelectorAll(".property-image img");
const galeryContainer = document.querySelector(".property-image");

galery.forEach((img) => {
    img.addEventListener("click", (event) => {
        let img = event.currentTarget;
        let media = matchMedia("(min-width: 940px)").matches;

        if (media) {
            galeryContainer.prepend(img)
        }
    })
});