#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', charResponse.statusCode);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
