#!/bin/bash
# display status code
curl -s -w '%{http_code}' "$1" -o /dev/null
