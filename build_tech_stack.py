#!/usr/bin/env python3
"""Generates the robust cybersecurity engineering dashboard banner with 
CSS-transform powered elliptical orbits guaranteed to render correctly in GitHub READMEs.
Run: python3 build_tech_stack.py"""

import os

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f"{OUT}/assets-b", exist_ok=True)

FONT = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"

def generate_tech_stack_svg():
    W, H = 1680, 800

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Enterprise Security &amp; Systems Architecture">
<title>Enterprise Security &amp; Systems Architecture</title>
<style>
    text {{ font-family: {FONT}; }}
    
    .core-pulse {{
        transform-box: fill-box;
        transform-origin: center;
        animation: breathe 4s ease-in-out infinite;
    }}
    
    @keyframes breathe {{
        0%, 100% {{ transform: scale(1); opacity: 0.9; }}
        50% {{ transform: scale(1.04); opacity: 1; }}
    }}
    
    /* Reliable CSS Keyframe Rotations for GitHub Renderers */
    /* Primary Orbits */
    .orbit-track-1 {{
        animation: spinCW 28s linear infinite;
        transform-box: fill-box;
        transform-origin: center;
    }}
    .counter-text-1 {{
        animation: spinCCW 28s linear infinite;
        transform-box: fill-box;
        transform-origin: center;
    }}

    .orbit-track-2 {{
        animation: spinCCW 24s linear infinite;
        transform-box: fill-box;
        transform-origin: center;
    }}
    .counter-text-2 {{
        animation: spinCW 24s linear infinite;
        transform-box: fill-box;
        transform-origin: center;
    }}
    
    /* Secondary Language Orbit (Slightly faster) */
    .orbit-track-3 {{
        animation: spinCW 18s linear infinite;
        transform-box: fill-box;
        transform-origin: center;
    }}
    .counter-text-3 {{
        animation: spinCCW 18s linear infinite;
        transform-box: fill-box;
        transform-origin: center;
    }}

    @keyframes spinCW {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}

    @keyframes spinCCW {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(-360deg); }}
    }}
    
    .capsule {{
        transition: all 0.25s ease;
    }}
    .capsule:hover {{
        fill: #161B22;
        stroke: #F0883E;
    }}
    
    @media (prefers-reduced-motion: reduce) {{
        .orbit-track-1, .orbit-track-2, .counter-text-1, .counter-text-2, 
        .orbit-track-3, .counter-text-3, .core-pulse {{
            animation: none !important;
        }}
    }}
</style>

<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#0D1117"/>
        <stop offset="1" stop-color="#090A09"/>
    </linearGradient>
    <pattern id="pinstripe" width="8" height="8" patternUnits="userSpaceOnUse">
        <rect width="8" height="8" fill="url(#bg)"/>
        <line x1="0" y1="0" x2="0" y2="8" stroke="#F8FAFC" stroke-opacity="0.015" stroke-width="1"/>
    </pattern>

    <radialGradient id="amberGlow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#F0883E" stop-opacity="0.10"/>
        <stop offset="100%" stop-color="#0D1117" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#F0883E" stop-opacity="0.6"/>
        <stop offset="100%" stop-color="#0D1117" stop-opacity="0"/>
    </radialGradient>

    <filter id="blur-glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="12"/>
    </filter>

    <linearGradient id="shimmer" x1="0" y1="0" x2="1680" y2="0" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#B0681E" stop-opacity="0.6"/>
        <stop offset="50%" stop-color="#F0883E" stop-opacity="0.8"/>
        <stop offset="100%" stop-color="#B0681E" stop-opacity="0.6"/>
    </linearGradient>
</defs>

<rect width="{W}" height="{H}" rx="14" fill="url(#pinstripe)"/>

<!-- TOP HEADER & SUB-HEADER -->
<g transform="translate(55, 60)">
    <text x="0" y="0" font-size="21" fill="#F0883E" font-weight="700" letter-spacing="1.5">// ENTERPRISE SECURITY ARCHITECT &amp; CORE INFRASTRUCTURE SYSTEMS ENGINEER</text>
    <text x="0" y="32" font-size="16" fill="#94A3B8" font-weight="600" letter-spacing="0.4">Hands-on Architecture: Infrastructure Hardening (CND) • Enterprise Networks (CCNA) • Offensive Labs (CEH) • DFIR Investigation (CHFI)</text>
</g>

