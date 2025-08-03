# 1978 — Your Personal Top‑10 Vinyl Picks

**1978** is a Python-based toolkit that turns your Apple Music listening history into a personalized vinyl crate starter kit—with AI-recommended picks you probably don’t own yet.

This repo does two things:

1. 🚀 **`library_parser.py`**: Parses your exported `Library.xml` (from Apple Music or Music.app) and builds `top10_real.json` with your most-played albums.
2. 🤖 **`vinyl_ai.py`**: Prompts OpenAI to generate five “crate‑digger” albums that match your musical taste but go beyond your Top 10—styled as a Markdown vinyl flyer.

*The project is named `1978` in homage to the peak era of vinyl record sales.*

---

## 🔧 Setup & Usage

### 1. Export your Apple Music Library XML  
Use Music.app on macOS: **File → Library → Export Library…** to generate `Library.xml`.

Or use tools like `music-library-exporter` for automated XML export. ([mirko‑leccese/Apple‑Music‑Library‑Analysis][turn2view0])

### 2. Parse your library  
```bash
python3 library_parser.py /path/to/Library.xml
