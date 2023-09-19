To use this model:

1. Set up the network toplogy:

    ```
    sudo mn --custom topo.py --topo mytopo
    ```

2. Load the routes:

    ```
    mininet> source setup.mn
    ```

3. Attempt some pings:

    ```
    mininet> serverA ping -c1 192.168.1.10
    PING 192.168.1.10 (192.168.1.10) 56(84) bytes of data.
    64 bytes from 192.168.1.10: icmp_seq=1 ttl=63 time=1.17 ms

    --- 192.168.1.10 ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 1.170/1.170/1.170/0.000 ms
    mininet> serverB ping -c1 192.168.1.10
    PING 192.168.1.10 (192.168.1.10) 56(84) bytes of data.
    64 bytes from 192.168.1.10: icmp_seq=1 ttl=62 time=1.70 ms

    --- 192.168.1.10 ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 1.704/1.704/1.704/0.000 ms
    ```
