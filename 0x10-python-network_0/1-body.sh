#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -Ls -I -X 'GET' "$1" | grep -q "200 OK" && curl -s -L -X "GET" "$1"
