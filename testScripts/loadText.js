function callback() {

    var minimized_elements = $('p.post-text');

    minimized_elements.each(function () {
        var t = $(this).text();
        if (t.length < 100) return;

        $(this).html(
            t.slice(0, 100) + '<span>... </span><a href="#" class="more">More</a>' +
            '<span style="display:none;">' + t.slice(100, t.length) + ' <a href="#" class="less">Less</a></span>'
        );

    });

    $('a.more', minimized_elements).click(function (event) {
        event.preventDefault();
        $(this).hide().prev().hide();
        $(this).next().show();
    });

    $('a.less', minimized_elements).click(function (event) {
        event.preventDefault();
        $(this).parent().hide().prev().show().prev().show();
    });

}

$(document).ready(function () {
    $.get("Scripts/", function (data) {
        var file_list = $(data).find('#files').text();
        file_list = file_list.split('\n').sort();
        $('#post1').load('Scripts/' + file_list[file_list.length - 1], callback);
        console.log('Srcipts/' + file_list[file_list.length - 1]);
        $('#post2').load('Scripts/' + file_list[file_list.length - 2], callback);
        console.log('Scripts/' + file_list[file_list.length - 2]);
        $('#post3').load('Scripts/' + file_list[file_list.length - 3], callback);
        console.log('Scripts/' + file_list[file_list.length - 3]);
    });
});
