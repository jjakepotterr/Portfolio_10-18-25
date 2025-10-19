
# Pip‑Boy Style Portfolio (Flask)

A single‑file Flask app that renders a Fallout‑inspired Pip‑Boy UI for a personal portfolio.
Tabs: **Stats**, **LinkedIn**, **Projects**, **GitHub**, **Contact**.

## Quick start

```bash
cd pipboy_portfolio
python3 -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install flask requests
python app.py
```

Visit http://127.0.0.1:5000/

## Customizing links
- Edit `app.py` in the `index()` route `links` dict **or**
- Edit `templates/index.html` where the iframes are and replace `src="{{ links.linkedin }}"` etc.
- If a site refuses to load in an iframe, you may try the optional `/proxy` route:
  - Open `app.py`, set `ENABLE_PROXY=True`.
  - Change iframe `src` to `/proxy?url=YOUR_URL`.
  - **Note:** Many sites use CSP/X‑Frame‑Options to block proxying; respect their TOS and only proxy content you own or have permission to display.

## Theme enforcement
Iframe content is tinted with a CRT green filter to keep the overall Pip‑Boy style while maintaining legibility.

## Stats screen
- The stats (S.P.E.C.I.A.L.) labels can be renamed directly in `templates/index.html` (look for `<!-- Change title here if desired -->`).
- You can adjust the bar values via the inline CSS custom property `--val` and the number at the right.
- The included image `static/img/vaultboy.avif` originates from your provided file path. Replace with your own artwork if needed.

## Controls
- Tabs: Left/Right arrow keys
- Activate: Enter (or click)
- Knobs: Adjust brightness, glow, and scanline intensity

## Notes
- The "exact" in‑game character style is approximated via the provided image and green filter; avoid distributing proprietary assets without rights.
- Many third‑party sites will not allow being framed. Consider creating your own project/contact pages for guaranteed embedding.
