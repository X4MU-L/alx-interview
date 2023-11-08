#!/usr/bin/node
const request = require('request');

const fetchMovie = () => {
  if (process.argv.length < 3) {
    console.error('Program requires an argument');
  } else if (isNaN(process.argv[2])) {
    console.error('Enter a valid id');
  } else {
    getMovieByID(process.argv[2]);
  }
};

const printAllRequest = (requestPromises) => {
  Promise.all(requestPromises)
    .then((prom) => prom.forEach((p) => console.log(JSON.parse(p).name)))
    .catch((err) => console.log(err));
};

const muiltPleCalls = (requestArray) => {
  return requestArray.map((url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, res, body) => {
        if (error) {
          reject(error);
        }
        resolve(body);
      });
    });
  });
};

const getMovieByID = (id) => {
  request(
    `https://swapi-api.alx-tools.com/api/films/${id}/`,
    async (err, res, body) => {
      if (err || res.statusCode !== 200) {
        return;
      }
      const b = await JSON.parse(body);
      const characterRequest = muiltPleCalls(b.characters);
      printAllRequest(characterRequest);
    }
  );
};

fetchMovie();
