"""Section graphics for the profile README: AI workflow, skill stack, experience timeline,
contact buttons. Same look as the banner and project cards. Static (no hide/reveal
animation), so they always render completely.

Regenerate:  python3 assets/sections/build.py
"""

import pathlib
from html import escape

OUT = pathlib.Path(__file__).parent
FONT = "Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif"
MONO = "SFMono-Regular, Menlo, Consolas, monospace"
BG = ('<style>.ring{animation:ring 2.4s ease-out infinite;transform-box:fill-box;transform-origin:center}.flow{animation:flow 1.2s linear infinite}'
      '@keyframes ring{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.9);opacity:0}}'
      '@keyframes flow{to{stroke-dashoffset:-20}}'
      '@media (prefers-reduced-motion:reduce){.ring,.flow{animation:none;opacity:0}}</style><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#07111f"/>'
      '<stop offset="1" stop-color="#0d1b33"/></linearGradient><pattern id="g" width="32" height="32" '
      'patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="#ffffff" '
      'stroke-opacity="0.035"/></pattern>'
      '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#64748b"/></marker></defs>')


def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'font-family="{FONT}"><title>{escape(title)}</title>{BG}'
            f'<rect width="{w}" height="{h}" rx="16" fill="url(#bg)"/><rect width="{w}" height="{h}" rx="16" '
            f'fill="url(#g)"/>{body}</svg>')


def t(x, y, s, size=14, fill="#cbd5e1", weight=400, anchor="start", font=None):
    f = f' font-family="{font}"' if font else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}"{f}>{escape(s)}</text>')


def chip(x, y, s, color="#ffffff", size=13):
    w = 16 + len(s) * (size * 0.62)
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="26" rx="7" fill="{color}" fill-opacity="0.10" '
            f'stroke="{color}" stroke-opacity="0.35"/>' + t(x + w / 2, y + 17.5, s, size, "#e2e8f0", 500, "middle", MONO)), w


# ---------- AI workflow ----------
def ai():
    b = [t(40, 52, "HOW I USE AI", 14, "#7dd3fc", 700), t(40, 86, "The agent drafts. The lab decides. I approve.", 27, "#ffffff", 800)]
    steps = [("1", "Agent drafts", "code, configs, tests", "#a78bfa"),
             ("2", "Lab runs it", "Cisco · Juniper · Arista · cloud", "#38bdf8"),
             ("3", "Tests + metrics", "unit tests · benchmarks · live", "#4ade80"),
             ("4", "I review", "read diffs, check numbers", "#facc15"),
             ("5", "Ship or roll back", "canary · health gate · rollback", "#fb923c")]
    x0, w, gap, y = 40, 226, 22, 116
    for i, (n, head, sub, c) in enumerate(steps):
        x = x0 + i * (w + gap)
        b.append(f'<rect x="{x}" y="{y}" width="{w}" height="86" rx="12" fill="{c}" fill-opacity="0.08" stroke="{c}" stroke-width="1.6"/>')
        b.append(f'<circle cx="{x + 24}" cy="{y + 26}" r="13" fill="{c}"/>' + t(x + 24, y + 31, n, 14, "#0b1220", 800, "middle"))
        b.append(t(x + 46, y + 32, head, 17, "#ffffff", 700))
        b.append(t(x + 16, y + 64, sub, 12.5, "#a9b8cf"))
        if i < len(steps) - 1:
            b.append(f'<line x1="{x + w + 3}" y1="{y + 43}" x2="{x + w + gap - 3}" y2="{y + 43}" stroke="#64748b" stroke-width="2" marker-end="url(#ar)"/>')
    b.append(f'<path class="flow" d="M {x0 + 4 * (w + gap) + w / 2} {y + 92} V {y + 112} H {x0 + w / 2} V {y + 92}" fill="none" stroke="#475569" stroke-width="1.6" stroke-dasharray="5 5" marker-end="url(#ar)"/>')
    xa, xb = x0 + w / 2, x0 + 4 * (w + gap) + w / 2
    b.append(f'<path id="tok" d="M {x0 + 10} {y + 43} H {x0 + 5 * w + 4 * gap - 10} L {xb} {y + 92} V {y + 112} H {xa} V {y + 92} Z" fill="none"/>')
    b.append('<circle r="6" fill="#ffffff" opacity="0.9"><animateMotion dur="8s" repeatCount="indefinite"><mpath href="#tok"/></animateMotion></circle>')
    b.append(t(640, y + 128, "failed check → back to the agent with the evidence", 12.5, "#64748b", 400, "middle"))
    b.append(t(40, 292, "Evidence from my projects", 13, "#7dd3fc", 700))
    ev = [("MindBridge AI blocked 2 bad Terraform changes before apply", "#38bdf8"),
          ("FabricPilot: 54 tests + canary auto-rollback", "#4ade80"),
          ("ProbePulse: operator-approved recovery", "#facc15")]
    x = 40
    for s, c in ev:
        g, w2 = chip(x, 304, s, c, 12.5)
        b.append(g); x += w2 + 14
    return svg(1280, 350, "How I use AI: the agent drafts, the lab decides, I approve", "".join(b))


