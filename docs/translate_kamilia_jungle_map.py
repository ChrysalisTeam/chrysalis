"""Build the English Kamilia jungle map from the French one, by replacing its 12 labels.

Usage (from the docs/ folder):
    python translate_kamilia_jungle_map.py ../alternate_reality_game_auction/images/world_maps/kamilia_jungle_map_fr.jpg ../alternate_reality_game_auction/images/world_maps/kamilia_jungle_map_en.jpg
(needs Pillow and the Windows Arial font)
"""
import statistics
import sys

from PIL import Image, ImageDraw, ImageFont

SOURCE, TARGET = sys.argv[1], sys.argv[2]
FONT_PATH = r"C:\Windows\Fonts\ARIAL_0.TTF"
FONT_SIZE = 14
LINE_HEIGHT = 18  # baseline-to-baseline distance of the original 2-line labels

# (box of the FR label: x0, y0, x1, y1 of its cap-height text), EN lines, alignment ("left" or "center")
LABELS = [
    ((645, 162, 723, 171), ["Windswept Mount"], "center"),
    ((410, 173, 503, 200), ["Cavern of the", "Invisible Giant"], "left"),
    ((832, 187, 973, 196), ["Dry Trees Mound"], "center"),
    ((298, 252, 365, 280), ["Kupoutac", "Plateau"], "left"),
    ((36, 269, 118, 295), ["Western Edge", "of the Birds"], "left"),
    ((677, 304, 787, 313), ["Glittering Brook"], "center"),
    ((794, 389, 902, 397), ["Muddy Brook"], "left"),
    ((294, 406, 388, 433), ["Brook of the", "1000 Branches"], "left"),
    ((752, 428, 857, 437), ["Valley of the Breath"], "left"),
    ((626, 488, 749, 497), ["Cascading River"], "center"),
    ((407, 574, 507, 583), ["Baboon Rock"], "center"),
    ((681, 611, 813, 622), ["Black Needle Peak"], "center"),
]


def is_label_pixel(r, g, b):
    # anti-aliased dark-blue text: red ~ green, blue clearly above; rivers have green >> red, outlines are grey
    return g - r < 30 and b - r > 4 and b - g > 4


im = Image.open(SOURCE).convert("RGB")
px = im.load()

# text colour = median of the most saturated label pixels
samples = []
for (x0, y0, x1, y1), _, _ in LABELS:
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            r, g, b = px[x, y]
            if b - r > 100 and abs(r - g) < 20:
                samples.append((r, g, b))
samples.sort(key=lambda c: c[0] + c[1] - 2 * c[2])  # most saturated first
samples = samples[:max(1, len(samples) // 3)]
color = tuple(int(statistics.median(c[i] for c in samples)) for i in range(3))
color = (36, 36, 192)  # anti-aliasing lightens the strokes, so the fill must be deeper than the sampled cores
print("text colour:", color, "from", len(samples), "pixels")

# erase the French labels (with margins for accents and descenders)
for (x0, y0, x1, y1), _, _ in LABELS:
    for y in range(y0 - 5, y1 + 6):
        for x in range(x0 - 8, x1 + 9):
            if is_label_pixel(*px[x, y]) or min(px[x, y]) >= 190:  # also JPEG halos
                px[x, y] = (255, 255, 255)

draw = ImageDraw.Draw(im)
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
cap_top = font.getbbox("H")[1]  # offset between the drawing origin and the top of capitals
for (x0, y0, x1, y1), lines, align in LABELS:
    center = (x0 + x1) / 2
    for index, line in enumerate(lines):
        top = y0 + index * LINE_HEIGHT - cap_top
        width = draw.textlength(line, font=font)
        x = x0 if align == "left" else round(center - width / 2)
        draw.text((x, top), line, fill=color, font=font)

im.save(TARGET, quality=92, dpi=(100, 100))
print("saved", TARGET)