<!-- TACTICAL ORBIT MATRIX (CSS TRANSFORM PATH-LOCKED) -->
<g transform="translate(255, 460)">
    <!-- Subtle background glow behind the entire orbit system -->
    <circle cx="0" cy="0" r="180" fill="url(#amberGlow)"/>

    <!-- ================= SECONDARY ORBIT TRACK 3 (Language Outer, Rotated -10deg) ================= -->
    <g transform="rotate(-10)">
        <ellipse cx="0" cy="0" rx="270" ry="115" fill="none" stroke="#484F58" stroke-width="0.8" stroke-dasharray="2 5" opacity="0.6"/>
        <!-- Scale Y by 115/270 = 0.42592 -->
        <g transform="scale(1, 0.42592)">
            <g class="orbit-track-3">
                <!-- PY Node (0 deg) -->
                <g transform="rotate(0)">
                    <g transform="translate(270, 0)">
                        <g transform="rotate(0)">
                            <g class="counter-text-3">
                                <!-- Un-scale Y by 1/0.42592 = 2.34785 -->
                                <g transform="scale(1, 2.34785)">
                                    <g transform="rotate(10)">
                                        <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#484F58" stroke-opacity="0.8" stroke-width="1.2"/>
                                        <text x="0" y="0" dy=".32em" font-size="8" fill="#8B949E" font-weight="600" text-anchor="middle">PY</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- BASH Node (60 deg) -->
                <g transform="rotate(60)">
                    <g transform="translate(270, 0)">
                        <g transform="rotate(-60)">
                            <g class="counter-text-3">
                                <g transform="scale(1, 2.34785)">
                                    <g transform="rotate(10)">
                                        <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#484F58" stroke-opacity="0.8" stroke-width="1.2"/>
                                        <text x="0" y="0" dy=".32em" font-size="7.5" fill="#8B949E" font-weight="600" text-anchor="middle">BASH</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- SQL Node (120 deg) -->
                <g transform="rotate(120)">
                    <g transform="translate(270, 0)">
                        <g transform="rotate(-120)">
                            <g class="counter-text-3">
                                <g transform="scale(1, 2.34785)">
                                    <g transform="rotate(10)">
                                        <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#484F58" stroke-opacity="0.8" stroke-width="1.2"/>
                                        <text x="0" y="0" dy=".32em" font-size="8" fill="#8B949E" font-weight="600" text-anchor="middle">SQL</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- C/C++ Node (180 deg) -->
                <g transform="rotate(180)">
                    <g transform="translate(270, 0)">
                        <g transform="rotate(-180)">
                            <g class="counter-text-3">
                                <g transform="scale(1, 2.34785)">
                                    <g transform="rotate(10)">
                                        <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#484F58" stroke-opacity="0.8" stroke-width="1.2"/>
                                        <text x="0" y="0" dy=".32em" font-size="7.5" fill="#8B949E" font-weight="600" text-anchor="middle">C/C++</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- YAML Node (240 deg) -->
                <g transform="rotate(240)">
                    <g transform="translate(270, 0)">
                        <g transform="rotate(-240)">
                            <g class="counter-text-3">
                                <g transform="scale(1, 2.34785)">
                                    <g transform="rotate(10)">
                                        <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#484F58" stroke-opacity="0.8" stroke-width="1.2"/>
                                        <text x="0" y="0" dy=".32em" font-size="7.5" fill="#8B949E" font-weight="600" text-anchor="middle">YAML</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- PS Node (300 deg) -->
                <g transform="rotate(300)">
                    <g transform="translate(270, 0)">
                        <g transform="rotate(-300)">
                            <g class="counter-text-3">
                                <g transform="scale(1, 2.34785)">
                                    <g transform="rotate(10)">
                                        <circle cx="0" cy="0" r="16" fill="#161B22" stroke="#484F58" stroke-opacity="0.8" stroke-width="1.2"/>
                                        <text x="0" y="0" dy=".32em" font-size="8" fill="#8B949E" font-weight="600" text-anchor="middle">PS</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>

    <!-- ================= PRIMARY ORBIT TRACK 1 (Outer, Rotated -20deg) ================= -->
    <g transform="rotate(-20)">
        <ellipse cx="0" cy="0" rx="195" ry="72" fill="none" stroke="#F0883E" stroke-width="1.5" stroke-opacity="0.4"/>
        <!-- Scale Y by 72/195 = 0.36923 -->
        <g transform="scale(1, 0.36923)">
            <g class="orbit-track-1">
                <!-- SOC Node (0 deg) -->
                <g transform="rotate(0)">
                    <g transform="translate(195, 0)">
                        <g transform="rotate(0)">
                            <g class="counter-text-1">
                                <!-- Un-scale Y by 1/0.36923 = 2.70833 -->
                                <g transform="scale(1, 2.70833)">
                                    <!-- Un-rotate the track's -20deg -->
                                    <g transform="rotate(20)">
                                        <circle cx="0" cy="0" r="24" fill="#161B22" stroke="#F0883E" stroke-width="1.5"/>
                                        <text x="0" y="0" dy=".3em" font-size="11" fill="#FFFFFF" font-weight="700" text-anchor="middle">SOC</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- DFIR Node (180 deg) -->
                <g transform="rotate(180)">
                    <g transform="translate(195, 0)">
                        <g transform="rotate(-180)">
                            <g class="counter-text-1">
                                <g transform="scale(1, 2.70833)">
                                    <g transform="rotate(20)">
                                        <circle cx="0" cy="0" r="24" fill="#161B22" stroke="#F0883E" stroke-width="1.5"/>
                                        <text x="0" y="0" dy=".3em" font-size="11" fill="#FFFFFF" font-weight="700" text-anchor="middle">DFIR</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>

    <!-- ================= PRIMARY ORBIT TRACK 2 (Inner, Rotated 35deg) ================= -->
    <g transform="rotate(35)">
        <ellipse cx="0" cy="0" rx="145" ry="55" fill="none" stroke="#484F58" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.8"/>
        <!-- Scale Y by 55/145 = 0.37931 -->
        <g transform="scale(1, 0.37931)">
            <g class="orbit-track-2">
                <!-- ZT Node (60 deg) -->
                <g transform="rotate(60)">
                    <g transform="translate(145, 0)">
                        <g transform="rotate(-60)">
                            <g class="counter-text-2">
                                <!-- Un-scale Y by 1/0.37931 = 2.63636 -->
                                <g transform="scale(1, 2.63636)">
                                    <!-- Un-rotate the track's 35deg -->
                                    <g transform="rotate(-35)">
                                        <circle cx="0" cy="0" r="24" fill="#161B22" stroke="#F0883E" stroke-width="1.5"/>
                                        <text x="0" y="0" dy=".3em" font-size="11" fill="#FFFFFF" font-weight="700" text-anchor="middle">ZT</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- PKI Node (180 deg) -->
                <g transform="rotate(180)">
                    <g transform="translate(145, 0)">
                        <g transform="rotate(-180)">
                            <g class="counter-text-2">
                                <g transform="scale(1, 2.63636)">
                                    <g transform="rotate(-35)">
                                        <circle cx="0" cy="0" r="24" fill="#161B22" stroke="#F0883E" stroke-width="1.5"/>
                                        <text x="0" y="0" dy=".3em" font-size="11" fill="#FFFFFF" font-weight="700" text-anchor="middle">PKI</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- RE Node (300 deg) -->
                <g transform="rotate(300)">
                    <g transform="translate(145, 0)">
                        <g transform="rotate(-300)">
                            <g class="counter-text-2">
                                <g transform="scale(1, 2.63636)">
                                    <g transform="rotate(-35)">
                                        <circle cx="0" cy="0" r="24" fill="#161B22" stroke="#F0883E" stroke-width="1.5"/>
                                        <text x="0" y="0" dy=".3em" font-size="11" fill="#FFFFFF" font-weight="700" text-anchor="middle">RE</text>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>

    <!-- STATIONARY CENTRAL SHIELD -->
    <circle cx="0" cy="0" r="56" fill="url(#coreGlow)" filter="url(#blur-glow)" class="core-pulse"/>
    <circle cx="0" cy="0" r="46" fill="#161B22" stroke="#F0883E" stroke-width="2" class="core-pulse"/>

    <g transform="translate(0, 0) scale(1.2)">
        <path d="M0 -13 C9 -13 15 -7 15 0 C15 9 9 17 0 21 C-9 17 -15 9 -15 0 C-15 -7 -9 -13 0 -13 Z" fill="none" stroke="#F0883E" stroke-width="1.8"/>
        <path d="M-4 1 L-1 5 L6 -3" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
