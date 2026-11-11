---
name: photo-graphic-designer
description: >-
  Use this skill whenever the user wants to add text graphics, typography, decorative patterns,
  frames, illustrations, badges, or postcard/poster layouts onto a photograph (such as birthday
  posts, travel/camping memories, anniversaries, or social media cards). Provides an end-to-end
  professional Art Director workflow covering visual composition analysis, directional flow,
  color harmony, 12+ curated design styles, authentic multi-tone Thai/English copywriting,
  and 4K Retina HTML/CSS/SVG vector rendering without distorting the original photo.
---

# Professional Photo Graphic Designer & Art Director Skill

This skill transforms raw photographs into studio-grade social media graphics, postcards, and commemorative posters. Instead of using AI image generation over photos (which distorts faces, alters skies, and garbles Thai typography), this workflow uses **HTML5 + CSS3 + Custom SVG Vector Artwork + Google Fonts**, rendered at **4K Retina resolution (`--force-device-scale-factor=2`)** via Headless Chrome and composited with Python `Pillow` (`subsampling=0`).

---

## Core Workflow (6 Phases)

### Phase 1: Photo Inspection & Automated Visual Analysis

1. **View the Target Photo**: Always call `read_file` on the target image first to visually understand the subject, mood, lighting, and obstacles (e.g., faces, tent poles, guy-lines, horizons, trees).
2. **Run the Photo Analyzer Script**:
   Execute [analyze_photo.py](./scripts/analyze_photo.py) on the target image to extract:
   - Exact pixel dimensions, aspect ratio, and EXIF metadata.
   - A **3×3 Grid Luminance & Negative Space Map** (identifies which zones are dark, mid-tone, or bright, and which zones have low detail suitable for typography).
   - **Extracted Color Palette** (dominant background hex colors + recommended high-contrast accent hex colors).
   ```powershell
   python ".agents/skills/photo-graphic-designer/scripts/analyze_photo.py" "<image_path>"
   ```

---

### Phase 2: Interactive Style & Direction Discovery

Before generating graphics, consult [style_catalog.md](./references/style_catalog.md) and use `ask_question` to let the user choose from curated design directions tailored to their photo:

1. **Design Style Selection** (Present 3–5 best-fitting styles from the 12+ styles in [style_catalog.md](./references/style_catalog.md), plus an option to generate multiple styles to compare):
   - *Celestial & Starry Romance* (Luxury gold serif, constellation lines, glowing starlight, astrolabe borders)
   - *Minimal Editorial / Magazine Postcard* (*Kinfolk* / *GO OUT* / *NatGeo* layout, hairline grids, metadata header, location stamp)
   - *Warm & Cute Hand-Drawn Doodle* (Cozy fairy lights, sketchy dashed borders, floating hearts, curved pointer arrows, handwritten script)
   - *Vintage Film & Analog Kodachrome* (Halation glow, film border frame, date stamp, retro serif)
   - *Modern Glassmorphism & Floating UI* (Frosted glass cards, music player / memory bar, sleek sans-serif)
   - *Outdoor Adventure & Retro Badge* (National Park / Camping emblem, topographic lines, compass & pine tree vectors)
   - *Japanese Minimalist Poster (Zakka / Muji Vibe)* (Vertical/asymmetric typography, generous whitespace, delicate line art)
   - *Cinematic Letterbox & Story Subtitles* (Anamorphic bars, movie title credit block, poetic bilingual subtitle)
2. **Aspect Ratio & Output Format**:
   - Original aspect ratio (e.g., 3:2 Landscape `3600×2400`)
   - Portrait Social Feed (4:5 `2400×3000`)
   - Square (1:1 `2800×2800`) or Story/Reel (9:16 `2160×3840`)

---

### Phase 3: Multi-Tone Copywriting Workshop (Crucial!)

Generic or overly cheesy quotes often feel unnatural (*"ไม่ใช่ตัวเอง"*). Before finalizing text—or when the user asks for wording ideas—read [copywriting_tones.md](./references/copywriting_tones.md) and use `ask_question` to let the user select or mix-and-match wording by **section** and **personality tone**:

- **Break the text into modular slots**:
  1. **Top Badge / Eyebrow** (e.g., English title or occasion tag)
  2. **Main Headline** (Primary Thai/English greeting)
  3. **Subtitle / Core Anchor** (Warm key phrase)
  4. **Body Message / Quote Box** (2-line heartfelt message—or option to omit for a cleaner look)
  5. **Subject Callout / Pointer Note** (Short cute label next to a hand-drawn arrow pointing to the person/subject—or option to omit)
- **Offer 5–6 distinct personality tones per slot**:
  - **สายลุย-ชิลล์ๆ (Outdoor / Chill Partner)**: Natural, relaxed, adventure-buddy vibe.
  - **แมนๆ จริงใจ ไม่เลี่ยน (Sincere & Grounded)**: Honest, warm, zero cringe.
  - **อบอุ่น-เรียบง่าย (Warm & Classic)**: Gentle, appreciative, timeless.
  - **กวนนิดๆ กันเอง (Playful & Teasing)**: Real-couple banter with affection.
  - **โรแมนติก-ลึกซึ้ง (Poetic & Romantic)**: Starlight, destiny, deep emotion.
  - **สั้นกระชับ-มินิมอล (Short & Punchy)**: Minimalist impact.

