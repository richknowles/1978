<p align="center">
  <img src="1978_banner_ajricardo.png" alt="1978 Banner" style="width:100%;"/>
</p>

<h1 align="center">🎶 1978 – AI-Driven Vinyl Discovery Engine 🎶</h1>

> *"Born in the era of vinyl. Reborn with AI."*

**1978** is a Python-based toolkit that turns your Apple Music listening history into a personalized vinyl crate starter kit—with AI-recommended picks you probably don’t own yet.

The project is named `1978` in homage to the **peak era of vinyl record sales** and the dawn of personal audio obsession.

It’s smart. It's nostalgic. It's yours.

---

## 🧠 What It Does

This repo currently includes two key scripts:

1. 🚀 `library_parser.py`  
   Parses your exported `Library.xml` (from Apple Music or Music.app) and builds `top10_real.json` with your most-played albums.

2. 🤖 `vinyl_ai.py`  
   Prompts OpenAI to generate five “crate‑digger” albums that match your musical taste but go beyond your Top 10—styled as a printable Markdown vinyl flyer.

> **Coming soon**: Multi-model inference with Claude, Gemini, DeepSeek, and more.

---

## 🔧 Setup & Usage

### 1. Export your Apple Music Library XML  
Use Music.app on macOS:  
**File → Library → Export Library…**  
→ Save as `Library.xml`.

Or use an automated tool like [`mirko-leccese/Apple-Music-Library-Analysis`](https://github.com/mirko-leccese/Apple-Music-Library-Analysis).

---

### 2. Parse your library

```bash
python3 library_parser.py /path/to/Library.xml