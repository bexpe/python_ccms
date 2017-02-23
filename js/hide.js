/**
 * Created by bujak on 23.02.17.
 */

window.onload=function()  //executes when the page finishes loading
{
	setTimeout(hide_panda, 5000);  //sets a timer which calls function hide_panda after 5,000 milliseconds = 5 secs.
    setTimeout(show_content, 5000);
};
function hide_panda()
{
	document.getElementById("panda").className="hide";
}
function show_content()
{
	document.getElementById("main_container").className="main_container";
}
