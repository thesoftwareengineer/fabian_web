$(document).ready(function () {
    var file_to_get = ""
    $.get("Scripts/", function (data) {
        var file_list = $(data).find('#files').text();
        file_list = file_list.split('\n').sort();
        $.ajax({
            url: 'Scripts/' + file_list[1],
            success: function (result) {
                result_id = $(result).find('#body-section');
                console.log(result_id.text())
                $("#posts").append('<p>' + result_id.text() + '</p>');
            }
        });
        $.ajax({
            url: 'Scripts/' + file_list[3],
            success: function (result) {
                result_id = $(result).find('#body-section');
                console.log(result_id.text())
                $("#posts").append('<a>' + result_id.text() + '</a>');
            }
        });
    });
});
