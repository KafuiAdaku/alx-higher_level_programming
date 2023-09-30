#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
status=$(curl -s -o /dev/null -w "%{http_code}" "$1") && [ "$status" -eq 200 ] && curl -s "$1"
