#!/usr/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, & print bytes
curl -s "$1" |wc -c
