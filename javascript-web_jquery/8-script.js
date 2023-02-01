#!/usr/bin/node
// a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $('ul#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
