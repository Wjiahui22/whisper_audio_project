import os
import re
import csv
import certifi
import whisper
from word2number import w2n

# Ensure SSL works on Mac
os.environ['SSL_CERT_FILE'] = certifi.where()

# Load Whisper model
model = whisper.load_model("small")

# Folder containing WAV files (current folder)
AUDIO_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Regex patterns
color_pattern = re.compile(r'(?:color|it is|my [\w\s]+ is)\s+([a-zA-Z]+)', re.IGNORECASE)
brand_pattern = re.compile(
    r'(?:the brand is|from)\s+([a-zA-Z0-9]+)', re.IGNORECASE
)

duration_pattern = re.compile(
    r'(\d+|one|two|three|four|five|six|seven|eight|nine|ten)\s*(year|month|week|day)s?', 
    re.IGNORECASE
)

# CSV output
csv_file = os.path.join(AUDIO_FOLDER, "audio_info.csv")
with open(csv_file, "w", newline="") as csvfile:
    fieldnames = ["filename", "transcription", "colors", "brands", "durations"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Process all WAV files in folder
    for filename in os.listdir(AUDIO_FOLDER):
        if filename.lower().endswith(".wav"):
            filepath = os.path.join(AUDIO_FOLDER, filename)
            print(f"Transcribing {filename} ...")
            result = model.transcribe(filepath)
            text = result["text"]
            print(f"Transcription:\n{text}\n")

            # Extract colors
            found_colors = color_pattern.findall(text)

            # Extract brands/items
            found_brands = brand_pattern.findall(text)

            # Extract durations (handle number words)
            found_durations = []
            for match in duration_pattern.findall(text.lower()):
                num_str, unit = match
                try:
                    num = w2n.word_to_num(num_str)  # "three" -> 3
                except ValueError:
                    num = int(num_str)  # fallback for digits
                found_durations.append(f"{num} {unit}")

            # Write row to CSV
            writer.writerow({
                "filename": filename,
                "transcription": text,
                "colors": ", ".join(found_colors),
                "brands": ", ".join(found_brands),
                "durations": ", ".join(found_durations)
            })

            print("Colors found:", found_colors)
            print("Brands/Items found:", found_brands)
            print("Durations found:", found_durations)
            print("-" * 50)

print(f"All results saved to {csv_file}")
