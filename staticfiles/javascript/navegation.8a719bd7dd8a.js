"use strict";
$('document').ready(function () {
	$( ".settings" ).hide();
	$("main").click(function(){
			$( ".settings" ).hide();


	})
    $('.menuIcon').click(function () {
        $('.mobileMenu').show();
        $('.menuIcon').hide();
    });
    $( ".user-name" ).click(function() {
	  $( ".settings" ).toggle()
	});
    


     $('.closeIcon').click(function () {
        $('.mobileMenu').hide();
        $('.menuIcon').show();
    })


});
