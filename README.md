project_name: Whisper Audio Transcription & Keyword Extraction
description: >
  This project uses OpenAI Whisper to transcribe .wav audio files and extract key
  information such as colors, brands/items, and durations using Regex and word2number.
  A sample audio file (stroller.wav) is included for testing.

project_structure:
  - whisper_audio/
      - test_whisper.py: "Main script to transcribe WAV files and extract keywords"
      - stroller.wav: "Sample audio file"
      - README.yaml: "This file"
      - additional_wav_files: "Any other WAV files you want to transcribe"

notes_on_structure:
  - "Place any additional .wav files in this folder; the script will process them automatically."
  - "The script handles multiple WAV files without renaming them."

requirements:
  python: "3.13 or 3.11+"
  ffmpeg: "Installed on your system for audio processing"
  python_packages:
    - openai-whisper
    - soundfile
    - word2number

install_ffmpeg_mac:
  command: "brew install ffmpeg"
  check_installation: "ffmpeg -version"

running_script:
  steps:
    - "Open a terminal and navigate to the project folder: cd /path/to/whisper_audio"
    - "Run the transcription script: python3 test_whisper.py"
  output:
    description: >
      The script will:
        - Transcribe each .wav file in the folder
        - Extract colors, brands/items, and durations
        - Print results to the terminal

example_output:
  file: stroller.wav
  transcription: >
    My stroller is pink, the brand is Gerber, and I have been using it for three years.
  extracted_keywords:
    colors: ['pink']
    brands_items: ['Gerber']
    durations: ['3 year']

notes_and_tips:
  - "Ensure audio files are reasonably clear for better transcription accuracy."
  - "Regex patterns can be extended to capture additional keywords like materials or sizes."
  - "Large audio files may take longer to process depending on your CPU."
  - "WAV files do not need to be renamed; the script handles any .wav file in the folder."

dependencies_summary:
  openai-whisper: "Speech-to-text transcription"
  soundfile: "Audio file reading"
  word2number: "Convert numbers in words to digits"
  ffmpeg: "Audio processing (required by Whisper)"
