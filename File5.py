#!/usr/bin/env python3 """split_uid_files.py

A small utility to read a list of UIDs from a text file, remove duplicates, and randomly distribute them across multiple output files. Prompts are kept in Hindi (Devanagari) as in the original script. """

import os import random from typing import List

def split_into_files(input_file: str, output_files: List[str]) -> None: """Read UID list, remove duplicates, randomly distribute into the provided output files.

Args:
    input_file: Path to the text file containing one UID per line.
    output_files: List of paths where the split UID files will be written.
"""
# Step 1 – Read all lines, strip blanks, remove duplicates (order‑preserving)
with open(input_file, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
lines = list(dict.fromkeys(lines))  # removes duplicates while preserving order

total = len(lines)
print(f"\n📊 कुल UID मिले: {total}")

# Step 2 – Shuffle so that distribution is random
random.shuffle(lines)

# Step 3 – Split into the requested number of parts
parts = len(output_files)
if parts == 0:
    print("❌ कोई आउटपुट फाइल नहीं दी गई।")
    return

chunk_size, remainder = divmod(total, parts)
start = 0
for i, out_path in enumerate(output_files):
    end = start + chunk_size + (1 if i < remainder else 0)
    chunk = lines[start:end]

    # Create parent directories if they don't exist
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(chunk))

    print(f"✅ output_{i + 1}: {len(chunk)} UID लिखे गए → {out_path}")
    start = end

print("\n🎉 सभी UID सफलतापूर्वक अलग‑अलग फाइलों में बाँट दिए गए।")

def main() -> None: """Command‑line interface that mirrors the original interactive behaviour."""

# Step 1 – Ask for input file
input_file = input("📥 स्टेप 1: UID लिस्ट वाली इनपुट फाइल का path डालें:\n➡ ").strip()
if not os.path.isfile(input_file):
    print("❌ फाइल नहीं मिली! कृपया सही path दें।")
    return

# Step 2 – Ask for number of parts
while True:
    try:
        num_parts = int(input("\n🔢 कितने हिस्सों में बाँटना है? ").strip())
        if num_parts <= 0:
            raise ValueError
        break
    except ValueError:
        print("❌ कृपया 1 या उससे अधिक का वैध integer दें।")

# Step 3 – Collect output file paths
print("\n📁 स्टेप 2: अब आउटपुट फाइलों के path एक‑एक करके डालें:")
output_files = []
for i in range(num_parts):
    path = input(f"➡ आउटपुट फाइल {i + 1} का path: ").strip()
    output_files.append(path)

# Start processing
print("\n🔄 बाँटना शुरू किया जा रहा है...")
split_into_files(input_file, output_files)

if name == "main": main()

