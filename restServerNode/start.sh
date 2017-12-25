#!/bin/bash

port_start=3000
port_num=5
let port_max=$port_start+$port_num

for ((port=$port_start; port < $port_max; port++)); do
    echo $port
    npm start $port &
done



