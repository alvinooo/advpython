#!/bin/bash
# curl_get.sh - curl to test GET

echo test GET with curl
curl -i http://localhost:5000/bookcatalog/api/json/books
