#!/bin/bash
# curl_post.sh - curl to test POST

echo test POST with curl

curl -u asgteach:python -i -H "Content-Type:application/xml" -X POST -d '<book><author>Zola, Emile</author><title>Masterpiece</title><notes>Literary Fiction</notes></book>' http://localhost:5000/bookcatalog/api/xml/books

