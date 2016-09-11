function reload(i, file_list) {
    $('#body-section').load('Scripts/' + file_list[i]);
}
$(document).ready(function () {
    $.get("Scripts/", function (data) {
        var file_list = $(data).find('#files').text();
        file_list = file_list.split('\n').sort();
        var i = file_list.length - 1;
        console.log(file_list[i]);
        reload(i, file_list);
        setCookie("i_value", i, 1);
        $('#newer').click(function () {
            i++;
            if (i <= file_list.length) {
                reload(i, file_list);
            } else {
                alert('This is already the latest post!');
            }
        });
        $('#older').click(function () {
            i--;
            if (i >= 1) {
                reload(i, file_list);
            } else {
                alert('This is already the oldest post!');
            }
        });
    });

});
