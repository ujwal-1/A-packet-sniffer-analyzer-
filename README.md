# Network Packet Analyzer

A real-time network packet capture and analysis tool built with Python (Scapy) and Flask.

## What it does
- Captures live network traffic from your network interface
- Identifies TCP, UDP, and ICMP packets
- Extracts source IP, destination IP, protocol, length, and timestamp
- Displays packets in real time through a web-based dashboard

## Tech Stack
- Python 3
- Scapy (packet capture)
- Flask (backend API)
- HTML/CSS/JavaScript (frontend dashboard)

## How to run
pip install -r requirements.txt
sudo python3 app.py

Then open your browser at http://localhost:5000

## What I learned
- How packets are structured at the IP/TCP/UDP layer
- How to use Scapy to capture and parse real network traffic
- How to serve live data from a Python backend to a web frontend.
