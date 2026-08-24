# FunASR Lite

This is a lightweight, modularized Speech-to-Text (ASR) project based on FunASR and Qwen models. It is designed for easy deployment and offline execution, specifically optimized for long audio files like sermons or speeches.

## Project Structure

- `config.py`: Centralized configuration for model paths and transcription parameters.
- `asr_engine.py`: Core ASR logic handling model initialization and inference.
- `text_formatter.py`: Text post-processing (e.g., punctuation-based line breaks).
- `main.py`: The entry point script to execute the transcription.
- `downloader.py`: Utility script to download required Hugging Face models.

## Prerequisites

It is highly recommended to use [Conda](https://docs.conda.io/en/latest/) to manage your Python environment.

### 1. Create a Conda Virtual Environment

Create and activate a new virtual environment named `funasr` with Python 3.10:

```bash
conda create -n funasr python=3.10 -y
conda activate funasr
```

### 2. Install Dependencies
Install the required Python packages:

```Bash
pip install -r requirements.txt
```
(Note: If you have an NVIDIA GPU, it is recommended to install the CUDA-specific version of PyTorch from the official PyTorch website before running the command above to ensure maximum performance.)

### 3. Download Models
Because the ASR and VAD models are large, they are not included in this repository. Run the downloader script to fetch the models automatically. This script supports resuming interrupted downloads.

```Bash
python downloader.py
```
After completion, the FunAudioLLM/ and fsmn-vad/ directories will be populated with the necessary model files.

### Usage
Place your target audio file (e.g., sermon.mp3) into the Inputs/ directory.

Run the main script.

If you want to transcribe the default sermon.mp3:

```Bash
python main.py
```
If you have a specifically named file (e.g., audio_test.mp3 inside Inputs/):

```Bash
python main.py audio_test.mp3
```
