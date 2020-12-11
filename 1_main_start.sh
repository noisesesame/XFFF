#!/bin/bash

tcpdump -i [ Your network interface name ] port 80 or 8080 -G 300 -w z_log_%Y-%m-%d_%H:%M:%S.pcap -Z root &

./main_src > /dev/null 2>&1 &

