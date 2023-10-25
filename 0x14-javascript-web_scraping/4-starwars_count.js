#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
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
      if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count += 1;
      }
    }
    console.log(count);
  }
});
