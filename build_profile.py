#!/usr/bin/env python3
"""Generates every visual of the profile README in Unified Tactical Amber Theme 
with subtle background grids, crisp high-contrast descriptions, and strict orange consistency.
Run: python3 build_profile.py"""
import math, random, os, sys
from xml.sax.saxutils import escape as E

STATIC = "--static" in sys.argv
OUT = "/tmp/prev" if STATIC else os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT + "/assets", exist_ok=True)

USER = "abdul-wahid022"
RAW = f"https://raw.githubusercontent.com/{USER}/{USER}/main"
VER = "10"
FONT = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
CWF = 0.6

A = lambda s: "" if STATIC else s
mw = lambda text, fs: len(text) * fs * CWF

LABS = [
 ("SOC", "SOC · SIEM · DFIR", "soc-blue-team-dfir-lab-portfolio", "Wazuh rule, Suricata/Zeek/RITA", "BITSLOTH forensics, KFSensor", ["Wazuh", "Suricata", "Zeek"], "8 modules"),
 ("ZT", "Zero Trust UTM Lab", "zero-trust-utm-security-lab", "5 machines: FortiGate, AD + PKI", "Shuffle SOAR, honeypots", ["FortiGate", "Wazuh", "SOAR"], "5 machines"),
 ("CND", "Network Defender", "certified-network-defender-lab-portfolio", "pfSense, AD, Wazuh, Splunk, cloud", "forensics and threat hunting", ["pfSense", "Splunk", "Wazuh"], "20 modules"),
 ("EXP", "Network Sec & Exploitation", "network-security-and-exploitation-lab-portfolio", "Metasploit, pivoting, privilege escalation,", "Active Directory and custom payloads", ["Metasploit", "AD", "Pivoting"], "12 labs"),
 ("RE", "Malware Analysis & RE", "malware-analysis-reverse-engineering-lab-portfolio", "Mirai, Kryptik, Ardamax, HeartBeat", "static, dynamic & AI Ghidra", ["Ghidra", "ANY.RUN", "capa"], "11 labs"),
 ("CTI", "Cyber Threat Intelligence", "cyber-threat-intelligence-lab-portfolio", "OTX, YARA, OpenIOC, ATT&CK mapping, ACH", "and an OpenCTI platform evaluation", ["YARA", "OpenCTI", "ATT&CK"], "8 labs"),
 ("OSI", "OSINT & Social Engineering", "osint-social-engineering-lab-portfolio", "Recon, Maltego, Pagodo dork filtering,", "Gophish and SET phishing simulations", ["Maltego", "Gophish", "SET"], "10 labs"),
 ("CEH", "Ethical Hacking (CEH)", "certified-ethical-hacker-lab-portfolio", "Recon, scanning, enumeration and", "OpenVAS + Acunetix assessments", ["Nmap", "OpenVAS", "Acunetix"], "4 modules"),
 ("DFIR", "Digital Forensics (CHFI)", "computer-hacking-forensic-investigator-lab-portfolio", "Imaging, recovery and anti-forensics with", "chain-of-custody records", ["Autopsy", "FTK Imager", "dd"], "4 modules"),
 ("NET", "Networking (CCNA+)", "ccna-enterprise-networking-lab-portfolio", "22 Packet Tracer modules and 6 enterprise", "designs: OSPF, BGP, IPSec, HSRP", ["Cisco IOS", "OSPF", "IPSec"], "22 modules"),
 ("DEV", "DevSecOps Assessment", "securetrack-lab-security-assessment", "SAST, SCA and DAST on a Flask app;", "pip-audit findings cut from 25 to 9", ["Semgrep", "ZAP", "pip-audit"], "SAST·SCA·DAST"),
]

PROJ = [
 ("OS", "Silent Vector", "silent-vector-distributed-mini-os", "Distributed mini-OS: task migration", "live dashboard & recovery", ["Python", "TCP", "JSON"], "14 commands"),
 ("NET", "Cloud TAP", "enterprise-network-simulator", "48-device network simulator with BST", "graph, BFS/DFS and Dijkstra", ["C++17", "Graphs", "DHCP"], "48 devices"),
 ("PWD", "Password Analyzer", "cpp-password-strength-analyzer", "Entropy analysis, generator and a", "Cupid Media breach case study", ["C++", "Entropy", "Web"], "C++ + web"),
 ("SKY", "Sky Cast", "cpp-weather-forecast-system", "Weather for Pakistani cities via", "OpenWeatherMap, libcurl, RapidJSON", ["C++", "libcurl", "JSON"], "5-day forecast"),
 ("x86", "x86 Traffic Light", "x86-traffic-light-controller", "Four-mode intersection controller in", "8086 assembly, runs in DOSBox", ["8086", "MASM", "DOSBox"], "4 modes"),
 ("OOP", "Library Management", "cpp-library-management-system", "OOP with inheritance, polymorphism,", "templates, admin and student roles", ["C++", "OOP", "Templates"], "C++11"),
 ("UX", "Owl Watch", "figma-survival-app-prototype", "Emergency app prototype: SOS, offline", "mode and map-based incident reports", ["Figma", "UX", "Offline"], "UI/UX"),
 ("SH", "Shell Scripting Guide", "shell-scripting-complete-guide", "Comprehensive bash scripting notes:", "variables, loops, arrays and automation", ["Bash", "Linux", "Scripts"], "Guide"),
 ("CLI", "Linux CLI Notes", "linux-cli-notes", "Core Linux commands, file permissions,", "system administration and networking", ["Linux", "CLI", "SysAdmin"], "Notes"),
]

