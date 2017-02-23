/**
 * Created by bujak on 23.02.17.
 */

window.onload=function()  //executes when the page finishes loading
{
	setTimeout(func1, 5000);  //sets a timer which calls function func1 after 2,000 milliseconds = 2 secs.
    setTimeout(func2, 5000);
};
function func1()
{
	document.getElementById("main_container").className="main_container";
}
function func2()
{
	document.getElementById("panda").className="hide";
}
