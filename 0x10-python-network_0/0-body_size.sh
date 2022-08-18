#!/bin/bash
# sends a request to that URL, and displays the size 
curl -sI "$1" | grep "Content-Length:"| cut -d' ' -f2
