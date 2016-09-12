//Loads the contents based on file name i
function reload(i, file_list) {
    $('#body-section').load('Scripts/' + file_list[i]);
}

/**************************************************************************
On page load first get the file names and put them on a sorted list. Then
check is if cookies have stored file index i.e. so that person doesn't lose
their place using getCookie. Load the html content of this ith file to the
body of blog.html. Finally if user wants to go back or to the front they
can by selecting the buttons.
**************************************************************************/
$(document).ready(function () {
    $.get("Scripts/", function (data) {
        var file_list = $(data).find('#files').text();
        file_list = file_list.split('\n').sort();
        var i = getCookie("i_value");
        if (i == "" || i == 0) {
            i = file_list.length - 1;
        }
        file_list = file_list.filter(function (data) {
            if (data.search('.html') != -1) {
                return true;
            }
            return false;
        });
        console.log(file_list);
        reload(i, file_list);
        setCookie("i_value", i, 1);
        $('#newer').click(function () {
            i++;
            if (i <= file_list.length) {
                setCookie("i_value", i, 1);
                reload(i, file_list);
            } else {
                alert('This is already the latest post!');
            }
        });
        $('#older').click(function () {
            i--;
            if (i >= 1) {
                setCookie("i_value", i, 1);
                reload(i, file_list);
            } else {
                alert('This is already the oldest post!');
            }
        });
    });

});
