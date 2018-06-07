const NUM_PHOTOS = 3;
const IMAGE_WIDTH = 1000;
let currentPhoto = 0;

const photoreel = document.getElementsByClassName('photoreel')[0];

function showNextPhoto() {
    currentPhoto = (currentPhoto + 1) % NUM_PHOTOS;
    photoreel.scroll({left: IMAGE_WIDTH * currentPhoto, behavior: 'smooth'});
}

window.setInterval(showNextPhoto, 10000);

