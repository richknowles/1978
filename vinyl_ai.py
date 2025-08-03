#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vinyl_ai.py – Taste-based vinyl crate recommendations with smart model fallback
"""

import os
import json
import getpass
import sys
from openai import OpenAI, OpenAIError

TOP10_PATH = "data/top10_real.json"
OUTPUT_PATH = "data/vinyl_ai.md"
MODEL_FALLBACKS = ["gpt-4", "gpt-4o", "gpt-3.5-turbo"]

def load_top10(path=TOP10_PATH):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Could not find {path}. Run library_parser.py first.", file=sys.stderr)
        sys.exit(1)

def prompt_for_key():
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key.strip()
    print("🔐 OpenAI API key not found.")
    return getpass.getpass("Enter your OpenAI API key (input hidden): ").strip()

def query_model(client, model, albums):
    prompt = (
        "You are a vinyl crate-digger with impeccable taste.\n\n"
        "Based on this user's actual top 10 albums, recommend 5 albums they probably don’t own but would *love* on vinyl.\n\n"
        "Top 10 Albums:\n"
        + "\n".join(f"{a['rank']}. {a['album']} — {a['artist']}" for a in albums)
        + "\n\n### Crate-Digger Recommendations\n"
    )
    return client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a vinyl crate-digger with impeccable taste."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.9,
    )

def run_recommendation():
    albums = load_top10()
    api_key = prompt_for_key()
    client = OpenAI(api_key=api_key)

    for model in MODEL_FALLBACKS:
        try:
            print(f"🔁 Trying model: {model}")
            response = query_model(client, model, albums)
            used = model
            break
        except OpenAIError as e:
            msg = str(e).lower()
            if "model" in msg and ("invalid" in msg or "not found" in msg or "no access" in msg):
                print(f"⚠️ Model '{model}' unavailable — falling back.")
                continue
            if "insufficient_quota" in msg or e.status == 429 or e.code == 429:
                print("\n❌ Insufficient quota error! Check billing → add payment or enable Pay-as-You-Go.")
                sys.exit(2)
            raise  # Other errors — show full error

    else:
        print("⚠️ No usable OpenAI models were available. Exiting.")
        sys.exit(3)

    md = response.choices[0].message.content.strip()
    print(f"\n✅ Recommendations generated using {used}\n{md}\n")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✅ Saved Markdown → {OUTPUT_PATH}")

if __name__ == "__main__":
    run_recommendation()
