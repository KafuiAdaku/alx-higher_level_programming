#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, async (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode !== 200) {
    console.error(response && response.statusCode);
  } else {
    const data = JSON.parse(body);
    const charactersUrl = data.characters;

    const characterNames = [];

    async function getCharacterName (characterUrl) {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, response, body) => {
          if (err) {
            reject(err);
          } else if (response.statusCode !== 200) {
            reject(response && response.statusCode);
          } else {
            const character = JSON.parse(body);
            characterNames.push(character.name);
            resolve();
          }
        });
      });
    }

    await Promise.all(charactersUrl.map((characterUrl) => getCharacterName(characterUrl)));

    for (const character of characterNames) {
      console.log(character);
    }
  }
});
