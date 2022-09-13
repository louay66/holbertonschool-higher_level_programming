#!/usr/bin/node
const axios = require('axios');
axios.get(process.argv[2])
  .then((response) => {
    console.log('code: %d', response.status);
  })
  .catch((error) => {
    if (error.response) {
      console.log('code: %d', error.response.status);
    }
  });
