from .node import LoadDart, DartPrompt, DartConfig, DartGenerate, BanTags
from ... import NODE_SURFIX, SYMBOL

NODE_CLASS_MAPPINGS = {
    f"LoadDart{NODE_SURFIX}": LoadDart,
    f"DartPrompt{NODE_SURFIX}": DartPrompt,
    f"DartConfig{NODE_SURFIX}": DartConfig,
    f"DartGenerate{NODE_SURFIX}": DartGenerate,
    f"BanTags{NODE_SURFIX}": BanTags
}

NODE_DISPLAY_NAME_MAPPINGS = {
    f"LoadDart{NODE_SURFIX}": f"Load Dart {SYMBOL}",
    f"DartPrompt{NODE_SURFIX}": f"Dart Prompt {SYMBOL}",
    f"DartConfig{NODE_SURFIX}": f"Dart Config {SYMBOL}",
    f"DartGenerate{NODE_SURFIX}": f"Dart Generate {SYMBOL}",
    f"BanTags{NODE_SURFIX}": f"Ban Tags {SYMBOL}"
}


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]