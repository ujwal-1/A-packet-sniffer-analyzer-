# Network Packet Analyzer

A real-time network packet capture tool built with Python (Scapy) and Flask. Captures live traffic from a network interface, classifies packets by protocol, and displays them through a web dashboard.

> The backend packet capture logic is written in Python using Scapy. The frontend dashboard UI was built with AI assistance.

---

## Features

- Live packet capture from your network interface
- TCP, UDP, and ICMP protocol detection
- Source and destination IP extraction with timestamps
- Packet length tracking
- Web-based dashboard to view traffic in real time

---

## Tech Stack

- Python 3 + Scapy — packet capture and processing
- Flask — backend API
- HTML, CSS, JavaScript — frontend dashboard

---

## How to Run

```bash
pip install -r requirements.txt
sudo python3 app.py
```

Open your browser at http://localhost:5000

> sudo is required for raw packet capture access

---

---

## What I Learned

- How packets are structured at the IP, TCP, UDP, and ICMP layers
- How to use Scapy to capture and parse real network traffic
- How to expose live data from a Python backend to a web frontend via Flask

---

> Built for educational purposes. All capture performed on local interfaces only.
