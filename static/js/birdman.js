(function($) {
		  
		  
    // preload.LOAD FUNCTION start
    $(window).load(preLoader);
    "use strict";

    function preLoader() {
        setTimeout(function() {
            $('#preload').delay(250).fadeOut(1500);
            $('.borders').delay(2400).css({
                display: 'none'
            }).fadeIn(3000);
            $('.cycle-it-home').delay(2400).css({
                display: 'none'
            }).fadeIn(3000);
            $('.cycle-it').delay(2400).css({
                display: 'none'
            }).fadeIn(3000);
            $('h1').delay(2400).css({
                display: 'none'
            }).fadeIn(3000);
            $('.menu').delay(2400).css({
                display: 'none'
            }).fadeIn(3000);
            $('#subscribe-wrapper').delay(2400).css({
                display: 'none'
            }).fadeIn(3000);
            $('canvas').delay(2400).css({
                display: 'none'
            }).fadeIn(3000);
            $('#countdown-wrapper').delay(2400).css({
                display: 'none'
            }).fadeIn(3000);
        });
		
    };
    // preload.LOAD FUNCTION end
	
	
	// WINDOW.LOAD FUNCTION start
    $(window).load(function() {
        "use strict";
		
        // flexSlider
        $('.flexslider').flexslider({
            animation: "fade",
            controlNav: false,
            directionNav: false,
            slideshowSpeed: 4800,
            animationSpeed: 800
        });
		
		// screen loader
        $('.screen-loader').fadeOut('slow');
		
    });
    // WINDOW.LOAD FUNCTION end
	
	
    // DOCUMENT.READY FUNCTION start
    $(document).ready(function() {
        "use strict";
		
        // preload
        $('#preload').css({
            display: 'table'
        });
		
		// kenburnsy
        $("#kenburnsy-bg").kenburnsy({
            fullscreen: true
        });
		
        // countdown setup start
        $("#countdown").countdown({
            date: "09 April 2016 12:00:00", // countdown target date settings
            format: "on"
        }, function() {
            // callback function
        });
		
        // fire
        // fire home
        $("#fire-home").on("click", function(e) {
            e.preventDefault();
            $(".current").fadeOut(1200, function() {
                $(".upper-page").fadeIn(2200);
                $(".current").removeClass("current");
                $(".upper-page").addClass("current");
            });
        });
        // fire about
        $("#fire-about").on("click", function(e) {
            e.preventDefault();
            $(".current").fadeOut(1200, function() {
                $("#about").fadeIn(2200);
                $(".current").removeClass("current");
                $("#about").addClass("current");
            });
        });
        // fire services
        $("#fire-services").on("click", function(e) {
            e.preventDefault();
            $(".current").fadeOut(1200, function() {
                $("#services").fadeIn(2200);
                $(".current").removeClass("current");
                $("#services").addClass("current");
            });
        });
        // fire contact
        $("#fire-contact").on("click", function(e) {
            e.preventDefault();
            $(".current").fadeOut(1200, function() {
                $("#contact").fadeIn(2200);
                $(".current").removeClass("current");
                $("#contact").addClass("current");
            });
        });
		
		// menu active state
        $('a.menu-state').on("click", function() {
            $('a.menu-state').removeClass("active");
            $(this).addClass("active");
        });
		
        // niceScroll
        $("body").niceScroll({
            cursorcolor: "#fff",
            cursorwidth: "5px",
            cursorborder: "1px solid #fff",
            cursorborderradius: "0px",
            zindex: "9999",
            scrollspeed: "60",
            mousescrollstep: "40"
        });
		
        // niceScroll || scrollbars resize
        $("body").getNiceScroll().resize();
		
        // CharCycle
        $('.cycle-it-home, .cycle-it').mouseenter(function() {
            if ($(this).hasClass('cycling') == false) {
                $(this).charcycle({
                    'target': '.cycle-text'
                });
            }
        });
		
        // YTPlayer
        $(".player").mb_YTPlayer();
		
    });
    // DOCUMENT.READY FUNCTION end
	
	
    // navigation.HEIGHT start
    function screen_height() {
        height = $(window).height();
        $('.main-nav').css('padding-top', height / 2.5)
    }
	// navigation.HEIGHT end
	
	// navigation.LOAD FUNCTION start
    $(window).load(function() {
        screen_height()
    });
    // navigation.LOAD FUNCTION end
	
	// navigation.RESIZE FUNCTION start
    $(window).resize(function() {
        screen_height()
    });
    // navigation.RESIZE FUNCTION end
	
	    // navigation.EXECUTION start
        $('.btn-nav').on("click", function(e) {
            e.preventDefault();
            $(this).toggleClass('closer');
            $('nav').toggleClass('show')
        });
        $('.main-nav a').on("click", function(e) {
            var hash = $(this.hash);
            $('nav').removeClass('show');
            $('.btn-nav').removeClass('closer');
            e.preventDefault()
        });
        // navigation.EXECUTION end
	
	
    // MOBILE DETECT start
    var isMobile = {
        Android: function() {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function() {
            return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        }
    };
	// MOBILE DETECT end
	
	
})(jQuery);