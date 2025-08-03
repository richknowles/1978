# library_parser.py – Parse Apple Music iTunes Library XML and export Top 10
import plistlib
from collections import defaultdict
import os
import json

def parse_itunes_library(xml_path):
    if not os.path.exists(xml_path):
        raise FileNotFoundError(f"Library file not found: {xml_path}")

    with open(xml_path, 'rb') as f:
        plist = plistlib.load(f)

    tracks = plist.get("Tracks", {})
    album_plays = defaultdict(lambda: {"artist": "", "plays": 0})

    for track_id, track in tracks.items():
        album = track.get("Album")
        artist = track.get("Artist")
        plays = track.get("Play Count", 0)

        if album and artist:
            key = (album, artist)
            album_plays[key]["artist"] = artist
            album_plays[key]["plays"] += plays

    return album_plays

def get_top10_albums(xml_path):
    album_data = parse_itunes_library(xml_path)
    sorted_albums = sorted(album_data.items(), key=lambda x: x[1]["plays"], reverse=True)

    top10 = []
    for idx, ((album, artist), data) in enumerate(sorted_albums[:10], 1):
        top10.append({
            "rank": idx,
            "album": album,
            "artist": artist,
            "plays": data["plays"]
        })
    return top10

def save_as_json(data, out_path):
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Exported JSON → {out_path}")

def save_as_markdown(data, out_path):
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("# 🎧 Your Top 10 Albums by Play Count\n\n")
        for album in data:
            f.write(f"**{album['rank']}. {album['album']}** — *{album['artist']}*  \n")
            f.write(f"Plays: `{album['plays']}`\n\n")
    print(f"✅ Exported Markdown → {out_path}")

if __name__ == "__main__":
    path = "data/Library.xml"
    top_albums = get_top10_albums(path)

    print("\n🎧 Your Top 10 Albums by Play Count:\n")
    for album in top_albums:
        print(f"{album['rank']}. {album['album']} – {album['artist']} ({album['plays']} plays)")

    # Save to files
    save_as_json(top_albums, "data/top10_real.json")
    save_as_markdown(top_albums, "data/top10_real.md")