# Unified Tactical Amber Palette (Primary Amber/Orange focus, ultra-subtle grid lines)
TAC = dict(w1="#0D1117", w2="#090A09", text="#F8FAFC", muted="#94A3B8", label="#F0883E",
           acc=("#B0681E", "#D29922", "#F0883E"), vis="#F0883E", visb="#FFA657",
           rule="#F0883E", glow=("#B0681E", "#D29922", "#F0883E"), glow_o=".12",
           pill=("#1A1714", "#F0883E"), chip="#FFFFFF", chip_o=".04")

def svg(w, h, defs, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{E(title)}">'
            f'<title>{E(title)}</title><style>text{{font-family:{FONT}}}</style><defs>{defs}</defs>{body}</svg>')

def save(name, s):
    open(f"{OUT}/{name}", "w", encoding="utf-8").write(s)

def T(x, y, s, fs, fill, extra=""):
    return f'<text x="{x:.1f}" y="{y}" font-size="{fs}" fill="{fill}" textLength="{mw(s, fs):.1f}" lengthAdjust="spacingAndGlyphs" {extra}>{E(s)}</text>'

def shimmer(gid, w, c, dur="14s"):
    return (f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{w}" y2="0">'
            f'<stop offset="0" stop-color="{c[0]}" stop-opacity="0.5"/><stop offset=".5" stop-color="{c[1]}" stop-opacity="0.75"/><stop offset="1" stop-color="{c[2]}" stop-opacity="0.5"/>'
            + A(f'<animate attributeName="x1" values="{-w};0;{-w}" dur="{dur}" repeatCount="indefinite"/>'
                f'<animate attributeName="x2" values="0;{w};0" dur="{dur}" repeatCount="indefinite"/>')
            + '</linearGradient>')

def base_defs(w):
    return (f'<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{TAC["w1"]}"/><stop offset="1" stop-color="{TAC["w2"]}"/></linearGradient>'
            # Ultra-subtle background grid lines (reduced visibility)
            f'<pattern id="pinstripe" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="url(#bg)"/><line x1="0" y1="0" x2="0" y2="8" stroke="{TAC["text"]}" stroke-opacity="0.015" stroke-width="1"/></pattern>'
            f'{shimmer("bd", w, TAC["acc"], "14s")}'
            f'{shimmer("chipgrad", 90, TAC["acc"], "8s")}'
            f'<linearGradient id="ac" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{TAC["acc"][0]}"/><stop offset=".5" stop-color="{TAC["acc"][1]}"/><stop offset="1" stop-color="{TAC["acc"][2]}"/></linearGradient>'
            f'<radialGradient id="gl"><stop offset="0" stop-color="{TAC["acc"][1]}" stop-opacity=".22"/><stop offset="1" stop-color="{TAC["acc"][1]}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="badgegl"><stop offset="0" stop-color="{TAC["acc"][1]}" stop-opacity=".40"/><stop offset="1" stop-color="{TAC["acc"][0]}" stop-opacity=".10"/></radialGradient>')

def border(w, h, rx=14):
    return f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="none" stroke="url(#bd)" stroke-width="1.1" opacity="0.80"/>'

