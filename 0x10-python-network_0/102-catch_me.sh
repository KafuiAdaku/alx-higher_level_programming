#!/bin/bash
# Send a request to 0.0.0.0:5000/catch_me to trigger the desired response
curl -s -X PUT -L -d "user_id=98" "0.0.0.0:5000/catch_me" -H "Origin: HolbertonSchool"
