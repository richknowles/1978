<p align="center">
  <img src="1978_banner_ajricardo.png" alt="1978 Banner" width="100%">
</p>

<p align="center">
  <img src="ajricardo_aj.png" alt="AJ Cartoon" width="180">
</p>

<p align="center">
  <img src="ajricardo_logo.png" alt="AJ Ricardo Logo" width="200">
</p>

# 1978 — Your Personal Top‑10 Vinyl Picks 🎶💿

**1978** is a Python-based toolkit that transforms your Apple Music listening history into a personalized vinyl crate—with smart AI‑powered album suggestions you probably don’t own yet.

🚀 **It uses OpenAI's GPT model**, with other AI models coming soon.  
📦 Fully local. Just run it and go crate-digging.

---

## 🔧 Setup & Usage

### 1. Export Your Apple Music Library
Open Music.app → **File → Library → Export Library…**  
Save the XML as `Library.xml`.

Or automate it with tools like [`music-library-exporter`](https://github.com/mirko-leccese/Apple-Music-Library-Analysis)

### 2. Parse Your Real Top 10
```bash
python3 library_parser.py /path/to/Library.xml
```

This creates `top10_real.json`.

### 3. Get Smart AI Album Recommendations
```bash
python3 vinyl_ai.py
```

🔐 First run asks for your OpenAI API key (no `.env` needed).  
Generates a vinyl flyer: `vinyl_recs.md`

---

## 📂 Files

- `library_parser.py` — parses your most-played albums
- `vinyl_ai.py` — AI crate-digger recommendations
- `vinyl_recs.md` — output flyer
- `top10_real.json` — saved top albums

---

## 💾 Coming Soon

- 🔄 GPT-4o and Claude 3 support
- 🖨️ Printable 'Dad to Son Vinyl Starter Kit'
- 🧠 Music memory inference
- 🎛️ Web app version with retro crate UI
- 🪞 Personalized crate mirror for friends & family

---

> 🕺 **The project is named *1978* in homage to the golden era of vinyl.**  
> Think: warm hiss, gatefold sleeves, and stories passed down on wax.

---
© AJ Ricardo — built with love 🩷