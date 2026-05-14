# Ubuntu Homelab

## Overview

This repository documents the development of my personal Ubuntu-based cybersecurity homelab. The purpose of this project is to strengthen practical skills in Linux administration, networking, cybersecurity operations, scripting, containerization, vulnerability analysis, and AI-assisted workflows through hands-on experimentation and documentation.

The homelab serves as an environment for testing tools, performing network analysis, developing Python utilities, exploring Docker containers, and studying modern cybersecurity concepts in a controlled and ethical setting.

---

## Current Environment

### Operating System
- Ubuntu Linux

### Development Tools
- Visual Studio Code
- Git & GitHub
- Python 3
- Pip & Virtual Environments

### Containerization & Virtualization
- Docker
- Portainer
- OWASP Juice Shop Container

### Networking & Security Tools
- Nmap
- Wireshark
- Recon-ng
- Metasploit Framework
- Lynis

### Password Auditing & Security Testing
- John the Ripper Jumbo
- Hashcat
- Hydra
- sqlmap

### AI & Automation
- Ollama
- Local Llama3 Model
- Open WebUI
- Continue VS Code Extension

---

## Repository Structure

```text
ubuntu-homelab/
├── docker/
├── nmap-scans/
├── notes/
├── python-tools/
├── wireshark/
└── README.md
```

---

## Current Learning Focus

- Linux administration
- Docker container management
- Network scanning and enumeration
- Web application security
- Vulnerability analysis
- Password auditing
- OSINT and reconnaissance workflows
- AI-assisted local development
- Python scripting and automation

---

## Docker Services

| Service | Port |
|---|---|
| Open WebUI | 3000 |
| OWASP Juice Shop | 3001 |
| Portainer | 8000 / 9443 |

---

## Example Tools & Commands

### Nmap Service Scan
```bash
nmap -sV localhost
```

### Docker Container Inspection
```bash
docker inspect juice-shop
```

### Metasploit Port Scanner
```bash
use auxiliary/scanner/portscan/tcp
```

### Hashcat MD5 Test
```bash
hashcat -m 0 hash.txt rockyou.txt
```

---

## Notes

This homelab is intended strictly for ethical learning, defensive security research, authorized testing, and personal skill development.