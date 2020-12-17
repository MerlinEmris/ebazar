$(document).ready(function() {

    // $("#owl-list").owlCarousel({
    //     items : 4,
    //     lazyLoad : true,
    //     navigation : true
    // });
    // $("#owl-list2").owlCarousel({
    //     items : 4,
    //     lazyLoad : true,
    //     navigation : true
    // });

    // $("#owl-lazy").owlCarousel({
    //     items : 4,
    //     lazyLoad : true,
    //     navigation : true
    // });
    //---------------------reach the end of page-------------------------
    $(window).scroll(function() {
        if($(window).scrollTop() + $(window).height() == $(document).height()) {
            // alert("bottom!");
        }
    });

    //----------------------------- lazy jquary plugin----------------------
    /*$(function() {
        $('.lazy').lazy({
            placeholder: "img/loading.gif"
        });
    });*/
    //--------------------------------------flickity--------------------------
    $('.main-gallery').flickity({
        // options
        cellAlign: 'left',
        contain: true,
        lazyLoad: false,
        adaptiveHeight: true,
        autoPlay: 1500,
        wrapAround: false
    });
    $('.category-carousel').flickity({
        groupCells: true,
        contain:true,
        adaptiveHeight: false,
    });
    //----------------------------birdman----------------------------
    // $('.birdman').birdman();
    //--------------------------- parallax---------------------------
    //$('.parallax-window').parallax({imageSrc: '/path/to/image.jpg'});
});