# Cybersecurity

A collection of my cybersecurity learning journey, featuring notes, experiments, scripts, tools, and hands-on projects covering ethical hacking, penetration testing, networking, and information security.

> ⚠️ **Disclaimer:** Everything in this repository is for **educational purposes only**. Only run these tools against networks and systems you own or have explicit written permission to test. Unauthorized scanning or attacks are illegal and unethical.

## Topics

- **Ethical Hacking**: techniques, methodologies, and practice labs
- **Penetration Testing**: reconnaissance, enumeration, exploitation, and reporting
- **Networking**: protocols, packet crafting, traffic analysis, and network discovery
- **Information Security**: core concepts, defensive practices, and hardening

## Repository Structure

```
cybersecurity/
├── encrypt-network/
│   ├── scan_network.py     # ARP scanner that lists devices on a local network
│   └── requirements.txt
└── README.md
```

## Projects

### Network Scanner (`encrypt-network/`)

A small Python script built with [Scapy](https://scapy.net/) that sends ARP requests across a subnet and lists every device that responds, showing its IP and MAC address.

**Setup**

```bash
cd encrypt-network
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Usage**

Sending raw packets requires elevated privileges:

```bash
sudo venv/bin/python scan_network.py
```

When prompted, enter the network range in CIDR notation:

```
Enter the network (192.168.1.0/24): 192.168.1.0/24
192.168.1.1      aa:bb:cc:dd:ee:ff
192.168.1.23     11:22:33:44:55:66
```

## Requirements

- Python 3.8+
- `pip` and `venv`
- Root or administrator privileges for tools that send raw packets

## Learning Resources

- [OWASP](https://owasp.org/)
- [TryHackMe](https://tryhackme.com/)
- [Hack The Box](https://www.hackthebox.com/)
- [Scapy Documentation](https://scapy.readthedocs.io/)

## Contributing

This is a personal learning repository, but suggestions and feedback are welcome. Feel free to open an issue or submit a pull request.

## Author

**Fernando Vázquez Medina**: [@fernandovmedina](https://github.com/fernandovmedina)
