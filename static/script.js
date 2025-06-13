
// contact 
document.addEventListener("DOMContentLoaded", function () {
    gsap.from(".contact-section h2", { opacity: 0, y: -20, duration: 1 });
    gsap.from(".contact-section p", { opacity: 0, y: 20, duration: 1, delay: 0.3 });
    gsap.from(".input-group", { opacity: 0, y: 30, duration: 1, stagger: 0.2, delay: 0.5 });
    gsap.from(".submit-btn", { opacity: 0, scale: 0.9, duration: 1, delay: 1 });

});

document.querySelector('.slideshow-wrapper').style.cssText = 'opacity: 1; visibility: visible';
document.querySelector('.slideshow').style.animation = 'slideshow 24s infinite';


