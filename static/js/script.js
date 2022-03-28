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


    let options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    };
    let date = new Date();
    let today = date.toISOString().slice(0, 10);
    document.getElementById("time-description").innerHTML = date.toLocaleDateString("en-US", options);
    document.getElementById("appointment-date").setAttribute("value", today);

});

function changeImage(imgs) {
    let expandImg = document.getElementById("first");
    expandImg.src = imgs.src;
    expandImg.parentElement.style.display = "flex";
}