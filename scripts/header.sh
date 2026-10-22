#!/usr/bin/env bash
# Writes assets/header-{light,dark}.svg, the terminal at the top of the README.
#
# Usage: scripts/header.sh <out_dir> <contributions_last_year> <member_since_year>
# The weekly workflow (.github/workflows/stats.yml) reruns this with fresh numbers.
set -euo pipefail

out_dir=$1 contributions=$2 since=$3

# 5478 -> 5,478 (printf's %'d depends on the runner's locale)
with_commas() {
  local n=$1 out=""
  while [ ${#n} -gt 3 ]; do
    out=",${n: -3}$out"
    n=${n%???}
  done
  echo "$n$out"
}

# Catppuccin Mocha (dark) and Latte (light)
palette() {
  if [ "$1" = dark ]; then
    base="#1e1e2e" mantle="#181825" s0="#313244" ov="#6c7086" sub="#a6adc8"
    text="#cdd6f4" green="#a6e3a1" blue="#89b4fa" mauve="#cba6f7" red="#f38ba8" yellow="#f9e2af"
  else
    base="#eff1f5" mantle="#e6e9ef" s0="#ccd0da" ov="#9ca0b0" sub="#6c6f85"
    text="#4c4f69" green="#40a02b" blue="#1e66f5" mauve="#8839ef" red="#d20f39" yellow="#df8e1d"
  fi
}

svg() {
  local W=880 H=248
  cat <<SVG
<svg xmlns="http://www.w3.org/2000/svg" width="$W" height="$H" viewBox="0 0 $W $H" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="15">
  <style>
    .cursor { animation: blink 1.1s steps(1) infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    /* the cover slides right one character at a time to "type" the command */
    .cover { animation: type 1.8s steps(45) 0.8s both; }
    @keyframes type { from { transform: translateX(0); } to { transform: translateX(440px); } }
    .output { animation: show 0.01s 2.9s both; }
    @keyframes show { from { opacity: 0; } to { opacity: 1; } }
    @media (prefers-reduced-motion: reduce) {
      .cursor, .output { animation: none; }
      .cover { display: none; }
    }
  </style>
  <rect x="0.5" y="0.5" width="$((W - 1))" height="$((H - 1))" rx="12" fill="$base" stroke="$s0"/>
  <path d="M12.5 0.5h$((W - 25))a12 12 0 0 1 12 12v22.5h-$((W - 1))v-22.5a12 12 0 0 1 12-12z" fill="$mantle"/>
  <line x1="0.5" y1="35" x2="$((W - 1)).5" y2="35" stroke="$s0"/>
  <circle cx="22" cy="18" r="6" fill="$red"/><circle cx="42" cy="18" r="6" fill="$yellow"/><circle cx="62" cy="18" r="6" fill="$green"/>
  <text x="$((W / 2))" y="23" text-anchor="middle" font-size="13" fill="$ov">mifwar — tmux</text>

  <text x="28" y="72"><tspan fill="$blue">~</tspan><tspan fill="$mauve"> ❯ </tspan><tspan fill="$text">whoami</tspan></text>
  <text x="28" y="100" font-size="22" font-weight="700" fill="$text">Miftahul Anwar</text>
  <text x="28" y="126" fill="$sub">software engineer <tspan fill="$ov">·</tspan> Zenius Education <tspan fill="$ov">·</tspan> Indonesia</text>
  <text x="28" y="150" fill="$ov"><tspan fill="$sub">$(with_commas "$contributions")</tspan> contributions in the last year · on GitHub since <tspan fill="$sub">$since</tspan></text>

  <text x="28" y="190"><tspan fill="$blue">~</tspan><tspan fill="$mauve"> ❯ </tspan></text>
  <text x="64" y="190" fill="$text">crew up profile lead=claude impl=codex rev=pi</text>
  <rect class="cover" x="62" y="172" width="440" height="24" fill="$base"/>
  <text class="output" x="28" y="216" fill="$sub"><tspan fill="$green">●</tspan> claude plans  <tspan fill="$green">●</tspan> codex builds  <tspan fill="$yellow">●</tspan> pi reviews  <tspan fill="$ov">· three agents, one tmux window</tspan><tspan class="cursor" fill="$text"> ▍</tspan></text>
</svg>
SVG
}

for scheme in light dark; do
  palette "$scheme"
  svg > "$out_dir/header-$scheme.svg"
done
