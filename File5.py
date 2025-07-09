import os
import random

def split_into_files(input_file, output_files):
    # Step 1: UID वाली फाइल से सभी लाइनें पढ़ो और डुप्लिकेट हटाओ
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = list(set(line.strip() for line in f if line.strip()))

    total = len(lines)
    print(f"\n📊 कुल UID मिले: {total}")

    # Step 2: शफल करें ताकि रैंडम बाँटे जाएँ
    random.shuffle(lines)

    # Step 3: बराबर 5 हिस्सों में बाँटे
    chunk_size = total // 5
    remainder = total % 5

    start = 0
    for i in range(5):
        end = start + chunk_size + (1 if i < remainder else 0)
        chunk = lines[start:end]

        with open(output_files[i], 'w', encoding='utf-8') as f:
            f.write('\n'.join(chunk))

        print(f"✅ output_{i+1}: {len(chunk)} UID लिखे गए → {output_files[i]}")
        start = end

    print("\n🎉 सभी UID 5 अलग-अलग फाइलों में बाँटे गए।")

def main():
    print("📥 स्टेप 1: UID लिस्ट वाली इनपुट फाइल का path डालें:")
    input_file = input("➡ इनपुट फाइल path: ").strip()

    if not os.path.isfile(input_file):
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
