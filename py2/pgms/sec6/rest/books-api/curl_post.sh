#!/bin/bash
# curl_post.sh - curl to test POST

echo test POST with curl

curl -u asgteach:python -i -H "Content-Type:application/json" -X POST -d '{"author":"Zola","title":"Germinal","notes":"Literary Fiction"}' http://localhost:5000/bookcatalog/api/json/books

