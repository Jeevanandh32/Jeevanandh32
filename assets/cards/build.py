"""Project cards for the profile README: one SVG per project, same look as the header.

Regenerate:  python3 assets/cards/build.py
Every number on a card is taken from that project's own README / results.
"""

import pathlib
from html import escape

OUT = pathlib.Path(__file__).parent
W, H = 600, 300

PROJECTS = [
    # file, kind, accent, featured, title, pitch (2 lines), metric, metric caption, chips
    ("cloudbridge", "CLOUD NETWORKING", "#38bdf8", True, "CloudBridge",
     ["Multi-cloud hub-and-spoke on AWS + Azure:", "4-tunnel IPsec/eBGP VPN, DNS on two providers"],
     "36.4 s", "failover with Route 53 unreachable", ["Terraform", "Transit Gateway", "BGP / ECMP", "EKS · AKS"]),
    ("fabricpilot", "NETWORK AUTOMATION", "#4ade80", True, "FabricPilot",
     ["Cisco NX-OS + Juniper Junos EVPN-VXLAN", "from NetBox/YAML, staged canary-first"],
     "54 tests", "canary → health gate → auto-rollback", ["Python", "Ansible", "NetBox", "containerlab"]),
    ("tradehunt", "MARKET-DATA NETWORKING", "#a78bfa", True, "TradeHunt",
     ["Redundant A/B multicast feeds on Arista,", "replaying real Nasdaq ITCH data"],
     "18 / 18", "blind diagnoses correct · 6 incidents", ["Arista EOS", "PIM-SSM", "IGMPv3", "Prometheus"]),
    ("sophos", "NETWORK SECURITY", "#f97316", False, "Sophos S2S VPN Lab",
     ["Two Sophos Firewalls in AWS VPCs joined", "by IKEv2 IPsec through AWS NAT"],
     "14 / 14", "validation tests passed from both sites", ["Sophos SFOS", "IPsec / IKEv2", "NAT", "Terraform"]),
    ("probepulse", "OBSERVABILITY", "#facc15", False, "ProbePulse",
     ["Container network observability with", "operator-approved recovery"],
     "36.95 s", "median alert detection · 351 ms recovery", ["Prometheus", "Grafana", "Docker", "tcpdump"]),
    ("multisite", "ENTERPRISE DESIGN", "#22d3ee", False, "HA Multi-Site Network",
     ["Five-site enterprise network with gateway", "redundancy and segmented VLANs"],
     "5 sites", "8 routers · 11 switches", ["OSPF", "EIGRP", "GRE", "HSRP"]),
    ("mpls", "SERVICE PROVIDER", "#fb7185", False, "Multi-AS BGP + MPLS L3VPN",
     ["Provider core carrying customer VRFs,", "broken and fixed to practise troubleshooting"],
     "3 ASes", "AS 100 core · AS 65001 / 65002 customers", ["BGP", "MPLS / LDP", "VRF", "route-maps"]),
    ("linux", "LINUX INFRASTRUCTURE", "#94a3b8", False, "Linux Network Infra",
     ["Ubuntu lab services: DNS, site-to-site", "VPN and automated backups"],
     "3 services", "BIND9 DNS · strongSwan IPsec · backups", ["Ubuntu", "BIND9", "strongSwan", "Bash"]),
    ("awss3", "CLOUD AUTOMATION", "#fbbf24", False, "AWS S3 Diagnostics",
     ["Python/boto3 checks for credentials, objects,", "multipart upload and versioning"],
     "JSON", "end-to-end report, cleanup failures flagged", ["Python", "boto3", "AWS S3", "IAM"]),
    ("earlier", "EARLIER PROJECTS", "#64748b", False, "Python Networking",
     ["RSA key exchange with encrypted chat, and a", "multi-threaded TCP client–server"],
     "+2 repos", "all repositories on my GitHub", ["Python", "sockets", "RSA", "PyCryptodome"]),
]


def card(kind, accent, featured, title, pitch, metric, caption, chips):
    p = []
    a = p.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
      f'font-family="Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif">')
    a(f'<title>{escape(title)}: {escape(" ".join(pitch))} {escape(metric)} {escape(caption)}</title>')
    a('<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#07111f"/>'
      '<stop offset="1" stop-color="#0d1b33"/></linearGradient>'
      '<pattern id="g" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M 28 0 L 0 0 0 28" '
      'fill="none" stroke="#ffffff" stroke-opacity="0.035"/></pattern></defs>')
    a(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="url(#bg)" stroke="{accent}" '
      f'stroke-opacity="{0.9 if featured else 0.35}" stroke-width="{2.5 if featured else 1.5}"/>')
    a(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="url(#g)"/>')
    a(f'<rect x="1" y="34" width="6" height="64" rx="3" fill="{accent}"/>')
    a(f'<text x="30" y="46" font-size="13" font-weight="700" letter-spacing="2.5" fill="{accent}">{escape(kind)}</text>')
    if featured:
        a(f'<rect x="{W - 130}" y="26" width="104" height="28" rx="14" fill="{accent}" fill-opacity="0.15" stroke="{accent}"/>')
        a(f'<text x="{W - 78}" y="45" font-size="13" font-weight="800" fill="{accent}" text-anchor="middle" letter-spacing="1">★ FEATURED</text>')
    a(f'<text x="28" y="88" font-size="31" font-weight="800" fill="#ffffff">{escape(title)}</text>')
    for i, line in enumerate(pitch):
        a(f'<text x="30" y="{118 + i * 22}" font-size="16" fill="#b8c6db">{escape(line)}</text>')
    a(f'<text x="28" y="{206}" font-size="40" font-weight="800" fill="{accent}">{escape(metric)}</text>')
    a(f'<text x="30" y="{230}" font-size="14" fill="#94a3b8">{escape(caption)}</text>')
    x = 30
    for c in chips:
        w = 18 + len(c) * 8
        a(f'<rect x="{x}" y="250" width="{w}" height="28" rx="7" fill="#ffffff" fill-opacity="0.06" stroke="#ffffff" stroke-opacity="0.12"/>')
        a(f'<text x="{x + w / 2}" y="269" font-size="13" fill="#dbe4f0" text-anchor="middle" '
          f'font-family="SFMono-Regular, Menlo, Consolas, monospace">{escape(c)}</text>')
        x += w + 10
    a(f'<text x="{W - 26}" y="{H - 22}" font-size="20" fill="{accent}" text-anchor="end">→</text>')
    a('</svg>')
    return "".join(p)


for f, *rest in PROJECTS:
    (OUT / f"{f}.svg").write_text(card(*rest))
print(f"wrote {len(PROJECTS)} cards to {OUT}")
