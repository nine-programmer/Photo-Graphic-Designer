"""
Analyze a photograph's resolution, aspect ratio, EXIF metadata, 3x3 grid luminance
& texture variance (to automatically locate the best Negative Space for typography),
and extract dominant/accent hex colors for harmonious graphic design.
"""
import sys
import os
import json
from math import gcd
from PIL import Image, ImageStat, ExifTags


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


def analyze_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: File not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    im = Image.open(image_path)
    width, height = im.size
    div = gcd(width, height)
    aspect_str = f"{width // div}:{height // div}"

    # Read EXIF
    exif_data = {}
    try:
        raw_exif = im.getexif()
        for k, v in raw_exif.items():
            tag = ExifTags.TAGS.get(k, k)
            if isinstance(v, (str, int, float)):
                exif_data[str(tag)] = v
    except Exception:
        pass

    # Downsample for fast grid & palette analysis
    small = im.convert("RGB").resize((600, 400), Image.Resampling.BILINEAR)
    sw, sh = small.size

    grid_names = [
        ["Top-Left", "Top-Center", "Top-Right"],
        ["Mid-Left", "Center", "Mid-Right"],
        ["Bottom-Left", "Bottom-Center", "Bottom-Right"],
    ]

    grid_report = []
    best_zones = []

    for r in range(3):
        for c in range(3):
            box = (
                int(c * sw / 3),
                int(r * sh / 3),
                int((c + 1) * sw / 3),
                int((r + 1) * sh / 3),
            )
            crop_rgb = small.crop(box)
            crop_l = crop_rgb.convert("L")
            stat_rgb = ImageStat.Stat(crop_rgb)
            stat_l = ImageStat.Stat(crop_l)

            mean_l = stat_l.mean[0]       # 0 (black) to 255 (white)
            std_l = stat_l.stddev[0]      # Texture/clutter complexity
            avg_hex = rgb_to_hex(stat_rgb.mean)

            tone = "Dark" if mean_l < 75 else ("Bright" if mean_l > 175 else "Mid-tone")
            clutter = "Low (Smooth/Open Sky)" if std_l < 28 else ("High (Busy/Subject)" if std_l > 52 else "Moderate")

            zone_info = {
                "zone": grid_names[r][c],
                "luminance_0_255": round(mean_l, 1),
                "texture_stddev": round(std_l, 1),
                "tone": tone,
                "clutter": clutter,
                "avg_color_hex": avg_hex,
                "recommended_text_color": "#FFFAF0 (Warm White)" if mean_l < 135 else "#1C2536 (Deep Navy)",
            }
            grid_report.append(zone_info)
            if std_l < 35 and r < 2:
                best_zones.append(grid_names[r][c])

    # Extract quantized 5-color palette
    quantized = small.quantize(colors=5, method=Image.Quantize.MEDIANCUT).convert("RGB")
    colors = quantized.getcolors(600 * 400)
    colors.sort(reverse=True, key=lambda x: x[0])
    palette = [rgb_to_hex(rgb) for count, rgb in colors[:5]]

    report = {
        "file": os.path.basename(image_path),
        "dimensions": f"{width}x{height}",
        "aspect_ratio": aspect_str,
        "exif": exif_data,
        "dominant_palette_hex": palette,
        "recommended_negative_space_zones": best_zones or ["Top-Center", "Top-Right"],
        "grid_3x3_analysis": grid_report,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_photo.py <image_path>")
        sys.exit(1)
    analyze_image(sys.argv[1])
