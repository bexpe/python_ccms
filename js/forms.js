function buttonclick(name){
    /*
     shows Modal on website
     make sure the id of button is the beginning od id of modal div and add "_Modal"
     span inside modal should be named as "close_" and name added
     */

// Get the modal
    var modal = document.getElementById(name+"_Modal");

// Get the button that opens the modal
    var btn = document.getElementById(name);

// Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close_"+name)[0];

    // When the user clicks the button, open the modal
    modal.style.display = "block";

// When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    };

// When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}