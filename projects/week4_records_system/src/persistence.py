
# src/persistence.py
# Persistence helpers (I/O only): save/load patient store as JSON.
# IMPORTANT: no validation logic here. Store is assumed clean.

from __future__ import annotations
from typing import Any, Dict, Tuple
import json
import os


def save_store_to_json(store: Dict[str, Dict[str, Any]], path: str) -> Tuple[bool, str]:
    """
    Save the store to a JSON file.
    Returns (ok, message).
    """
    try:
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(store, f, ensure_ascii=False, indent=2)

        return True, f"saved {len(store)} records to '{path}'"
    except OSError as e:
        return False, f"save failed: {e}"
    except TypeError as e:
        return False, f"save failed (non-serializable data): {e}"


def load_store_from_json(path: str) -> Tuple[bool, str, Dict[str, Dict[str, Any]]]:
    """
    Load store from a JSON file.
    Returns (ok, message, store).
    """
    if not os.path.exists(path):
        return False, f"load failed: file not found '{path}'", {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            return False, "load failed: JSON root must be an object/dict", {}

        # Minimal structural check (no deep validation)
        for pid, rec in data.items():
            if not isinstance(pid, str):
                return False, "load failed: patient_id keys must be strings", {}
            if not isinstance(rec, dict):
                return False, "load failed: each patient record must be a dict", {}

        return True, f"loaded {len(data)} records from '{path}'", data

    except json.JSONDecodeError as e:
        return False, f"load failed: invalid JSON ({e})", {}
    except OSError as e:
        return False, f"load failed: {e}", {}
