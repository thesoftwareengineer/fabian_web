/***********************************************************************
Callback function used by load to make sure that not too many words per
post are shown on the main page. As we only want an intro. Perhaps on
click() of a.more we should add link to blog with i_value sent.
***********************************************************************/
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

/***************************************************************************
Finds names of the latest 3 blog posts then loads them using the callback
function.
***************************************************************************/
$(document).ready(function () {
    $.get("Scripts/", function (data) {
        var file_list = $(data).find('#files').text();
        file_list = file_list.split('\n').sort();
        file_list = file_list.filter(function (data) {
            if (data.search('.html') != -1) {
                return true;
            }
            return false;
        });
        $('#post1').load('Scripts/' + file_list[file_list.length - 1], callback);
        console.log('Srcipts/' + file_list[file_list.length - 1]);
        $('#post2').load('Scripts/' + file_list[file_list.length - 2], callback);
        console.log('Scripts/' + file_list[file_list.length - 2]);
        $('#post3').load('Scripts/' + file_list[file_list.length - 3], callback);
        console.log('Scripts/' + file_list[file_list.length - 3]);
    });
});
