# File: utils/pack_loader.py

import os
import importlib.util

PACKS_DIR = "packs"

def load_pack(name):
    path = os.path.join(PACKS_DIR, f"{name.lower()}.py")
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "PACK", None)
