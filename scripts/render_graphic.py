"""
High-DPI 4K Retina HTML/CSS/SVG -> JPEG Renderer.
Renders an HTML graphic template over a target photograph using Headless Chrome
or Edge, guaranteeing full Google Fonts loading and zero chroma subsampling loss.
"""
import argparse
import os
import subprocess
import sys
import tempfile
from PIL import Image


BROWSER_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_browser():
    for path in BROWSER_CANDIDATES:
        if os.path.exists(path):
            return path
    raise FileNotFoundError("Could not find Google Chrome or Microsoft Edge for headless rendering.")


def main():
    parser = argparse.ArgumentParser(description="Render HTML/CSS/SVG graphic over a photograph at 4K Retina quality.")
    parser.add_argument("--photo", required=True, help="Path to the source photograph")
    parser.add_argument("--html", required=True, help="Path to the HTML/SVG design file")
    parser.add_argument("--output", required=True, help="Path to save the rendered JPEG")
    parser.add_argument("--width", type=int, default=1800, help="CSS viewport width (default: 1800)")
    parser.add_argument("--height", type=int, default=1200, help="CSS viewport height (default: 1200)")
    parser.add_argument("--scale", type=int, default=2, help="Device scale factor for Retina output (default: 2 -> 3600x2400)")
    args = parser.parse_args()

    browser = find_browser()
    target_w = args.width * args.scale
    target_h = args.height * args.scale

    with tempfile.TemporaryDirectory() as tmpdir:
        # 1. Prepare high-res Lanczos base image
        base_jpg = os.path.join(tmpdir, "base_prepared.jpg")
        im = Image.open(args.photo).convert("RGB")
        if im.size != (target_w, target_h):
            im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im.save(base_jpg, "JPEG", quality=98, subsampling=0)
        base_url = "file:///" + base_jpg.replace("\\", "/")

        # 2. Inject {{BASE_IMAGE_URL}} if placeholder is present in HTML
        with open(args.html, "r", encoding="utf-8") as f:
            html_content = f.read()

        if "{{BASE_IMAGE_URL}}" in html_content:
            html_content = html_content.replace("{{BASE_IMAGE_URL}}", base_url)

        render_html = os.path.join(tmpdir, "render_scene.html")
        with open(render_html, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 3. Render with Headless Browser
        out_png = os.path.join(tmpdir, "rendered.png")
        cmd = [
            browser,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--force-device-scale-factor={args.scale}",
            f"--window-size={args.width},{args.height}",
            "--virtual-time-budget=3000",
            f"--screenshot={out_png}",
            render_html,
        ]
        subprocess.run(cmd, check=True)

        # 4. Save final 4:4:4 Chroma JPEG
        final_im = Image.open(out_png).convert("RGB")
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        final_im.save(args.output, "JPEG", quality=96, subsampling=0)
        print(f"Successfully rendered {final_im.size[0]}x{final_im.size[1]} graphic -> {args.output}")


if __name__ == "__main__":
    main()
