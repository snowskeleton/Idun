#!/bin/bash

curl -X GET http://127.0.0.1:5000/api/fetchTicketInfo -H "Content-Type: application/json" -d '{ "_id": 3 }'
