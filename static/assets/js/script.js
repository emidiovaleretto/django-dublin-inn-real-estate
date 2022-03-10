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

var options = {
    weekday: 'long', 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
};
var date = new Date();
let today = date.toISOString().slice(0,10);
document.getElementById("time-description").innerHTML = date.toLocaleDateString("en-US", options);
document.getElementById("appointment-date").setAttribute("value", today);
