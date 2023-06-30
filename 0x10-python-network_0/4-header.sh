#!/bin/bash
# write a bash script that takes in URL to  send custom headers to servers
curl -s -H "X-School-User-Id: 98" "$1"
