$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for(var i = 0 ; i < data.count ; i++)
  {
   $('<li>' + data.results[i].title + '</li>').appendTo('UL#list_movies');;
  }
});