</g>

<!-- RIGHT: ORGANIZED CAPSULE MATRIX GRID -->
<g transform="translate(530, 140)">
    <g transform="translate(0, 0)">
        <text x="0" y="22" font-size="16" fill="#F0883E" font-weight="700">[❯]</text>
        <text x="26" y="22" font-size="16" fill="#F8FAFC" font-weight="700" letter-spacing="0.5">ENGINEERING MILESTONES &amp; CORE SYSTEMS</text>
        <g transform="translate(0, 34)">
            <rect class="capsule" x="0" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#F0883E" stroke-width="1.5"/>
            <text x="18" y="32" font-size="15" fill="#FFFFFF" font-weight="600">✓ 5-Node 104GB Cluster</text>
            <rect class="capsule" x="278" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#F0883E" stroke-width="1.5"/>
            <text x="296" y="32" font-size="15" fill="#FFFFFF" font-weight="600">✓ Silent Vector Mini-OS</text>
            <rect class="capsule" x="556" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#F0883E" stroke-width="1.5"/>
            <text x="574" y="32" font-size="15" fill="#FFFFFF" font-weight="600">✓ Custom C-TLS VPN (PKI)</text>
            <rect class="capsule" x="834" y="0" width="250" height="52" rx="8" fill="#161B22" stroke="#F0883E" stroke-width="1.5"/>
            <text x="852" y="32" font-size="15" fill="#FFFFFF" font-weight="600">✓ Enterprise Simulation</text>
        </g>
    </g>

    <g transform="translate(0, 126)">
        <text x="0" y="22" font-size="16" fill="#F0883E" font-weight="700">[❯]</text>
        <text x="26" y="22" font-size="16" fill="#F8FAFC" font-weight="700" letter-spacing="0.5">SOC, SIEM &amp; HARDENING (CND / BLUE TEAM)</text>
        <g transform="translate(0, 34)">
            <rect class="capsule" x="0" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="18" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Wazuh SIEM</tspan><tspan fill="#94A3B8"> &amp; Suricata</tspan></text>
            <rect class="capsule" x="278" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="296" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Shuffle SOAR</tspan><tspan fill="#94A3B8"> &amp; RITA</tspan></text>
            <rect class="capsule" x="556" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="574" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">FortiGate</tspan><tspan fill="#94A3B8"> &amp; Hardening</tspan></text>
            <rect class="capsule" x="834" y="0" width="250" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="852" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Maltego</tspan><tspan fill="#94A3B8"> &amp; OSINT</tspan></text>
        </g>
    </g>

    <g transform="translate(0, 252)">
        <text x="0" y="22" font-size="16" fill="#F0883E" font-weight="700">[❯]</text>
        <text x="26" y="22" font-size="16" fill="#F8FAFC" font-weight="700" letter-spacing="0.5">DIGITAL FORENSICS (CHFI / ACTIVE LABS)</text>
        <g transform="translate(0, 34)">
            <rect class="capsule" x="0" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="18" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Autopsy</tspan><tspan fill="#94A3B8"> &amp; FTK Imager</tspan></text>
            <rect class="capsule" x="278" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="296" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">WinHex</tspan><tspan fill="#94A3B8"> &amp; $MFT Carving</tspan></text>
            <rect class="capsule" x="556" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="574" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Wireshark</tspan><tspan fill="#94A3B8"> PCAP Analysis</tspan></text>
            <rect class="capsule" x="834" y="0" width="250" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="852" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Chain of Custody</tspan><tspan fill="#94A3B8"> Records</tspan></text>
        </g>
    </g>

    <g transform="translate(0, 378)">
        <text x="0" y="22" font-size="16" fill="#F0883E" font-weight="700">[❯]</text>
        <text x="26" y="22" font-size="16" fill="#F8FAFC" font-weight="700" letter-spacing="0.5">REVERSE ENGINEERING &amp; ATTACKS (CEH)</text>
        <g transform="translate(0, 34)">
            <rect class="capsule" x="0" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="18" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Ghidra</tspan><tspan fill="#94A3B8"> (AI-Assisted RE)</tspan></text>
            <rect class="capsule" x="278" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="296" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Metasploit</tspan><tspan fill="#94A3B8"> &amp; Pivoting</tspan></text>
            <rect class="capsule" x="556" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="574" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">ANY.RUN</tspan><tspan fill="#94A3B8"> &amp; OllyDbg</tspan></text>
            <rect class="capsule" x="834" y="0" width="250" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="852" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">SQLi, Gophish</tspan><tspan fill="#94A3B8"> &amp; SET</tspan></text>
        </g>
    </g>

    <g transform="translate(0, 504)">
        <text x="0" y="22" font-size="16" fill="#F0883E" font-weight="700">[❯]</text>
        <text x="26" y="22" font-size="16" fill="#F8FAFC" font-weight="700" letter-spacing="0.5">DEVSECOPS &amp; ENVIRONMENT PIPELINES</text>
        <g transform="translate(0, 34)">
            <rect class="capsule" x="0" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="18" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Semgrep</tspan><tspan fill="#94A3B8"> &amp; OWASP ZAP</tspan></text>
            <rect class="capsule" x="278" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="296" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">pip-audit</tspan><tspan fill="#94A3B8"> / Safety SCA</tspan></text>
            <rect class="capsule" x="556" y="0" width="265" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="574" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Docker</tspan><tspan fill="#94A3B8"> &amp; Nginx Proxy</tspan></text>
            <rect class="capsule" x="834" y="0" width="250" height="52" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
            <text x="852" y="32" font-size="15"><tspan fill="#FFFFFF" font-weight="600">Samba</tspan><tspan fill="#94A3B8"> Active Directory</tspan></text>
        </g>
    </g>
</g>

<rect width="{W-3}" height="{H-3}" x="1.5" y="1.5" rx="14" fill="none" stroke="url(#shimmer)" stroke-width="1.8" opacity="0.85"/>

</svg>"""

    with open(f"{OUT}/assets-b/tech-stack.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated 100% path-locked CSS-animated assets-b/tech-stack.svg successfully!")

if __name__ == "__main__":
    generate_tech_stack_svg()