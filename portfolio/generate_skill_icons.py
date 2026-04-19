from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

icons = {
    'html': 'HTML',
    'css': 'CSS',
    'javascript': 'JS',
    'react': 'RE',
    'tailwind': 'TW',
    'mongodb': 'MDB',
    'express': 'EX',
    'nodejs': 'NODE',
    'bootstrap': 'BS',
    'postgresql': 'PG',
    'java': 'JAVA',
    'c': 'C',
    'git': 'GIT',
    'github': 'GH',
    'postman': 'PM',
    'vscode': 'VS'
}

folder = Path('assets/skills')
folder.mkdir(parents=True, exist_ok=True)
size = 120

try:
    font = ImageFont.truetype('arial.ttf', 34)
except Exception:
    font = ImageFont.load_default()

for name, label in icons.items():
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([(0, 0), (size, size)], radius=24, fill=(255, 255, 255, 255), outline=(238, 238, 238, 255), width=3)
    w, h = draw.textsize(label, font=font)
    draw.text(((size - w) / 2, (size - h) / 2), label, fill=(51, 51, 51, 255), font=font)
    img.save(folder / f'{name}.png')

print('created', len(icons), 'icons in', folder.resolve())
