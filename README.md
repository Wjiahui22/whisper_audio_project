# Whisper Audio Transcription with Keyword Extraction
This project uses OpenAI Whisper to transcribe .wav audio files and extract key information such as colors, brands/items, and durations using Regex and word2number.

A sample file stroller.wav is included for testing.

Requirements

Python 3.13 (or 3.11+)

ffmpeg
 installed on your system (used for audio processing)

Python packages:

pip3 install openai-whisper soundfile word2number

Setup

Clone the repository:

git clone https://github.com/YourUsername/whisper_audio_project.git
cd whisper_audio_project


Make sure ffmpeg is installed and accessible from your PATH:

ffmpeg -version


Place any .wav files you want to transcribe into the folder. A sample stroller.wav is already included.

Usage

Run the script with Python:

python3 test_whisper.py


The script will automatically process all .wav files in the folder and print:

Full transcription

Colors found

Brands/Items found

Durations found

Example Output
Transcription:
My stroller is pink, the brand is Gerber, and I have been using it for three years.

Colors found: ['pink']
Brands/Items found: ['Gerber']
Durations found: ['3 year']

Notes

Make sure each audio file is clear and not too noisy for better transcription accuracy.

Regex patterns are basic and can be expanded to capture other keywords.

Large audio files may take a few minutes to process.
