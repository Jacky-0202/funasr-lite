import os
from huggingface_hub import snapshot_download

def download_models():
    # Define repository IDs and their corresponding local target directories
    models_to_download = {
        "FunAudioLLM/Fun-ASR-Nano-2512": "./FunAudioLLM/Fun-ASR-Nano-2512",
        "funasr/fsmn-vad": "./fsmn-vad"
    }

    print("=== Starting Model Download and Environment Setup ===")
    
    for repo_id, local_dir in models_to_download.items():
        # 1. Create target directory if it does not exist
        os.makedirs(local_dir, exist_ok=True)
        print(f"\n[System] Verified directory exists: {local_dir}")
        print(f"[System] Preparing to download model: {repo_id} ...")
        
        # 2. Execute download
        try:
            snapshot_download(
                repo_id=repo_id,
                local_dir=local_dir,
                local_dir_use_symlinks=False,  # Ensure real files are downloaded instead of symlinks
                resume_download=True           # Enable resuming interrupted downloads
            )
            print(f"[Success] Successfully downloaded {repo_id}!")
        except Exception as e:
            print(f"[Error] Failed to download {repo_id}. Error: {e}")

    # 3. Create Inputs and Outputs directories for the main application
    for extra_dir in ["./Inputs", "./Outputs"]:
        os.makedirs(extra_dir, exist_ok=True)
        print(f"[System] Verified working directory exists: {extra_dir}")

    print("\n=== Environment Setup Completed ===")

if __name__ == "__main__":
    download_models()