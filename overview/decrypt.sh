#!/bin/bash

if [  $# -le 1 ]
then 
  echo "Usage: $0 <problem> <key>"
  exit 1
fi 

openssl enc -in "$1".enc -out "$1".pdf -d -k "$2" -md sha1 -aes-256-cbc

