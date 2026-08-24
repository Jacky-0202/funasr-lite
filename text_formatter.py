class TextFormatter:
    @staticmethod
    def format_sermon(raw_text: str) -> str:
        if not raw_text:
            return ""
        
        # Add newlines after sentence endings
        formatted = raw_text.replace("。", "。\n").replace("？", "？\n").replace("！", "！\n")
        
        # Clean up empty lines
        lines = [line.strip() for line in formatted.split("\n") if line.strip()]
        return "\n".join(lines)