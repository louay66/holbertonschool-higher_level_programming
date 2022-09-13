#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');

axios.get(process.argv[2])
  .then((response) => {
    fs.writeFile(process.argv[3], response.data, 'utf-8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  });