---

### Phase 4: Composition, Directional Flow & Color Theory Rules

Consult [composition_and_color.md](./references/composition_and_color.md) when authoring the HTML/CSS/SVG overlay. Always enforce these golden rules:

1. **Subject & Obstacle Protection Zone**:
   - Map the exact bounding coordinates `(x, y)` of faces, bodies, and structural lines (such as tent poles or diagonal guy-line ropes).
   - Never let text, floating hearts, stars, or arrows cross over faces or awkwardly intersect guy-lines. Shift callout elements cleanly to one side of any rope/line.
2. **Directional Eye-Flow (Visual Vectoring)**:
   - Guide the viewer's eye from the **Primary Typography Block** (in the open negative space) -> along **Secondary Ornaments / Callout Arrows** -> directly to the **Human Subject's Face/Smile**.
   - Use curved SVG paths (`<path d="M ... Q ...">`), crescent moon orientation, or shooting star angles that point *toward* the subject or frame the text inward, never leading the eye off the edge of the canvas.
3. **Color Harmony & Adaptive Legibility**:
   - **60-30-10 Color Rule**:
     - `60%` Base photo ambient tone (e.g., Deep Midnight Navy `#0A1530` or Forest Green).
     - `30%` Primary Typography color (High-contrast Warm Ivory `#FFFAF0` or Pure Crisp White `#FFFFFF`).
     - `10%` Accent Highlight color sampled or harmonized with the scene (e.g., Warm Fairy-Light Gold `#FFE299`, Champagne `#F0CA86`, or Soft Coral Heart `#FF7B93`).
   - Always place a subtle, invisible-edge radial/linear gradient (`rgba(8, 16, 38, 0.38)`) or frosted glass container (`backdrop-filter: blur(4px)`) behind body text so typography remains 100% legible over stars, clouds, or foliage.
4. **Thai Typography Perfection**:
   - Use `white-space: nowrap` on multi-sentence Thai quote lines or explicit `<br>` line breaks at natural phrase boundaries so Thai words (like *"ฉัน"* or *"วัน"*) **never** wrap onto an orphan line by themselves.
   - Leave at least `35px–50px` of clear padding between large Thai display text (which has tall upper vowels/tone marks like `ั ิ ี ึ ื ่ ้ ๊ ๋ ์` and lower vowels `ุ ู`) and surrounding SVG stars, moons, or borders.

---

### Phase 5: 4K Retina Rendering Pipeline

Use [render_graphic.py](./scripts/render_graphic.py) to render any HTML/CSS/SVG template over the target photo at 4K resolution:

```powershell
python ".agents/skills/photo-graphic-designer/scripts/render_graphic.py" `
  --photo "DSC03461.jpg" `
  --html "path/to/design.html" `
  --output "DSC03461_Output.jpg" `
  --width 1800 --height 1200 --scale 2
```

- **Why `--scale 2` and `--virtual-time-budget=3000` matter**:
  - Designing in `1800×1200` CSS pixels with `--force-device-scale-factor=2` produces an ultra-crisp `3600×2400` Retina output.
  - `--virtual-time-budget=3000` ensures Google Fonts finishes downloading and applying before Chrome captures the frame (preventing system font fallback).
  - Saving with `quality=96, subsampling=0` preserves 100% sharp edges on colored text and thin vector lines.

---

### Phase 6: Mandatory Visual QA Verification

After rendering **every** image, you MUST inspect the generated `.jpg` file using `read_file` and verify this checklist before showing it to the user:

- [ ] **Font Verification**: Did the intended Google Fonts load properly (no Tahoma/Arial fallback)?
- [ ] **No Orphan Word Wraps**: Are all Thai sentences broken cleanly at intentional `<br>` points without single trailing words?
- [ ] **Zero Collision Check**: Do any stars, moons, hearts, borders, or arrows touch or overlap Thai vowels/tone marks, human faces, or tent ropes?
- [ ] **Visual Balance & Contrast**: Is every line of text effortlessly readable from a thumbnail view as well as full screen?

If any issue is spotted during `read_file` inspection, immediately adjust the CSS/SVG coordinates and re-render before presenting the result.

---

## Reference Templates & Documentation

- **Style Catalog & Font Pairings**: [references/style_catalog.md](./references/style_catalog.md)
- **Composition, Directional Flow & Color Guide**: [references/composition_and_color.md](./references/composition_and_color.md)
- **Thai & English Copywriting Matrix**: [references/copywriting_tones.md](./references/copywriting_tones.md)
- **Ready-to-Use HTML/SVG Reference Templates**:
  - [examples/style_starry_romantic.html](./examples/style_starry_romantic.html)
  - [examples/style_minimal_magazine.html](./examples/style_minimal_magazine.html)
  - [examples/style_warm_cute_doodle.html](./examples/style_warm_cute_doodle.html)
