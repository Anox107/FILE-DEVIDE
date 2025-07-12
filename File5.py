import os import random

def split_into_files(input_file, output_files): """Read UID list, remove duplicates, randomly distribute into the provided output files."""

# Step 1: Read all lines, strip blanks, remove duplicates
with open(input_file, "r", encoding="utf-8") as f:
    lines = list({line.strip() for line in f if line.strip()})

total = len(lines)
print(f"\n📊 कुल UID मिले: {total}")

# Step 2: Shuffle so that distribution is random
random.shuffle(lines)

# Step 3: Split into the requested number of parts
parts = len(output_files)
chunk_size = total // parts
remainder = total % parts

start = 0
for i in range(parts):
    end = start + chunk_size + (1 if i < remainder else 0)
    chunk = lines[start:end]

    with open(output_files[i], "w", encoding="utf-8") as f:
        f.write("\n".join(chunk))

    print(
        f"✅ output_{i + 1}: {len(chunk)} UID लिखे गए → {output_files[i]}"
    )
    start = end

print("\n🎉 सभी UID अलग-अलग फाइलों में बाँट दिए गए।")

def main(): print("📥 स्टेप 1: UID लिस्ट वाली इनपुट फाइल का path डालें:") input_file = input("➡ इनपुट फाइल path: ").strip()

if not os.path.isfile(input_file):
    print("❌ फाइल नहीं मिली! कृपया सही path दें।")
    return

# Ask user how many parts to create
while True:
    try:
        num_parts = int(input("\n🔢 कितने हिस्सों में बाँटना है? ").strip())
        if num_parts <= 0:
            raise ValueError
        break
    except ValueError:
        print("❌ कृपया 1 या उससे अधिक का वैध integer दें।")

print("\n📁 स्टेप 2: अब आउटपुट फाइलों के path एक-एक करके डालें:")

output_files = []
for i in range(num_parts):
    path = input(f"➡ आउटपुट फाइल {i + 1} का path: ").strip()
    output_files.append(path)

# Start processing
print("\n🔄 बाँटना शुरू किया जा रहा है...")
split_into_files(input_file, output_files)

if name == "main": main()

        print("❌ फाइल नहीं मिली! कृपया सही path दें।")
        return

    print("\n📁 स्टेप 2: अब 5 आउटपुट फाइलों के path एक-एक करके डालें:")

    output_files = []
    for i in range(5):
        path = input(f"➡ आउटपुट फाइल {i+1} का path: ").strip()
        output_files.append(path)

    # प्रोसेस शुरू
    print("\n🔄 बाँटना शुरू किया जा रहा है...")
    split_into_files(input_file, output_files)

if __name__ == "__main__":
    main()
