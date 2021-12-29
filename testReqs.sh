#!/bin/bash

curl -X GET http://127.0.0.1:5000/api/fetchTicketInfo -H "Content-Type: application/json" -d '{ "_id": 5 }'
curl -X POST http://127.0.0.1:5000/api/createNewTicket -H "Content-Type: application/json" -d '{ "customer": "Randolph", "serialNumber": "T", "modelNumber": "456", "assetTag": "george" }'


curl -X POST http://127.0.0.1:5000/api/fetchTicketInfo -H \
{
	"_id": 2,
	"parts": [
		{
			"name": "LCD",
			"ordered": false,
			"replaced": false,
			"cost": 29.99
		},
		{
			"name": "Motherboard",
			"ordered": false,
			"replaced": false,
			"cost": 100.00
		},
		{
			"name": "Keyboard",
			"ordered": false,
			"replaced": false,
			"cost": 49.99
		}
	]
}



# {
# 	"_id": 3,
#    	"device": {
# 		"serialNumber": "1234098",
# 		"modelNumber": "somethingClever",
# 		"assetTag": "2358"
# 	},
# 	"ticketNumber": {
# 		"$numberInt": "48"
# 	}
# }