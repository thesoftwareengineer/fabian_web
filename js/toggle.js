$(document).ready(function () {
    $("#logo-toggle").click(function () {
        var visibility = $('.navbar-brand').css('visibility');
        if (visibility == "hidden") {
            $(".navbar-brand").css("visibility", "visible");
        } else {
            $(".navbar-brand").css("visibility", "hidden");
        }
    });
});
