# Master Guide: Visual Composition, Directional Flow & Color Theory

This reference defines the Art Direction rules for placing typography and vector graphics over real-world photography so the final image looks balanced, intentional, and magazine-worthy.

---

## 1. Spatial Mapping & Negative Space Discovery

Before writing any CSS coordinates, divide the `1800×1200` (3:2) or `1200×1500` (4:5) canvas into functional zones:

1. **Primary Subject Zone (Protected)**:
   - Human faces, bodies, hands, pets, or key foreground objects.
   - **Rule**: Never place text or decorative lines across faces or heads. Leave a minimum `40px–80px` buffer around heads and shoulders.
2. **Structural Obstacle Lines (Protected)**:
   - Tent poles, diagonal guy-line ropes, tree trunks, horizon lines, fences.
   - **Rule**: Do not let floating hearts, badges, or callout arrows straddle or get cut in half by a guy-line rope or pole. Position floating elements cleanly to one side of the line.
3. **Active Negative Space (Typography Canvas)**:
   - Open sky, calm water, out-of-focus foliage, or dark shadow regions where luminance variance (texture clutter) is lowest.
   - Center the **Primary Typography Block** inside the largest continuous negative space region, aligned either:
     - **Centered Optical Axis** (for symmetrical or romantic/doodle layouts)
     - **Left-Aligned Editorial Axis** with a vertical hairline border (`border-left: 1.5px solid ...`) for magazine/modern layouts.

---

## 2. Directional Flow & Visual Vectoring

Great graphic design guides the viewer's eye through the frame in a deliberate sequence (**1 -> 2 -> 3**):

```text
[1. Primary Headline in Sky]
         │
         ▼  (Guided by Subtitle & Quote Box)
[2. Secondary Callout / Floating Hearts / Curved Arrow]
         │
         ╰──────► [3. Subject's Face / Smile]
```

### Techniques for Controlling Eye Direction:
- **Inward-Facing Ornaments**:
  - If a Crescent Moon is placed to the left of the text block, curve its opening *toward* the text (`rotate(-12deg)`), cradling the headline rather than facing away toward the border.
  - Angle shooting stars or constellation arcs so they sweep *toward* the center of interest.
- **Curved Callout Arrows**:
  - Use quadratic Bezier SVG curves (`<path d="M x1,y1 Q cx,cy x2,y2" />`) with a hand-drawn dashed stroke (`stroke-dasharray="6 5"`) that starts near the callout label and curves gently toward the subject's smile or shoulder, stopping `25px–40px` short of touching their face/hair.
- **Counter-Balance**:
  - When a heavy foreground element occupies the **Left** side of the photo (e.g., a brightly lit tent tarp on the left), place the **Typography Block** in the **Upper-Right** quadrant. This creates diagonal visual equilibrium across the frame.

---

## 3. Color Theory & Contrast Engineering

### The 60-30-10 Photographic Color Harmony Rule
1. **60% Ambient Photo Tone**: The natural dominant color of the photograph (e.g., Deep Starry Navy `#091533`, Sunset Amber, or Forest Green).
2. **30% Primary Typography Color**: High-luminance neutral that contrasts cleanly against the background:
   - On dark/night photos: Warm Ivory (`#FFFAF0`), Alabaster (`#FFF8EB`), or Crisp White (`#FFFFFF`).
   - On bright/daylight skies: Deep Charcoal Navy (`#1A2438`) or Espresso (`#2C221E`), OR keep white text inside an anchored dark/frosted editorial card.
3. **10% Accent & Emotional Highlight Color**:
   - Sample a warm highlight already present in the photo (such as the warm yellow glow of a tent tarp `#FFE299` or champagne gold `#F0CA86`) and echo that exact hue in the **Subtitle**, **Fairy Light Bulbs**, **Stars**, or **Pill Badge**.
   - Use a complementary warm accent (`#FF7B93` Coral Pink) sparingly (`2–4` small elements like hearts) to draw the eye to the emotional focal point.

### Invisible Contrast Boosters (Guaranteed Readability)
Never rely on raw text over a busy photo alone. Always combine at least two of these three subtle contrast layers:
1. **Soft Atmospheric Radial Scrim**:
   ```css
   background: radial-gradient(ellipse 820px 520px at 69% 34%, rgba(8, 17, 42, 0.40) 0%, transparent 75%);
   ```
   Darkens the sky behind the text by ~15–20% with zero visible hard edges.
2. **Multi-Stage Text Shadow**:
   ```css
   text-shadow:
     0 3px 12px rgba(0, 0, 0, 0.90),
     0 0 24px rgba(255, 210, 135, 0.35);
   ```
   Combines a tight dark drop-shadow for crisp character edges with a wide warm ambient glow.
3. **Frosted Glass Pill / Dashed Container**:
   ```css
   background: rgba(12, 24, 52, 0.38);
   backdrop-filter: blur(3px);
   ```
   Softens background stars/foliage inside the quote box so small `21px–24px` Thai body text is effortless to read.

---

## 4. Thai Typography Rules & Spacing Discipline

Thai script has a 4-level vertical structure (Base consonants + Upper vowels `ั ิ ี ึ ื` + Tone marks `่ ้ ๊ ๋ ์` + Lower vowels `ุ ู`). To prevent clipping or crowding:

1. **Line Height (`line-height`)**:
   - Display Headlines (`72px–96px`): Use `line-height: 1.22` to `1.30` and `padding: 4px 24px` (especially when using `background-clip: text` gradients, so upper tone marks and lower vowels are never clipped by the bounding box!).
   - Body Copy (`20px–24px`): Use `line-height: 1.75` to `1.85` for comfortable reading.
2. **Preventing Orphan Word Wraps**:
   - Never allow automatic browser word-wrapping to push the last 1–2 words of a Thai sentence (e.g., *"ฉัน"*, *"วัน"*, *"นะ"*) onto a new line by itself.
   - Always use explicit `<br>` tags at natural clause breaks paired with `white-space: nowrap;` on the quote container.
3. **Ornament Clearance**:
   - Keep SVG stars, moons, and sparkle crosses at least `40px` away from the left/right edges of the Thai headline (`สุขสันต์วันเกิด...`) so decorative elements frame the text without touching the characters.
