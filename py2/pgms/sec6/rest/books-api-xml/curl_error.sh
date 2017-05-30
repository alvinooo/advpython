#!/bin/bash
# curl_error.sh - curl to test Not Found

echo test Not Found with curl
curl -i http://localhost:5000/bookcatalog/api/xml/books/200
