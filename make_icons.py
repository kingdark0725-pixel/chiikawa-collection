#!/usr/bin/env python3
import subprocess, sys

# Install cairosvg if needed
try:
    import cairosvg
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cairosvg', '--break-system-packages', '-q'])
    import cairosvg

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="100" fill="#E8724A"/>
  <circle cx="256" cy="200" r="110" fill="#FFF8F0"/>
  <circle cx="210" cy="175" r="38" fill="#FFF8F0" stroke="#E8724A" stroke-width="4"/>
  <circle cx="302" cy="175" r="38" fill="#FFF8F0" stroke="#E8724A" stroke-width="4"/>
  <circle cx="256" cy="220" r="85" fill="#FFF8F0"/>
  <circle cx="230" cy="210" r="10" fill="#333"/>
  <circle cx="282" cy="210" r="10" fill="#333"/>
  <ellipse cx="256" cy="238" rx="14" ry="10" fill="#F4A0A0"/>
  <path d="M238 250 Q256 268 274 250" stroke="#333" stroke-width="3" fill="none" stroke-linecap="round"/>
  <text x="256" y="360" text-anchor="middle" font-family="sans-serif" font-size="52" font-weight="bold" fill="#FFF8F0">ちいかわ</text>
  <text x="256" y="420" text-anchor="middle" font-family="sans-serif" font-size="32" fill="#FFD9C8">ご当地コレクション</text>
</svg>'''

for size in [192, 512]:
    cairosvg.svg2png(bytestring=svg.encode(), write_to=f'/home/claude/chiikawa-pwa/icons/icon-{size}.png', output_width=size, output_height=size)
    print(f'icon-{size}.png created')
