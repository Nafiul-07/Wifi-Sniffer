# Wi-Fi Probe Request Sniffer (Educational Only)

This is a basic Python script that listens for Wi-Fi probe requests using `scapy`. It shows which nearby devices are actively looking for Wi-Fi networks (SSIDs).

## 🔒 Legal Disclaimer
This tool is created for **educational and ethical hacking practice only**.  
Do not use this tool on public networks or without permission.  
Test only on your own network or a controlled lab environment.

## 💡 What It Does
- Captures probe request packets from nearby Wi-Fi-enabled devices
- Displays the device's MAC address and the SSID it's searching for

## 🧰 Requirements

- Python 3
- `scapy` library
- A Wi-Fi adapter that supports **monitor mode**
- Linux-based system (like Kali Linux)

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/wifi-sniffer.git
   cd wifi-sniffer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Enable monitor mode on your Wi-Fi card:
   ```bash
   sudo airmon-ng start wlan0
   ```

## ▶️ How to Run

Run the script with `sudo` and the correct wireless interface:

```bash
sudo python sniff_probes.py -i wlan0mon
```

Replace `wlan0mon` with your actual wireless interface in monitor mode.

## 📘 Example Output

```
[+] Device 88:25:93:8a:xx:xx is probing for SSID: HomeWiFi
[+] Device 3c:52:82:4e:xx:xx is probing for SSID: Starbucks_WiFi
```

## ✅ Educational Purpose

This tool helps you understand:
- Passive Wi-Fi sniffing
- MAC addresses
- Wireless reconnaissance techniques

## 🧠 Future Ideas

- Log probe requests to a file
- Count unique devices
- Track SSID popularity

## 👨‍💻 Author

Created by a Cybersecurity Student for learning purposes.

## 🏷️ Tags

`python` `scapy` `wifi` `ethical-hacking` `cybersecurity`
