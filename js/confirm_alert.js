/**
 * Created by sebm on 24.02.17.
 */
function confirmAlert() {
    var x;
    if (confirm("Remove - Are you sure?") == true) {
        x = "Remove";
    } else {
        x = "Cancel";
    }

}