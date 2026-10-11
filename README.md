# 👋 Hi, I'm Jeevanandh Ravi

**Network Engineer · Network Automation · Cisco & Juniper**
MS in Telecommunication Networks, Northeastern University (Dec 2026) · JNCIA-Junos · Boston, MA (open to relocation)

I troubleshoot and build enterprise networks, and I automate the changes so they go out safely: validated, staged, health-checked, and rolled back on their own when something breaks.

- 🛠️ Network Engineer co-op at **Global Partners**: resolved 300+ WAN, LAN, Wi-Fi and POS incidents across 890+ retail sites, with 88% resolved the same day
- 🎓 Graduate Teaching Assistant, **Linux for Network Engineers**, Northeastern University
- 🤖 Currently building: multivendor EVPN-VXLAN automation on real Cisco NX-OS and Juniper Junos images

## 🚀 Featured project

### [FabricPilot: Multivendor EVPN-VXLAN Fabric Automation](https://github.com/Jeevanandh32/fabricpilot)

[![FabricPilot demo](https://github.com/Jeevanandh32/fabricpilot/raw/main/docs/demo-poster.png)](https://github.com/Jeevanandh32/fabricpilot/blob/main/docs/fabricpilot-short.mp4)

One source of truth (NetBox/YAML) drives Cisco NX-OS and Juniper Junos configs. Every change goes through a pipeline: **validate → render → plan → canary/batch rollout → health gate → verify → email report**.

- Canary-to-batch deployments with BGP/VXLAN health checks and automatic rollback (Junos `commit confirmed`, NX-OS checkpoints)
- Run on real Nexus 9000v and vJunos-switch images in a containerlab fabric on Google Cloud
- Fixed 20+ issues found on real switch images, including a Cisco/Juniper EVPN interoperability bug, to get Layer 2 and Layer 3 traffic working between the two vendors
- Ansible check mode reported zero configuration drift; the NetBox round trip renders identical configs
- `Python` `Jinja2` `Netmiko` `Ansible` `NetBox` `containerlab` `Google Cloud` `BGP EVPN` `VXLAN`

▶️ [Watch the 2-minute demo](https://github.com/Jeevanandh32/fabricpilot/blob/main/docs/fabricpilot-short.mp4)

## 📂 More projects

**[ProbePulse: Container Network Observability & Recovery](https://github.com/Jeevanandh32/ProbePulse)**
Docker Compose lab testing HTTP, connection and DNS failures, with tcpdump packet analysis. Prometheus Blackbox probes and Grafana email alerts gave a 36.95 s median detection time across five controlled outages. Operator-approved Bash remediation recovered 5/5 outages, with a 351 ms median recovery after approval.
`Docker Compose` `Prometheus` `Grafana` `tcpdump` `Bash` `Python`

**[AWS S3 Storage Diagnostic Automation](https://github.com/Jeevanandh32/AWS-S3-Connectivity-Tester)**
Python/boto3 tool that validates AWS credentials, network connectivity and S3 across nine operations, including multipart uploads, IAM permissions and metadata. It tells access, resource and server failures apart (HTTP 403/404/500) and writes JSON reports, cutting diagnostic time from 15 minutes to under 10 seconds.
`Python` `boto3` `AWS S3` `IAM` `JSON`

**[Linux Network Infrastructure & Monitoring](https://github.com/Jeevanandh32/Adhoc-Network-Infrastructure-using-Linux)**
Primary and secondary BIND9 DNS servers and ISC DHCP on Ubuntu VMs in VMware. VMs connected across physical hosts with NAT port forwarding and IPsec, verified with Wireshark, ping and traceroute. Backups automated with cron, and Fail2Ban configured for access protection.
`Ubuntu` `BIND9` `ISC DHCP` `IPsec` `Wireshark` `cron` `Fail2Ban`

<details>
<summary>Earlier projects</summary>

- [Multi-Site Network Design with OSPF and VLANs](https://github.com/Jeevanandh32/Multi-Location-Network-Design-and-Implementation-using-Cisco-Packet-Tracer): OSPF, VLANs, HSRP, IPsec VPN, Rapid STP, EtherChannel (Cisco Packet Tracer)
- [Secure Communication Using RSA Encryption](https://github.com/Jeevanandh32/Secure-Communication-Using-RSA-Encryption): Python RSA key exchange and encrypted client-server chat
- [Network Automation for a Multi-Vendor Environment](https://github.com/Jeevanandh32/Network-Automation-for-Multi-Vendor-Environment)
- [Advanced Network Configuration & Troubleshooting](https://github.com/Jeevanandh32/Advanced-Network-Configuration-Troubleshooting)
- [Socket Programming in Python](https://github.com/Jeevanandh32/SOCKET-PROGRAMMING-IN-PYTHON)

</details>

## 🛠️ Skills

| Area | Tools and technologies |
|---|---|
| **Networking** | TCP/IP, IPv4/IPv6 subnetting, VLANs, 802.1Q, STP/RSTP, OSPF, BGP, DHCP, DNS, NAT/PAT, MPLS, EVPN-VXLAN |
| **Network platforms** | Cisco IOS/IOS XE, Cisco NX-OS, Cisco Meraki Dashboard, Junos OS |
| **Automation** | Python, Bash, Ansible, Netmiko, NetBox, Jinja2, YAML, REST APIs, JSON, Git, Bitbucket |
| **Systems** | Ubuntu Linux, VMware, Docker, Docker Compose, containerlab |
| **Monitoring & troubleshooting** | SolarWinds Orion, SNMP, Prometheus, Grafana, ServiceNow, Wireshark, tcpdump |
| **Cloud** | AWS (S3, IAM, VPC, boto3, CloudShell), Google Cloud (Compute Engine, Cloud Storage) |

## 💼 Experience

**Graduate Teaching Assistant, Linux for Network Engineers**, Northeastern University · *Sep 2026 – Present*
Co-run hands-on Linux labs for 20+ graduate students (Ubuntu, Bash scripting); write lab guides and troubleshoot student VM setups.

**Network Engineer (Co-op)**, Global Partners, Waltham, MA · *Jan 2026 – Jun 2026*
- Tier 1/2 investigations: 300+ WAN, LAN, Wi-Fi and POS incidents across 890+ retail sites, 88% resolved the same day
- Configured Cisco routers and switches and provisioned Meraki APs and cellular gateways (VLANs, access/trunk ports, IP addressing, DHCP)
- Isolated VLAN mismatches, port-security violations, DHCP errors and DMVPN faults; upgraded Cisco IOS/IOS XE
- Coordinated 60+ carrier escalations; configured RPDU/UPS remote management and fusion-spliced fiber in a company-owned data center

**R&D Intern**, boAt (Imagine Marketing), Bangalore, India · *Jan 2024 – May 2024*
Prototyped C firmware for a TWS charging case (TI MSPM0L1306 MCU, SSD1306 OLED over I2C), managed in Git.

## 📜 Certifications

- **Juniper Networks Certified Associate, Junos (JNCIA-Junos)**, Oct 2026
- Master Network Automation with Python for Network Engineers (Udemy)

## 📫 Contact

- **Email:** jeevanandhravi@gmail.com
- **LinkedIn:** [linkedin.com/in/jeevanandhravi](https://www.linkedin.com/in/jeevanandhravi/)
