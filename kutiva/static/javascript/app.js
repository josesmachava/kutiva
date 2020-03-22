
$(document).ready(function(){
   //   $('.testimonials').slick();
    $('.search-mobile').hide();
    $('.search-icon').click(function () {
              $('.search-mobile').toggle('slow');
    })
    window.onscroll = function(){
                          $('.search-mobile').hide();

    }
})