/**
 * Created by sebm on 24.02.17.
 */
document.onkeypress = keyPress;

function pressEnter(e){
  var x = e || window.event;
  var key = (x.keyCode || x.which);
    if(key == 13 || key == 3){
     //  myFunc1();
     document.onEnterKey.submit();
    }
    }