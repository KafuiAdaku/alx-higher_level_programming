#!/bin/bash
# Send a request to 0.0.0.0:5000/catch_me to trigger the desired response
curl -s 0.0.0.0:5000/catch_me | grep -o "You got me!"
