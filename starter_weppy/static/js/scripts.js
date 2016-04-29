$(document).ready(function($){
    // browser window scroll (in pixels) after which the "back to top" link is shown
    var offset = 300,
    //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
        offsetOpacity = 1200,
    //duration of the top scrolling animation (in ms)
        scrollTopDuration = 700,
    //grab the "back to top" link
        $backToTop = $(".cd-top");

    //hide or show the "back to top" link
    $(window).scroll(function(){
        ( $(this).scrollTop() > offset ) ? $backToTop.addClass("cd-is-visible") : $backToTop.removeClass("cd-is-visible cd-fade-out");
        if( $(this).scrollTop() > offsetOpacity ) {
            $backToTop.addClass("cd-fade-out");
        }
    });

    //smooth scroll to top
    $backToTop.on("click", function(event){
        event.preventDefault();
        $("body,html").animate({
                scrollTop: 0
            }, scrollTopDuration
        );
    });

});