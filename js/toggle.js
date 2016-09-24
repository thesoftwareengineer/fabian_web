$(document).ready(function () {
    $("#logo-toggle").click(function () {
        var visibility = document.getElementsByClassName("navbar-brand").getAttribute("visibility");
        if (visibility == "hidden") {
            $(".navbar-brand").css("visibility", "visible");
        } else {
            $(".navbar-brand").css("visibility", "hidden");
        }
    });
});
