import os
import torch
from funasr import AutoModel

class ASREngine:
    def __init__(self, asr_model_path: str, vad_model_path: str, vad_max_segment: int):
        self.device = self._get_device()
        self.asr_model_path = asr_model_path
        self.vad_model_path = vad_model_path
        self.vad_max_segment = vad_max_segment
        self.model = self._initialize_model()

    def _get_device(self) -> str:
        if torch.cuda.is_available():
            return "cuda:0"
        elif torch.backends.mps.is_available():
            return "mps"
        return "cpu"

    def _initialize_model(self):
        print(f"[System] Initializing ASR Engine on {self.device}...")
        return AutoModel(
            model=self.asr_model_path,
            trust_remote_code=True,
            vad_model=self.vad_model_path,
            vad_kwargs={"max_single_segment_time": self.vad_max_segment},
            device=self.device,
            disable_update=True
        )

    def transcribe(self, audio_path: str, lang: str, itn: bool, merge_vad: bool, merge_length_s: int) -> str:
        print(f"[System] Starting transcription for: {audio_path}")
        res = self.model.generate(
            input=[audio_path],
            cache={},
            batch_size=1,
            language=lang,
            itn=itn,
            merge_vad=merge_vad,
            merge_length_s=merge_length_s
        )

        if res and len(res) > 0:
            return res[0].get("text", "")
        return ""