#!/usr/bin/node
const movieId = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const request = require('request');
request(endpoint, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
