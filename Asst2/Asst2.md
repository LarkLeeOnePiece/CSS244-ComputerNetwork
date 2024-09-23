# CS244 Computer Network Assignment2

## Command

1. Change the algorithm
```
sudo vim /etc/sysctl.conf
```

2. Reload the config
```
sudo sysctl -p
```

3. Show the algorithm
```
sysctl net.ipv4.tcp_congestion_control
```

4. Throughput and Delay
```
iperf3 -c 10.68.75.53 -t 20
iperf3 -c 10.68.75.53 -t 20 -J -i 0.1
```

## 1. TCP congestion control algorithm
### 1.1 TCP BBR
TCP BBR (Bottleneck Bandwidth and RTT) is a congestion control algorithm developed by Google to improve network transmission efficiency. Unlike traditional TCP congestion control algorithms (e.g., TCP Reno or TCP CUBIC), which rely heavily on packet loss and congestion window adjustment, TCP BBR employs a bandwidth and delay (RTT)-based mechanism to estimate the network's bottleneck bandwidth and the minimum RTT in order to dynamically adjust the sending rate.

TCP BBR works by actively detecting the current network state by continuously monitoring the available bandwidth and RTT of the network links and estimating the optimal transmission rate (i.e., bottleneck bandwidth) and the shortest delay (i.e., RTT when there is no queuing) of the network. It then controls the data sending rate based on these .

### 1.2 TCP CUBIC
TCP CUBIC is a congestion control algorithm for the Transmission Control Protocol (TCP) designed to optimize TCP transmission performance in high-bandwidth-latency network environments. It is the default TCP congestion control algorithm in the Linux kernel, and is designed to address the lack of performance of traditional TCP congestion control algorithms in high-bandwidth and high-latency networks

When network congestion is detected (e.g., packet loss), CUBIC decreases the congestion window size and then gradually increases the window as a cubic function. Over time, the growth rate accelerates until the maximum bandwidth utilization is reached. When the network stabilizes, CUBIC recovers the pre-packet-loss state more quickly, thus maintaining higher transmission rates in high-bandwidth-latency networks.

### 1.3 TCP Reno
TCP Reno is a popular congestion control algorithm for the Transmission Control Protocol (TCP) with some improvements over TCP Tahoe.The main goal of TCP Reno is to improve network throughput and efficiently adjust transmission rates when congestion is detected.

TCP Reno controls network traffic through four steps: Slow Start, Congestion Avoidance, Fast Retransmission, and Fast Recovery. TCP Reno controls network traffic through four steps, “Slow Start,” “Congestion Avoidance,” “Fast Retransmission,” and “Fast Recovery,” and adjusts the sending rate to minimize packet loss when congestion is detected.

### 1.4 TCP Vegas
TCP Vegas is a delay-based TCP congestion control algorithm proposed by Brakmo and Peterson in 1994. Unlike the classic TCP Tahoe and TCP Reno, TCP Vegas does not rely on packet loss to detect network congestion, but rather measures delay to predict network congestion. Its core idea is to pre-adjust the sending rate before congestion occurs in order to reduce packet loss and improve network utilization.

##2. Algorithm comparison

### 2.1 Throughput
> Wireless

**BBR**

bbr_bandwidth_data=[85.2, 76.6, 70.4, 62.7, 76.6, 83.0, 76.6, 76.3, 76.6, 76.3, 96.6, 77.6, 96.6, 77.1, 76.3, 83.8, 76.6, 77.3, 83.0, 90.2, 79.8, 79.0]

|  | 1s | 3s | 5s | 7s | 9s | 12s | 15s | 20s | AVG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bandwidth | 85.2 Mbits/s | 70.4 Mbits/s | 76.6 Mbits/s | 76.6 Mbits/s | 76.6 Mbits/s | 96.6 Mbits/s | 76.3 Mbits/s | 90.2 Mbits/s |79.8 Mbits/s |

Cwnd_data=[234.0, 248.0, 240.0, 205.0, 222.0, 251.0, 240.0, 251.0, 234.0, 231.0, 225.0, 237.0, 168.0, 190.0, 185.0, 220.0, 220.0, 231.0, 154.0, 248.0]

|  | 1s | 3s | 5s | 7s | 9s | 12s | 15s | 20s  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cwnd | 234.0 KBytes | 240.0 KBytes | 222.0 KBytes | 240.0 KBytes | 234.0 KBytes | 225.0 KBytes | 185.0 KBytes | 248.0 KBytes 

**CUBIC**

bandwidth_data=[72.6, 85.6, 79.4, 85.8, 35.5, 80.2, 89.2, 85.6, 89.7, 87.9, 83.8, 84.3, 81.7, 79.4, 80.7, 80.9, 81.2, 77.1, 75.3, 76.8, 79.6, 79.5]

|  | 1s | 3s | 5s | 7s | 9s | 12s | 15s | 20s | AVG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bandwidth | 72.6 Mbits/s | 79.4 Mbits/s | 35.5 Mbits/s | 89.2 Mbits/s | 89.7 Mbits/s | 83.8 Mbits/s | 80.7 Mbits/s | 76.8 Mbits/s |79.6 Mbits/s |

Cwnd_data=[64.2, 64.2, 64.2, 64.2, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0]

|  | 1s | 3s | 5s | 7s | 9s | 12s | 15s | 20s  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cwnd | 64.2 KBytes | 64.2 KBytes | 67.0 KBytes | 67.0 KBytes | 67.0 KBytes | 67.0 KBytes | 67.0 KBytes | 67.0 KBytes

### 2.2 delay



**CUBIC**
rtt_cubic：[516, 814, 1576, 1126, 1353, 770, 767, 3808, 870, 554, 2114, 1098, 956, 1925, 790, 526, 2596, 718, 505, 1066]
cwnd_cubic：[65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7, 65.7]
var_cubic:[35, 69, 333, 195, 435, 67, 80, 704, 127, 182, 63, 148, 242, 269, 159, 112, 563, 184, 108, 281]


