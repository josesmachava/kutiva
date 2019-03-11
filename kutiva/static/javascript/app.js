"use strict"

$('.optionstyle a').click(function(){
    $(this).parent().find('.optionstyle').css('border-bottom','#ffffff');
    $(this).css('border-bottom','3px solid blue');
});
