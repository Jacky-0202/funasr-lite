import os
from dataclasses import dataclass

@dataclass
class AppConfig:
    # Directory settings
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    ASR_MODEL_DIR: str = os.path.join(BASE_DIR, "FunAudioLLM", "Fun-ASR-Nano-2512")
    VAD_MODEL_DIR: str = os.path.join(BASE_DIR, "fsmn-vad")
    INPUT_DIR: str = os.path.join(BASE_DIR, "Inputs")
    OUTPUT_DIR: str = os.path.join(BASE_DIR, "Outputs")
    
    # Default execution settings
    DEFAULT_AUDIO: str = "sermon.mp3"
    
    # Transcription settings
    LANGUAGE: str = "中文"
    MERGE_VAD: bool = True
    MERGE_LENGTH_S: int = 30
    ITN: bool = True
    VAD_MAX_SEGMENT_TIME: int = 30000

CONFIG = AppConfig()