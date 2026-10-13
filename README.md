# FunASR Lite

Lightweight, offline speech-to-text pipeline using FunASR and Qwen.

## Project Structure

- `config.py`: Centralized configuration.
- `asr_engine.py`: ASR initialization and inference.
- `text_formatter.py`: Punctuation formatting and line breaks.
- `main.py`: CLI entry point.
- `downloader.py`: Model download script.

## Setup

### 1. System Dependencies
Install FFmpeg and GCC (required by Triton/PyTorch kernel compilation):

```bash
sudo apt update && sudo apt install -y ffmpeg build-essential
```
### 2. Environment & Python Packages

```bash
conda create -n funasr python=3.10 -y
conda activate funasr
pip install -r requirements.txt
```

### 3. Download Models

```bash
python downloader.py
```

### Usage

Place audio files in ./Inputs/.

```bash
# Transcribe default audio configured in config.py
python main.py

# Transcribe specific audio file
python main.py sample.mp3
```

