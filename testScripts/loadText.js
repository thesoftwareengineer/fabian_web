$(document).ready(function () {
    var file_to_get = ""
    $.get("Scripts/", function (data) {
        var file_list = $(data).find('#files').text();
        file_list = file_list.split('\n').sort()
        console.log('Scripts/' + file_list[file_list.length - 2]);
        var file = 'Scripts/' + file_list[file_list.length - 2];
        $.ajax({
            url: file,
            success: function (result) {
                result_id = $(result).filter('#body-section');
                console.log(result_id.text())
                $("#posts").append('<p>' + result_id.text() + '</p>');
            }
        });
        file = 'Scripts/' + file_list[file_list.length - 3];
        $.ajax({
            url: file,
            success: function (result) {
                result_id = $(result).filter('#body-section');
                console.log(result_id.text())
                $("#posts").append('<a>' + result_id.text() + '</a>');
            }
        });
    });
});
