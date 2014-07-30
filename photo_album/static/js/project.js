/* Project specific Javascript goes here. */

$(document).ready(function() {
    $("img.img-responsive.img-thumbnail").hover(
        function() { $(this).toggleClass("bg-primary"); });
});
