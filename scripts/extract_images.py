#!/usr/bin/env python3
"""
Extrahiert Base64-kodierte Bilder aus .fodt-Dateien und speichert sie als Dateien.
"""

import re
import base64
import os
import sys
from pathlib import Path
import hashlib

def get_image_extension(data_bytes):
    """Ermittelt die Dateiendung anhand der Magic Bytes."""
    if data_bytes[:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    elif data_bytes[:2] == b'\xff\xd8':
        return 'jpg'
    elif data_bytes[:4] == b'GIF8':
        return 'gif'
    elif data_bytes[:4] == b'RIFF' and data_bytes[8:12] == b'WEBP':
        return 'webp'
    elif data_bytes[:2] in (b'BM', b'BA'):
        return 'bmp'
    else:
        return 'bin'

def extract_images_from_fodt(fodt_path, output_dir):
    """Extrahiert alle Bilder aus einer .fodt-Datei."""

    fodt_path = Path(fodt_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Lese {fodt_path}...")
    with open(fodt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Finde alle office:binary-data Elemente
    pattern = r'<office:binary-data>([^<]+)</office:binary-data>'
    matches = re.findall(pattern, content)

    print(f"Gefunden: {len(matches)} eingebettete Bilder")

    # Prefix für Dateinamen basierend auf Quelldatei
    prefix = fodt_path.stem.replace('.', '-').replace(' ', '-')

    extracted = []
    seen_hashes = {}

    for i, b64_data in enumerate(matches, 1):
        # Entferne Whitespace
        b64_clean = re.sub(r'\s+', '', b64_data)

        try:
            image_data = base64.b64decode(b64_clean)
        except Exception as e:
            print(f"  Warnung: Konnte Bild {i} nicht dekodieren: {e}")
            continue

        # Ermittle Dateiformat
        ext = get_image_extension(image_data)

        # Generiere Dateinamen
        filename = f"{prefix}-{i:03d}.{ext}"
        filepath = output_dir / filename

        # Prüfe auf Duplikate
        img_hash = hashlib.md5(image_data).hexdigest()[:12]
        if img_hash in seen_hashes:
            # Erstelle Symlink zum Original
            original = seen_hashes[img_hash]
            if not filepath.exists():
                filepath.symlink_to(original)
            print(f"  Bild {i}: Symlink zu {original}")
            extracted.append(filename)
            continue

        # Speichere Bild
        with open(filepath, 'wb') as f:
            f.write(image_data)

        seen_hashes[img_hash] = filename
        extracted.append(filename)
        print(f"  Bild {i}: {filename} ({len(image_data):,} Bytes)")

    return extracted

def main():
    src_dir = Path(__file__).parent.parent / 'src'
    output_dir = Path(__file__).parent.parent / 'docs' / 'images'

    fodt_files = list(src_dir.glob('*.fodt'))

    if not fodt_files:
        print("Keine .fodt-Dateien gefunden!")
        sys.exit(1)

    print(f"Verarbeite {len(fodt_files)} .fodt-Dateien...")
    print(f"Ausgabeverzeichnis: {output_dir}")
    print()

    total_images = []

    for fodt_file in fodt_files:
        print(f"\n{'='*60}")
        images = extract_images_from_fodt(fodt_file, output_dir)
        total_images.extend(images)

    print(f"\n{'='*60}")
    print(f"Fertig! {len(total_images)} Bilder extrahiert nach {output_dir}")

if __name__ == '__main__':
    main()
