#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode !== 200) {
    console.error(response && response.statusCode);
  } else {
    const data = JSON.parse(body);
    const characterUrls = data.characters;

    fetchCharacter(0);

    function fetchCharacter (index) {
      if (index === characterUrls.length) {
        return;
      }

      request(characterUrls[index], (err, response, body) => {
        if (err) {
          console.error(err);
          return;
        }
        if (response.statusCode !== 200) {
          console.error(response && response.Status);
          return;
        }
        const character = JSON.parse(body);
        console.log(character.name);
        fetchCharacter(++index);
      });
    }
  }
});
