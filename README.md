# Ubuntu Homelab

## Overview

This repository documents the development of my personal Ubuntu-based cybersecurity homelab. The purpose of this project is to strengthen practical skills in Linux administration, networking, cybersecurity operations, scripting, containerization, vulnerability analysis, OSINT workflows, and AI-assisted development through hands-on experimentation and documentation.

The homelab serves as an environment for testing tools, performing network analysis, developing Python utilities, exploring Docker containers, mapping infrastructure, and studying modern cybersecurity concepts in a controlled and ethical setting.

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
- Maltego

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
├── screenshots/
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
- Infrastructure mapping and visualization
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

## Current Lab Projects

### OWASP Juice Shop
Dockerized vulnerable web application used for:
- Web application testing
- Enumeration practice
- Nmap scanning
- Docker container inspection
- Security tooling experimentation

### Local AI Environment
Locally hosted Llama3 environment using:
- Ollama
- Open WebUI
- Continue VS Code extension

### OSINT & Infrastructure Mapping
Using Maltego and Recon-ng to:
- Map domains and DNS relationships
- Visualize infrastructure
- Practice reconnaissance workflows
- Perform ethical OSINT research

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

### Hydra Example
```bash
hydra -l admin -P passwords.txt ssh://127.0.0.1
```

### Recon-ng
```bash
recon-ng
```

---

## Notes

This homelab is intended strictly for ethical learning, defensive security research, authorized testing environments, and personal skill development.