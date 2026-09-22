import os
import sys
from config import CONFIG
from asr_engine import ASREngine
from text_formatter import TextFormatter

def main():
    # 1. Resolve input arguments using the centralized configuration
    input_arg = sys.argv[1] if len(sys.argv) > 1 else CONFIG.DEFAULT_AUDIO
    
    if not os.path.isabs(input_arg) and not input_arg.startswith(CONFIG.INPUT_DIR):
        audio_path = os.path.join(CONFIG.INPUT_DIR, input_arg)
    else:
        audio_path = input_arg

    # 2. Pre-run checks
    if not os.path.exists(audio_path):
        print(f"[Error] Audio file not found: {audio_path}")
        sys.exit(1)

    if not os.path.exists(CONFIG.ASR_MODEL_DIR) or not os.path.exists(CONFIG.VAD_MODEL_DIR):
        print("[Error] Models not found. Please run downloader.py first.")
        sys.exit(1)

    os.makedirs(CONFIG.OUTPUT_DIR, exist_ok=True)
    file_stem = os.path.splitext(os.path.basename(audio_path))[0]
    output_txt_path = os.path.join(CONFIG.OUTPUT_DIR, f"{file_stem}.txt")

    # 3. Execution pipeline
    try:
        engine = ASREngine(
            asr_model_path=CONFIG.ASR_MODEL_DIR,
            vad_model_path=CONFIG.VAD_MODEL_DIR,
            vad_max_segment=CONFIG.VAD_MAX_SEGMENT_TIME
        )
        
        raw_text = engine.transcribe(
            audio_path=audio_path,
            lang=CONFIG.LANGUAGE,
            itn=CONFIG.ITN,
            merge_vad=CONFIG.MERGE_VAD,
            merge_length_s=CONFIG.MERGE_LENGTH_S
        )
        
        if not raw_text:
            print("[Warning] Transcription returned empty text.")
            sys.exit(0)

        formatted_text = TextFormatter.format_sermon(raw_text)

        with open(output_txt_path, "w", encoding="utf-8") as f:
            f.write(formatted_text)
            
        print("\n=== Sermon Transcription Completed ===")
        print(f"[Success] Saved to: {output_txt_path}")

    except Exception as e:
        print(f"[Error] Transcription failed: {e}")

if __name__ == "__main__":
    main()