def card(code, title, repo, l1, l2, chips, badge):
    W, H = 420, 156
    bw = mw(badge, 10) + 20
    left_margin = 22

    if len(repo) * 10 * CWF > 180:
        repo = repo[:28] + "..."

    o = [f'<rect width="{W}" height="{H}" rx="14" fill="url(#pinstripe)"/>']
    o.append(border(W, H))

    # Left glass panel with solid dark overlay for maximum description readability
    o.append(f'<rect x="12" y="12" width="220" height="132" rx="8" fill="#000000" fill-opacity=".28" stroke="#ffffff" stroke-opacity=".05"/>')
    
    badge_w = mw(code, 10) + 16
    o.append(f'<rect x="{left_margin}" y="20" width="{badge_w:.1f}" height="18" rx="9" fill="{TAC["acc"][1]}" fill-opacity=".12" stroke="url(#ac)" stroke-opacity=".60"/>')
    o.append(T(left_margin + 8, 33, code, 10, TAC["label"], 'font-weight="700"'))
    
    o.append(T(left_margin, 58, title, 14, "#FFFFFF", 'font-weight="700"'))
    o.append(T(left_margin, 74, repo, 10, TAC["muted"]))
    o.append(f'<line x1="{left_margin}" x2="220" y1="84" y2="84" stroke="{TAC["acc"][1]}" stroke-opacity=".15"/>')
    o.append(T(left_margin, 100, l1, 11, "#F1F5F9"))  # Ultra-crisp bright text
    o.append(T(left_margin, 116, l2, 11, "#F1F5F9"))

    x = left_margin
    for c in chips[:3]:
        cw = mw(c, 10) + 18
        o.append(f'<rect x="{x}" y="128" width="{cw:.1f}" height="20" rx="10" fill="#ffffff" fill-opacity=".04" stroke="{TAC["acc"][1]}" stroke-width="1" stroke-opacity=".22"/>')
        o.append(T(x + 9, 142, c, 10, "#FFFFFF", 'font-weight="600"'))
        x += cw + 6

    # Center middle pseudo-code column (subtle background details, opacity 0.22)
    o.append(f'<rect x="248" y="12" width="68" height="132" rx="8" fill="#ffffff" fill-opacity=".01" stroke="#ffffff" stroke-opacity=".02"/>')
    o.append(f'<g opacity="0.22" font-size="6" fill="#64748B">')
    for i, line in enumerate(["nmap -sV", "  rule::match", "    probe();", "  ::active", "}", "// 0x7F4A", "status: ok"]):
        o.append(f'<text x="254" y="{34 + i*16}">{E(line)}</text>')
    o.append('</g>')

    # Right precision radar assembly (Strictly Unified Tactical Amber Accent)
    cx, cy = 362, 84
    o.append(f'<g transform="translate({cx},{cy})">')
    o.append(f'<circle r="40" fill="url(#gl)">' + A('<animate attributeName="r" values="38;41;38" dur="6s" repeatCount="indefinite"/>') + '</circle>')
    o.append(f'<circle r="38" fill="none" stroke="url(#ac)" stroke-opacity=".18" stroke-width="1"/>')
    o.append(f'<circle r="31" fill="none" stroke="{TAC["label"]}" stroke-opacity=".45" stroke-width="1.2" stroke-dasharray="3 7">'
              + A('<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="18s" repeatCount="indefinite"/>') + '</circle>')
    o.append(f'<circle r="23" fill="none" stroke="{TAC["acc"][1]}" stroke-opacity=".30" stroke-width="1.4" stroke-dasharray="2 5">'
              + A('<animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="12s" repeatCount="indefinite"/>') + '</circle>')
    o.append(f'<circle r="15" fill="none" stroke="#ffffff" stroke-opacity=".12" stroke-width="1.6" stroke-dasharray="11 6">'
              + A('<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="26s" repeatCount="indefinite"/>') + '</circle>')
    o.append(T(-mw(code, 13)/2, 5, code, 13, "#ffffff", 'font-weight="700"'))
    o.append('</g>')

    bx = W - 12 - bw
    o.append(f'<rect x="{bx:.1f}" y="12" width="{bw:.1f}" height="22" rx="11" fill="url(#badgegl)" fill-opacity=".35" stroke="url(#ac)" stroke-opacity=".60"/>')
    o.append(T(bx + 10, 27, badge, 10, "#ffffff", 'font-weight="700"'))

    return svg(W, H, base_defs(W), "".join(o), f"{title} — {repo}")

def section_header(label):
    W, H = 880, 52
    body = (f'<rect width="{W}" height="{H}" rx="12" fill="url(#pinstripe)"/>{border(W, H, 12)}'
            + T(36, 32, label, 16, "#F8FAFC", 'font-weight="700"'))
    return svg(W, H, base_defs(W), body, label)

def readme():
    pic = lambda n: f'{RAW}/{n}?v={VER}'
    def cards(lst):
        return "\n".join(f'<a href="https://github.com/{USER}/{c[2]}"><img src="{pic("assets/card-"+c[2]+".svg")}" width="49%" alt="{c[1]}"></a>' for c in lst)
    return f'''<!-- Tactical Amber Layout -->
<div align="center">
<br>
<img src="{pic("assets/h-labs.svg")}" width="100%" alt="Lab portfolios">
{cards(LABS)}
<br><br>
<img src="{pic("assets/h-projects.svg")}" width="100%" alt="Software projects">
{cards(PROJ)}
</div>
'''

if __name__ == "__main__":
    for c in LABS + PROJ:
        save(f"assets/card-{c[2]}.svg", card(c[0], c[1], c[2], c[3], c[4], c[5], c[6]))

    save("assets/h-labs.svg", section_header("LAB PORTFOLIOS // TACTICAL INTELLIGENCE"))
    save("assets/h-projects.svg", section_header("SOFTWARE PROJECTS"))

    if not STATIC:
        open(f"{OUT}/README.md", "w", encoding="utf-8").write(readme())
    print("Perfected unified tactical cards generated successfully:", OUT)