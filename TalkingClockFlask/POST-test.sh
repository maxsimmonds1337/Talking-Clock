#!/bin/sh
curl -X POST -H "Content-Type: application/json" -d '{
  "time": "10:10",
}' http://localhost:5000/