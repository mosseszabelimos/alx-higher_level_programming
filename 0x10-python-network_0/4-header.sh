#!/bin/bash
# write a bash script that takes in URL to  send custom headers to servers
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
