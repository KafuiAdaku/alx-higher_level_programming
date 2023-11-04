$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json',
    (data) => {
      const films = data.results;
      $.each(films, (film) => {
        $('#list_movies').append('<li>' + film + '</li>');
      });
    });
});
