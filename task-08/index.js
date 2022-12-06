let playW = () => new Audio("sounds/crash.mp3").play()
let playA = () => new Audio("sounds/kick-bass.mp3").play()
let playS = () => new Audio("sounds/snare.mp3").play()
let playD = () => new Audio("sounds/tom-1.mp3").play()
let playJ = () => new Audio("sounds/tom-2.mp3").play()
let playK = () => new Audio("sounds/tom-3.mp3").play()
let playL = () => new Audio("sounds/tom-4.mp3").play()

document.addEventListener('keydown', function(e) {
    if (e.keyCode == 87) {
        var audio = new Audio("sounds/crash.mp3").play();
    }
});

document.addEventListener('keydown', function(e) {
    if (e.keyCode == 65) {
        var audio = new Audio("sounds/kick-bass.mp3").play();
    }
});

document.addEventListener('keydown', function(e) {
    if (e.keyCode == 83) {
        var audio = new Audio("sounds/snare.mp3").play();
    }
});

document.addEventListener('keydown', function(e) {
    if (e.keyCode == 68) {
        var audio = new Audio("sounds/tom-1.mp3").play();
    }
});

document.addEventListener('keydown', function(e) {
    if (e.keyCode == 74) {
        var audio = new Audio("sounds/tom-2.mp3").play();
    }
});

document.addEventListener('keydown', function(e) {
    if (e.keyCode == 75) {
        var audio = new Audio("sounds/tom-3.mp3").play();
    }
});

document.addEventListener('keydown', function(e) {
    if (e.keyCode == 76) {
        var audio = new Audio("sounds/tom-4.mp3").play();
    }
});
