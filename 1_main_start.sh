#!/bin/bash

pkill -9 main_src
pkill -9 python
pkill -9 tcpdump

tcpdump -i [ Your network interface name ] port 80 or 8080 -G 300 -w ./7_pcap/log_%Y-%m-%d_%H_%M_%S.pcap -Z root &

cd ./3_c && ./main_src > /dev/null 2>&1 &

