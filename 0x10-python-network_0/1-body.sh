#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
status=$(curl -sL -o /dev/null -w "%{http_code}" "$1") && [ "$status" -eq 200 ] && curl -sL "$1"
