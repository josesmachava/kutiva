$(document).ready(function(){
 $.ajaxSetup({ cache: false });
 $('#search').keyup(function(){
  $('#result').html('');
  $('#state').val('');
  var searchField = $('#search').val();
  var expression = new RegExp(searchField, "i");
  $.getJSON('http://localhost:8000/api/courses/?format=json', function(data) {
   $.each(data, function(key, value){
    if (value.name.search(expression) != -1 || value.description.search(expression) != -1)
    {
     $('#result').append('<li class="list-group-item link-class"><a href="http://localhost:8000/cms/details/'+value.id+'" ><img src="'+value.image+'" height="40" width="40" class="img-thumbnail" /> '+value.name+' |</li></a>');
    }else{
          $('#result').append('<li class="list-group-item link-class">Pesquisa não encontrada</li>');

    }
   });
  });
 });
 $.ajaxSetup({ cache: false });
 $('#mobile-search').keyup(function(){
  $('#mobile-result').html('');
  $('#state').val('');
  var searchField = $('#mobile-search').val();
  var expression = new RegExp(searchField, "i");
  $.getJSON('http://localhost:8000/api/courses/?format=json', function(data) {
   $.each(data, function(key, value){
    if (value.name.search(expression) != -1 || value.description.search(expression) != -1)
    {
     $('#mobile-result').append('<li class="list-group-item link-class"><a href="http://localhost:8000/cms/details/'+value.id+'" ><img src="'+value.image+'" height="40" width="40" class="img-thumbnail" /> '+value.name+' |</li></a>');
    }else{
          $('#mobile-result').append('<li class="list-group-item link-class">Pesquisa não encontrada</li>');

    }
   });
  });
 });


});
