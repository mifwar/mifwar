"""Writes assets/header-{light,dark}.svg, the terminal at the top of the README.

Usage: python3 scripts/header.py <out_dir> <contributions_last_year> <member_since_year>
The weekly workflow (.github/workflows/stats.yml) reruns this with fresh numbers.
"""
import sys

# Catppuccin Mocha (dark) and Latte (light)
PALETTES = {
    "dark": dict(base="#1e1e2e", mantle="#181825", s0="#313244", ov="#6c7086", sub="#a6adc8",
                 text="#cdd6f4", green="#a6e3a1", blue="#89b4fa", mauve="#cba6f7",
                 red="#f38ba8", yellow="#f9e2af"),
    "light": dict(base="#eff1f5", mantle="#e6e9ef", s0="#ccd0da", ov="#9ca0b0", sub="#6c6f85",
                  text="#4c4f69", green="#40a02b", blue="#1e66f5", mauve="#8839ef",
                  red="#d20f39", yellow="#df8e1d"),
}


def svg(p, contributions, since):
    W, H = 880, 248
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="15">
  <style>
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    /* the cover slides right one character at a time to "type" the command */
    .cover {{ animation: type 1.8s steps(45) 0.8s both; }}
    @keyframes type {{ from {{ transform: translateX(0); }} to {{ transform: translateX(440px); }} }}
    .output {{ animation: show 0.01s 2.9s both; }}
    @keyframes show {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .cursor, .output {{ animation: none; }}
      .cover {{ display: none; }}
    }}
  </style>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="{p['base']}" stroke="{p['s0']}"/>
  <path d="M12.5 0.5h{W-25}a12 12 0 0 1 12 12v22.5h-{W-1}v-22.5a12 12 0 0 1 12-12z" fill="{p['mantle']}"/>
  <line x1="0.5" y1="35" x2="{W-0.5}" y2="35" stroke="{p['s0']}"/>
  <circle cx="22" cy="18" r="6" fill="{p['red']}"/><circle cx="42" cy="18" r="6" fill="{p['yellow']}"/><circle cx="62" cy="18" r="6" fill="{p['green']}"/>
  <text x="{W/2}" y="23" text-anchor="middle" font-size="13" fill="{p['ov']}">mifwar — tmux</text>

  <text x="28" y="72"><tspan fill="{p['blue']}">~</tspan><tspan fill="{p['mauve']}"> ❯ </tspan><tspan fill="{p['text']}">whoami</tspan></text>
  <text x="28" y="100" font-size="22" font-weight="700" fill="{p['text']}">Miftahul Anwar</text>
  <text x="28" y="126" fill="{p['sub']}">software engineer <tspan fill="{p['ov']}">·</tspan> Zenius Education <tspan fill="{p['ov']}">·</tspan> Indonesia</text>
  <text x="28" y="150" fill="{p['ov']}"><tspan fill="{p['sub']}">{contributions:,}</tspan> contributions in the last year · on GitHub since <tspan fill="{p['sub']}">{since}</tspan></text>

  <text x="28" y="190"><tspan fill="{p['blue']}">~</tspan><tspan fill="{p['mauve']}"> ❯ </tspan></text>
  <text x="64" y="190" fill="{p['text']}">crew up profile lead=claude impl=codex rev=pi</text>
  <rect class="cover" x="62" y="172" width="440" height="24" fill="{p['base']}"/>
  <text class="output" x="28" y="216" fill="{p['sub']}"><tspan fill="{p['green']}">●</tspan> claude plans  <tspan fill="{p['green']}">●</tspan> codex builds  <tspan fill="{p['yellow']}">●</tspan> pi reviews  <tspan fill="{p['ov']}">· three agents, one tmux window</tspan><tspan class="cursor" fill="{p['text']}"> ▍</tspan></text>
</svg>
'''


if __name__ == "__main__":
    out_dir, contributions, since = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    for name, palette in PALETTES.items():
        with open(f"{out_dir}/header-{name}.svg", "w") as f:
            f.write(svg(palette, contributions, since))
