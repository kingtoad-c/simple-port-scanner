# 🛰️ Python Port Scanner

A simple Python script that scans a target IP address over a range of ports and identifies open ports.  
Built using the `socket` library — perfect for beginners learning networking basics!

---

## 🚀 Features
- Scan a specific IP address.
- Choose any range of ports to scan.
- Displays open ports in real-time.
- Gracefully handles interruptions and errors.

---

## 📜 Requirements
- Python 3.x

No external libraries needed!

---

## 🛠️ How to Use

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```

2. **Run the script:**

```bash
python3 port_scanner.py
```

3. **Follow the prompts:**
- Enter the target IP address.
- Enter the port range (e.g., `20-80`).

---

## 💻 Example

```text
Enter target IP address: 192.168.1.1
Enter port range (e.g., 20-80): 20-30
Port 22 is OPEN
Port 23 is OPEN
```

---

## ⚡ Notes
- **Timeout** is set to 1 second per port scan for quicker results.
- Make sure you have permission to scan the target IP. Unauthorized scanning may be illegal!
- To stop scanning anytime, press `Ctrl + C`.

---

## 🛡️ Disclaimer
This tool is intended for **educational purposes only**.  
Use it responsibly and only on networks you own or have explicit permission to scan.

---

## ✨ Future Improvements
- Add threading for faster scans
- Auto-detect open services (e.g., SSH, HTTP)
- Scan multiple IP addresses