# ---------- skill stack ----------
def skills():
    layers = [("CLOUD", "#38bdf8", ["Transit Gateway", "S2S VPN", "PrivateLink", "Route 53", "EKS", "Azure VPN GW", "Azure DNS", "Traffic Mgr", "AKS", "GCP"]),
              ("AUTOMATION", "#4ade80", ["Python", "Ansible", "Terraform", "NetBox", "Netmiko", "Jinja2", "Bash", "REST APIs", "Git"]),
              ("ROUTING & SWITCHING", "#a78bfa", ["OSPF", "BGP", "ECMP", "EVPN-VXLAN", "MPLS L3VPN", "VLANs / 802.1Q", "STP/RSTP", "PIM-SSM", "IGMPv3"]),
              ("SECURITY & VPN", "#fb923c", ["IPsec / IKEv2", "NAT / PAT", "nftables", "Sophos SFOS", "ACLs", "NetworkPolicy"]),
              ("PLATFORMS", "#f472b6", ["Cisco IOS / IOS XE", "Cisco NX-OS", "Meraki", "Junos OS", "Arista EOS", "Ubuntu", "Docker", "containerlab"]),
              ("OBSERVABILITY", "#facc15", ["Prometheus", "Grafana", "SolarWinds", "SNMP", "Wireshark", "tcpdump", "ServiceNow"])]
    b = [t(40, 52, "SKILL STACK", 14, "#7dd3fc", 700), t(40, 86, "From the wire to the cloud", 27, "#ffffff", 800)]
    y = 112
    for name, c, items in layers:
        b.append(f'<rect x="40" y="{y}" width="1200" height="50" rx="10" fill="{c}" fill-opacity="0.07" stroke="{c}" stroke-opacity="0.45"/>')
        b.append(f'<rect x="40" y="{y}" width="8" height="50" rx="4" fill="{c}"/>')
        b.append(t(64, y + 31, name, 13, c, 800))
        x = 250
        for s in items:
            g, w = chip(x, y + 12, s, c, 12.5)
            if x + w > 1228:
                break
            b.append(g); x += w + 10
        y += 60
    b.append(f'<circle cx="44" r="5" fill="#ffffff" opacity="0.9"><animate attributeName="cy" values="{y - 33};137;{y - 33}" dur="6s" repeatCount="indefinite"/></circle>')
    b.append(t(1240, 52, "packet: wire → cloud", 12, "#64748b", 400, "end"))
    return svg(1280, y + 16, "Skill stack: cloud, automation, routing and switching, security, platforms, observability", "".join(b))


