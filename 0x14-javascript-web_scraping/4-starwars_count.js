#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const characterId = '18';
let count = 0;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode !== 200) {
    console.error(response && response.statusCode);
  } else {
    const filmsData = JSON.parse(body);
    const results = filmsData.results;

    for (const result of results) {
      const characters = result.characters;
      for (const character of characters) {
        if (character.includes(characterId)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
