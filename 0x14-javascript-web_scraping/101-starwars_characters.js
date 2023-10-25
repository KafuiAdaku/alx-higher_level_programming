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

    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
        } else if (response.statusCode !== 200) {
          console.error(response && response.statusCode);
        } else {
          const characterData = JSON.parse(body);
          const characterName = characterData.name;
          console.log(`${characterName}`);
        }
      });
    });
  }
});
