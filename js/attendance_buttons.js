var images = ['../img/b_green.png', '../img/b_yellow.png', '../img/b_red.png'],
i = 0;

    // preload
for (var j=images.length; j--;) {
    var img = new Image();
    img.src = images[j];
}


var buttons = document.getElementsByClassName("attendance_button")

for (var i=buttons.length; i--;) {
    buttons[i].addEventListener('click', function() { this.src = images[i >= images.length - 1 ? i = 0 : ++i];}
, false);
}
