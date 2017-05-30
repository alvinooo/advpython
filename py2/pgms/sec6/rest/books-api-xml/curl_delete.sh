#!/bin/bash
# curl_delete.sh - curl to test delete

echo test delete with curl
curl -u asgteach:python -i -X DELETE http://localhost:5000/bookcatalog/api/xml/books/104
