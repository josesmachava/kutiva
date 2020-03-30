
$(document).ready(function(){
   //   $('.testimonials').slick();
    //$('.search-mobile').hide();
    $('.user-menu').hide();
    $('.search-icon').click(function () {
              $('.search-mobile').toggle('slow');
    })
    $('.user-icon').click(function () {
              $('.user-menu').toggle();
    })
    window.onscroll = function(){
                          $('.search-mobile').hide();

    }
      window.onscroll = function(){
                          $('.user-menu').hide();

    }
})