# ---------- experience timeline ----------
def experience():
    b = [t(40, 52, "EXPERIENCE", 14, "#7dd3fc", 700), t(40, 86, "Where I've worked", 27, "#ffffff", 800)]
    y = 152
    b.append(f'<line x1="70" y1="{y}" x2="1210" y2="{y}" stroke="#334155" stroke-width="3"/>')
    stops = [(150, "Jan – May 2024", "R&D Intern", "boAt · Bangalore", ["C firmware, TWS charging case", "TI MSP MCU · OLED over I2C"], "#94a3b8"),
             (470, "Jan – Jun 2026", "Network Engineer (Co-op)", "Global Partners · Newton, MA", ["300+ incidents · 890+ retail sites", "88% same-day · 60+ carrier escalations"], "#38bdf8"),
             (800, "Sep 2026 – present", "Graduate Teaching Assistant", "Northeastern · Linux for Network Engineers", ["Labs for 25+ graduate students", "lab guides · VM troubleshooting"], "#4ade80"),
             (1110, "Dec 2026", "MS Telecom Networks", "Northeastern University", ["JNCIA-Junos · Terraform Associate", "open to relocation"], "#a78bfa")]
    b.append(f'<circle cy="{y}" r="5" fill="#ffffff" opacity="0.85"><animate attributeName="cx" values="70;1210" dur="6s" repeatCount="indefinite"/></circle>')
    b.append(f'<circle class="ring" cx="800" cy="{y}" r="11" fill="none" stroke="#4ade80" stroke-width="3"/>')
    for x, when, role, org, lines, c in stops:
        b.append(f'<circle cx="{x}" cy="{y}" r="11" fill="#0b1220" stroke="{c}" stroke-width="4"/>')
        b.append(t(x, y - 24, when, 13, c, 700, "middle"))
        b.append(t(x, y + 40, role, 16.5, "#ffffff", 700, "middle"))
        b.append(t(x, y + 62, org, 12.5, "#a9b8cf", 400, "middle"))
        for i, s in enumerate(lines):
            b.append(t(x, y + 88 + i * 19, s, 12.5, "#cbd5e1", 400, "middle"))
    return svg(1280, 290, "Experience: boAt R&D intern 2024; Global Partners network engineer co-op 2026; Northeastern TA; MS Dec 2026", "".join(b))


# ---------- contact buttons ----------
STYLE_ONLY = BG.split('<defs>')[0]


def button(label, value, color, glyph):
    lines = value if isinstance(value, list) else [value]
    b = [f'<rect x="1" y="1" width="398" height="86" rx="14" fill="{color}" fill-opacity="0.10" stroke="{color}" stroke-width="2"/>',
         f'<circle cx="46" cy="44" r="24" fill="{color}" fill-opacity="0.20"/>',
         f'<circle class="ring" cx="46" cy="44" r="24" fill="none" stroke="{color}" stroke-width="2"/>', t(46, 52, glyph, 22, color, 800, "middle"),
         t(84, 30 if len(lines) > 1 else 38, label, 13, color, 700)]
    if len(lines) > 1:
        b += [t(84, 52, lines[0], 15.5, "#ffffff", 700), t(84, 73, lines[1], 15.5, "#ffffff", 700)]
    else:
        b.append(t(84, 62, lines[0], 17, "#ffffff", 700))
    value = " · ".join(lines)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="88" viewBox="0 0 400 88" font-family="{FONT}">'
            f'<title>{escape(label)}: {escape(value)}</title>' + STYLE_ONLY + '<rect width="400" height="88" rx="15" fill="#0b1220"/>'
            + "".join(b) + "</svg>")


(OUT / "ai-workflow.svg").write_text(ai())
(OUT / "skill-stack.svg").write_text(skills())
(OUT / "experience.svg").write_text(experience())
(OUT / "contact-portfolio.svg").write_text(button("PORTFOLIO", "jeevanandh32.github.io", "#38bdf8", "◎"))
(OUT / "contact-linkedin.svg").write_text(button("LINKEDIN", "in/jeevanandhravi", "#60a5fa", "in"))
(OUT / "contact-email.svg").write_text(button("EMAIL", "jeevanandhravi@gmail.com", "#4ade80", "@"))
print("wrote section graphics")
