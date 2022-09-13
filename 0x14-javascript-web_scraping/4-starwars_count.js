#!/usr/bin/node
const axios = require('axios');
let count = 0;
axios.get(process.argv[2])
  .then((response) => {
    for (let id = 0; id < response.data.count; id++) {
      if (String(response.data.results[id].characters).includes('18')) {
        count = count + 1;
      }
    }
    console.log(count);
  })
  .catch((error) => {
    console.log(error);
  });
