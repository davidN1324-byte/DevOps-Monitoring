#!/bin/bash

SERVER_CONTAINER="iperf-server"
SERVER_IP="172.17.0.2"
PORT="5201"
DURATION="60"
INTERVAL="1"

if [ ! "$(docker ps -q -f name=$SERVER_CONTAINER)" ]; then
  echo "Start iperf server..."
  docker run -d --name $SERVER_CONTAINER -p $PORT:$PORT networkstatic/iperf3 -s
else
  echo "iperf the server is already running."
fi

sleep 10

echo "We launch the load on the server..."
docker run --rm networkstatic/iperf3 -c $SERVER_IP -p $PORT -t $DURATION -i $INTERVAL

echo "We check the metrics data in Prometheus..."
curl -s "http://localhost:9090/api/v1/query?query=rate(node_network_transmit_bytes_total[1m])" | jq .

curl -s "http://localhost:9090/api/v1/query?query=rate(node_network_receive_bytes_total[1m])" | jq .

sleep 10

echo "Checking alerts in Prometheus..."
curl -s "http://localhost:9090/api/v1/alerts" | jq .
