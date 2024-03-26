# ARP-Scanner

ARP scanner for Linux made in Python

# What is an ARP scanner?

An ARP scanner is a tool used in computer networks to explore and gather information about devices connected to the local network. The main objective of ARP scanning is to map the IP addresses of devices in a local network along with their MAC addresses.

# Usage

For this script we must have certain libraries installed

```
pip3 install scapy textwrap termcolor
```

If we want to run the script we must take into account the "Broadcast address" since not all networks are the same and change, so if you want to improve the arp scanning, you must set your "Broadcast address" correctly. One way to know is to use the following command

```
ip addr show enp0s3
```

![ARP](https://github.com/MT-256/ARP-Scanner/assets/127991386/11695461-053b-408c-bfd7-0b3f91fd02bd)


As we already know that in this case it is /24, we can scan the computers on the network in a better way

```
python3 ARP_Scanner.py -t 172.16.0.0/24
```

![Example](https://github.com/MT-256/ARP-Scanner/assets/127991386/0a7fac46-9d05-48db-a424-900cdfb930ac)
