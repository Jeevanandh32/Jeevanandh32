# 👋 Hi, I'm Jeevanandh Ravi

**Network Engineer · Network Automation · Cloud Networking · Cisco & Juniper**
MS in Telecommunication Networks, Northeastern University (Dec 2026) · JNCIA-Junos · Terraform Associate · Boston, MA (open to relocation)
🌐 **Portfolio:** [jeevanandh32.github.io](https://jeevanandh32.github.io)

I work on enterprise network troubleshooting and deployment. My lab projects explore validated configuration changes, staged rollouts, health checks, rollback, and cloud-network recovery under injected failures.

- 🛠️ Network Engineer co-op at **Global Partners**: resolved 300+ WAN, LAN, Wi-Fi and POS incidents across 890+ retail sites, with 88% resolved the same day
- 🎓 Graduate Teaching Assistant, **Linux for Network Engineers**, Northeastern University
- 🤖 Projects: multi-cloud AWS–Azure hub-and-spoke networking in Terraform, multivendor EVPN-VXLAN automation with virtual Cisco NX-OS and Juniper Junos images, and market-data multicast troubleshooting on Arista
- 🧠 AI-assisted engineering: I use coding agents to support design and debugging, then check changes with automated tests, virtual-switch lab output, and recorded benchmarks

## 📜 Certifications

<p>
  <a href="https://www.credly.com/badges/e5376b58-1848-4cb8-8b9a-ee32a6ad1a65/public_url"><img src="assets/jncia-junos-badge.png" alt="HPE JNCIA-Junos Certified Associate" width="110"></a>
  &nbsp;&nbsp;
  <a href="https://www.credly.com/badges/108ebacc-e498-498b-83f1-58f7ebb84bac/public_url"><img src="assets/terraform-associate-badge.png" alt="HashiCorp Certified: Terraform Associate (004)" width="110"></a>
  &nbsp;&nbsp;
  <a href="https://www.credly.com/badges/75b9c09d-8ff1-4e77-b0ec-b56a134a1db6/public_url"><img src="assets/amd-rocm-badge.png" alt="AMD ROCm Certified Associate" width="110"></a>
  &nbsp;&nbsp;
  <a href="https://www.credly.com/badges/03a6de74-6eb8-4782-a961-c115e34026ed/public_url"><img src="assets/aws-application-networking-badge.png" alt="AWS Application Networking Demonstrated microcredential" width="110"></a>
</p>

- **Juniper Networks Certified Associate, Junos (JNCIA-Junos)**, Oct 2026 – Oct 2029 · [Verify](https://www.credly.com/badges/e5376b58-1848-4cb8-8b9a-ee32a6ad1a65/public_url)
- **HashiCorp Certified: Terraform Associate (004)**, Nov 2026 – Nov 2028 · [Verify](https://www.credly.com/badges/108ebacc-e498-498b-83f1-58f7ebb84bac/public_url)
- **AMD ROCm Certified Associate**, Oct 2026 – Oct 2028 · [Verify](https://www.credly.com/badges/75b9c09d-8ff1-4e77-b0ec-b56a134a1db6/public_url)
- **AWS Application Networking Demonstrated** (microcredential, AWS Training and Certification), Nov 2026 – Nov 2027 · [Verify](https://www.credly.com/badges/03a6de74-6eb8-4782-a961-c115e34026ed/public_url)
- Master Network Automation with Python for Network Engineers (Udemy)

## 🚀 Featured projects

### [CloudBridge: Multi-Cloud Hub-and-Spoke Network on AWS + Azure](https://github.com/Jeevanandh32/CloudBridge)

[![CloudBridge](https://github.com/Jeevanandh32/CloudBridge/raw/main/docs/cover.png)](https://jeevanandh32.github.io/cloudbridge-demo.html)

An active-passive network across AWS and Azure, built in Terraform:
- **AWS:** a Transit Gateway hub with inspection firewalls.
- **Azure:** a hub VNet with a firewall VM and a peered AKS spoke.
- **Between them:** a 4-tunnel active-active IPsec/eBGP VPN with ECMP.
- **DNS:** served by both Route 53 and Azure DNS/Traffic Manager.

Six controlled failure tests, each measured ([results](https://github.com/Jeevanandh32/CloudBridge#results)):

- **DNS:** with every Route 53 name server unreachable, Azure DNS answered 304 of 304 lookups and users failed over in 36.4 s.
- **Region loss:** with the app and all four tunnels cut, users reached Azure in 41.7 s (102 s in the earlier single-provider build).
- **BGP:** a configuration break on one tunnel dropped no packets across 16 test flows. A VPN gateway instance reset paused 38% of flows for 22–31 s, with no full outage.
- **Failures that look healthy, found and fixed:**
  - a missing Transit Gateway route that blackholed traffic;
  - /28 fragmentation that stalled an EKS rollout (custom networking then took pods from 18 to 204);
  - an AKS inbound path dropped by the node security group.
- **MindBridge AI:** a read-only Python tool I built that checks Terraform plans before apply and warned 9–14 minutes before an injected packet-loss ramp crossed 5 %, with no false alarms.
- `Terraform` `AWS Transit Gateway` `Site-to-Site VPN` `Azure VPN Gateway` `IPsec/IKEv2` `BGP/ECMP` `EKS` `AKS/Cilium` `Route 53` `Azure DNS` `Traffic Manager` `nftables` `Python`

▶️ [Watch the 2-minute demo](https://jeevanandh32.github.io/cloudbridge-demo.html)

### [FabricPilot: Multivendor EVPN-VXLAN Fabric Automation](https://github.com/Jeevanandh32/FabricPilot)

[![FabricPilot demo](https://github.com/Jeevanandh32/FabricPilot/raw/main/docs/demo-poster.png)](https://github.com/Jeevanandh32/FabricPilot/blob/main/docs/fabricpilot-short.mp4)

One source of truth (NetBox/YAML) drives Cisco NX-OS and Juniper Junos configs. Every change goes through a pipeline: **validate → render → plan → canary/batch rollout → health gate → verify → email report**.

- Canary-to-batch deployments with BGP/VXLAN health checks and automatic rollback (Junos `commit confirmed`, NX-OS checkpoints)
- Exercised on Nexus 9000v and vJunos-switch images in a containerlab fabric on Google Cloud; 54 local tests cover validation, rendering, rollout logic, and driver parsing
- Resolved documented Cisco/Juniper EVPN interoperability and CLI-handling issues; recorded cross-vendor Layer 2 and Layer 3 connectivity checks
- Ansible check mode reported no proposed changes on three Cisco switches; the README records matching configs after a NetBox inventory round trip
- [Validation scope](https://github.com/Jeevanandh32/FabricPilot#validation-scope): separate evidence for a six-device control-plane check, a 9/16 host ping matrix, and a later halted canary run
- `Python` `Jinja2` `Netmiko` `Ansible` `NetBox` `containerlab` `Google Cloud` `BGP EVPN` `VXLAN`

▶️ [Watch the 2-minute demo](https://github.com/Jeevanandh32/FabricPilot/blob/main/docs/fabricpilot-short.mp4)

### [TradeHunt: Market-Data Feed Troubleshooting on Redundant Multicast](https://github.com/Jeevanandh32/TradeHunt)

[![TradeHunt](https://github.com/Jeevanandh32/TradeHunt/raw/main/docs/cover.png)](https://jeevanandh32.github.io/tradehunt-demo.html)

Rebuilds how exchanges deliver market data:
- **Feeds:** redundant A/B multicast feeds over four Arista cEOS switches.
- **Data:** real Nasdaq TotalView-ITCH data, replayed at 1/10 speed.
- **Incidents:** each failure is diagnosed the way a market-data support engineer would.

Six injected incidents, a silent-feed alert in 6.1–7.0 s, and a diagnostic tool that was correct in 18 of 18 blind runs ([results](https://github.com/Jeevanandh32/TradeHunt/blob/main/RESULTS.md)).

- `Arista EOS` `PIM-SSM` `IGMPv3` `OSPF` `MoldUDP64` `Python` `Prometheus` `Grafana`

▶️ [Watch the 2-minute demo](https://jeevanandh32.github.io/tradehunt-demo.html)

## 📂 More projects

### [Sophos Firewall Site-to-Site VPN Lab on AWS](https://github.com/Jeevanandh32/sophos-firewall-site-to-site-vpn-lab)

[![Sophos site-to-site VPN demo](assets/sophos-s2s-vpn.png)](https://github.com/Jeevanandh32/sophos-firewall-site-to-site-vpn-lab/blob/main/docs/sophos-s2s-vpn-demo.mp4)

Two Sophos Firewalls (SFOS v22) in separate AWS VPCs, each protecting an Ubuntu host, built with Terraform and joined by an IKEv2 IPsec tunnel. Each layer was configured and checked in turn: **build → firewall rules → NAT → web filter → IPsec → tests → backup/restore**.

- IKEv2 IPsec through AWS 1:1 NAT: NAT-T on UDP 4500, Elastic IP identities, AES-256 with Curve25519
- Ordered deny/allow rules with logging, masquerade NAT and category web filtering; 14 of 14 validation tests passed from both sites, confirmed with tcpdump and the IPsec SA
- Found and fixed real issues on the live firewalls (IPsec blocked from the WAN zone, an API-created tunnel left inactive, backups needing a secure storage master key)
- Took an encrypted config backup, made a change, restored it, and confirmed the change was reverted after the reboot
- `Sophos Firewall` `IPsec/IKEv2` `NAT` `Web filtering` `Terraform` `CloudFormation` `AWS VPC/EC2` `tcpdump`

▶️ [Watch the 1-minute walkthrough](https://github.com/Jeevanandh32/sophos-firewall-site-to-site-vpn-lab/blob/main/docs/sophos-s2s-vpn-demo.mp4)

### [ProbePulse: Container Network Observability & Recovery](https://github.com/Jeevanandh32/ProbePulse)

[![ProbePulse](assets/probepulse.png)](https://github.com/Jeevanandh32/ProbePulse)

Docker Compose lab for HTTP, connection, and DNS diagnostics with tcpdump. Five local stopped-container tests recorded 36.95 s median Grafana alert detection and 351 ms median post-approval recovery to HTTP 200; all five recoveries succeeded. Detection excludes email-delivery time, and the recovery script handles a stopped target container.
`Docker Compose` `Prometheus` `Blackbox Exporter` `Grafana` `tcpdump` `Bash` `Python`

### [High-Availability Multi-Site Network Design](https://github.com/Jeevanandh32/Multi-Location-Network-Design-and-Implementation-using-Cisco-Packet-Tracer)

[![High-Availability Multi-Site Network Design](assets/ha-multi-site.png)](https://github.com/Jeevanandh32/Multi-Location-Network-Design-and-Implementation-using-Cisco-Packet-Tracer)

Five-site Cisco Packet Tracer lab with 8 routers and 11 switches. The project documents multi-area OSPF, EIGRP, GRE, VLAN segmentation, gateway redundancy, and connectivity checks. Redundancy configuration is separate from a measured failover-time or zero-loss guarantee.
`Cisco Packet Tracer` `Multi-area OSPF` `EIGRP` `GRE` `HSRP` `Rapid PVST+` `LACP` `ACLs`

### [Multi-AS BGP & MPLS L3VPN Lab](https://github.com/Jeevanandh32/Advanced-Network-Configuration-Troubleshooting)

[![Multi-AS BGP & MPLS L3VPN Lab](assets/mpls-l3vpn.png)](https://github.com/Jeevanandh32/Advanced-Network-Configuration-Troubleshooting)

A provider core (AS 100) carrying customer VRFs between customer sites in AS 65001 and AS 65002. Customer routes are kept apart in VRFs and label-switched across the core, then broken and fixed on purpose to practice troubleshooting.
`Cisco IOS` `BGP` `MPLS` `LDP` `OSPF` `VRF` `route-maps` `L3VPN`

### [Linux Network Infrastructure & Monitoring](https://github.com/Jeevanandh32/Adhoc-Network-Infrastructure-using-Linux)

[![Linux Network Infrastructure & Monitoring](assets/linux-infrastructure.png)](https://github.com/Jeevanandh32/Adhoc-Network-Infrastructure-using-Linux)

Ubuntu lab examples for primary IPv4 BIND9 DNS zones, strongSwan IPsec/IKEv2, and archive/SCP backup automation. The repository includes configuration, diagnostic samples, and the limits of its current reproducibility.
`Ubuntu` `BIND9` `strongSwan` `IPsec/IKEv2` `Bash` `cron` `SCP`

### [AWS S3 Storage Diagnostic Automation](https://github.com/Jeevanandh32/AWS-S3-Connectivity-Tester)

[![AWS S3 Storage Diagnostic Automation](assets/aws-s3-diagnostic.png)](https://github.com/Jeevanandh32/AWS-S3-Connectivity-Tester)

Python/boto3 tool for credential validation and S3 bucket, object, multipart-upload, and versioning checks, with JSON reporting and separate SDK error-handling examples. Cleanup failures are reported; no measured diagnostic-time improvement is claimed.
`Python` `boto3` `AWS S3` `IAM` `JSON`

<details>
<summary>Earlier projects</summary>

- [Secure Communication Using RSA Encryption](https://github.com/Jeevanandh32/Secure-Communication-Using-RSA-Encryption): Python RSA key exchange and encrypted client-server chat
- [Socket Programming in Python](https://github.com/Jeevanandh32/SOCKET-PROGRAMMING-IN-PYTHON)

</details>

## 🧠 AI skills (used in my projects)

| Skill | Where I used it |
|---|---|
| **Building with AI coding agents** | Built FabricPilot (Python, Jinja2, Ansible, 54 tests) and ProbePulse by directing an AI agent through design, code, tests and docs |
| **Verifying AI output** | Checked generated configuration and code against virtual Cisco/Juniper lab output, automated tests, and recorded measurements |
| **AI-assisted troubleshooting** | Used AI to analyze device output and logs while investigating documented CLI and Cisco/Juniper EVPN interoperability issues |
| **Human-in-the-loop automation** | Kept people in control: operator-approved remediation in ProbePulse; changes, commits and deployments approved by me first |
| **Predicting network failures** | MindBridge AI in CloudBridge: checks Terraform plans before apply, runs single-failure what-if sweeps, and warned 9–14 min before an injected loss ramp, with 0 false alarms; models corrected from measured tests |

## 🛠️ Skills

| Area | Tools and technologies |
|---|---|
| **Networking** | TCP/IP, IPv4/IPv6 subnetting, VLANs, 802.1Q, STP/RSTP, OSPF, BGP, ECMP, DHCP, DNS, NAT/PAT, MPLS, EVPN-VXLAN, IPsec/IKEv2 site-to-site VPN, multicast (PIM-SSM, IGMPv3) |
| **Network platforms** | Cisco IOS/IOS XE, Cisco NX-OS, Cisco Meraki Dashboard, Junos OS, Arista EOS, Sophos Firewall (SFOS), Linux nftables firewalls |
| **Automation** | Python, Bash, Ansible, Terraform, Netmiko, NetBox, Jinja2, YAML, REST APIs, JSON, Git, Bitbucket |
| **Systems** | Ubuntu Linux, VMware, Docker, Docker Compose, containerlab |
| **Monitoring & troubleshooting** | SolarWinds Orion, SNMP, Prometheus, Grafana, ServiceNow, Wireshark, tcpdump |
| **AI-assisted engineering** | AI coding agents, AI-assisted debugging and testing, human-in-the-loop automation |
| **Cloud** | AWS (VPC, Transit Gateway, Site-to-Site VPN, PrivateLink, EKS, Route 53, S3, IAM, EC2, CloudFormation, boto3), Azure (VNet peering, VPN Gateway, Private Endpoint, Azure DNS, Traffic Manager, AKS, Monitor), Google Cloud (Compute Engine, Cloud Storage) |

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

## 📫 Contact

- **Portfolio:** [jeevanandh32.github.io](https://jeevanandh32.github.io)
- **Email:** jeevanandhravi@gmail.com
- **LinkedIn:** [linkedin.com/in/jeevanandhravi](https://www.linkedin.com/in/jeevanandhravi/)
