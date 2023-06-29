#!/bin/bash
# write a bash script that sends a delete request to the url passed and displays reponse
curl -s -X DELETE "$1"
