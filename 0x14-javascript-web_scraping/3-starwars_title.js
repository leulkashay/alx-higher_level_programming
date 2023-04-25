#!/usr/bin/node
const request = require('request');
cinst url = "https://swapi-api.alx-tools.com/api/films/:id" + processargv[2]
request(url, function(error, response, body) {
    console.log(error || JSON.parse(body).title);
});
