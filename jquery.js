$(document).ready(function () {
     var el = $('#intro');
     var el1 = $('#intro-content');
           
        //run on scroll
        $(window).scroll(function () {
            var el = $('#intro'); // important! (local)
            var el1 = $('#intro-content'); // important! (local)
            var el2 = $('#button_1');

            var elpos = el.offset().top-$(window).scrollTop(); // take current situation
            var elpos1 = el1.offset().top-$(window).scrollTop(); // take current situation
            var elpos2 = el2.offset().top-$(window).scrollTop(); // take current situation
            
            var winhigh = window.innerHeight;
            if(elpos>0&&elpos<winhigh)
            {
                el.stop().animate({"marginLeft": 0+"px" }, "slow" );
                
            }
            else 
            {
                el.stop().animate({"marginLeft": -el.width()+"px" }, "slow" );
                
            }
            
             if(elpos1>0&&elpos1<winhigh)
            {
                
                el1.stop().animate({"marginLeft": 0.2*window.innerWidth+"px" }, "slow" );
                
            }
            else 
            {
               el1.stop().animate({"marginLeft": window.innerWidth+"px" }, "slow" );
                 
            }

            if(elpos2>0&&elpos2<winhigh)
            {
                el2.stop().animate({"marginTop": 20+"px" }, "slow" );
                
            }

        });
    });