#!/bin/bash
# write a bash script that takes in URL to post data to a server
curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
