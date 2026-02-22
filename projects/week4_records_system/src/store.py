
# src/store.py

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple


# ----------------------------
# Contract constants (single source of truth)
# ----------------------------
AGE_MIN = 0
AGE_MAX = 120

TRUE_WORDS = {"true", "t", "yes", "y", "1"}
FALSE_WORDS = {"false", "f", "no", "n", "0"}
UNKNOWN_WORDS = {"unknown", "unk", "na", "n/a", ""}


# ----------------------------
# Normalizers (normalize + validate)
# They raise ValueError when invalid.
# ----------------------------
def normalize_patient_id(patient_id: Any) -> str:
    if patient_id is None:
        raise ValueError("patient_id is required")

    pid = str(patient_id).strip()
    if pid == "":
        raise ValueError("patient_id cannot be empty")

    # Leading zeros are allowed, so no numeric conversion.
    return pid


def normalize_name(name: Any) -> str:
    if name is None:
        raise ValueError("name is required")

    cleaned = str(name).strip()
    if cleaned == "":
        raise ValueError("name cannot be empty")

    # Optional: collapse multiple spaces into one
    cleaned = " ".join(cleaned.split())
    return cleaned


def normalize_age(age: Any) -> Optional[int]:
    if age is None:
        return None

    # Accept blank strings as None
    if isinstance(age, str) and age.strip() == "":
        return None

    # Convert strings like "34" to int
    try:
        n = int(age)
    except (TypeError, ValueError):
        raise ValueError("age must be an integer or None")

    if n < AGE_MIN or n > AGE_MAX:
        raise ValueError(f"age must be between {AGE_MIN} and {AGE_MAX}")

    return n


def normalize_vaccinated(vaccinated: Any) -> Optional[bool]:
    if vaccinated is None:
        return None

    if isinstance(vaccinated, bool):
        return vaccinated

    # Accept strings (case-insensitive)
    if isinstance(vaccinated, str):
        v = vaccinated.strip().lower()
        if v in TRUE_WORDS:
            return True
        if v in FALSE_WORDS:
            return False
        if v in UNKNOWN_WORDS:
            return None
        raise ValueError(
            "vaccinated must be True/False/None (or yes/no/unknown)")

    # Accept numeric 1/0
    if isinstance(vaccinated, (int, float)):
        if vaccinated == 1:
            return True
        if vaccinated == 0:
            return False
        raise ValueError("vaccinated numeric values must be 1 or 0")

    raise ValueError("vaccinated must be bool or None (or a supported string)")


def normalize_conditions(conditions: Any) -> List[str]:
    if conditions is None:
        return []

    # If a single string, convert to one-item list
    if isinstance(conditions, str):
        item = conditions.strip()
        return [item] if item != "" else []

    # If iterable collection, normalize each to cleaned string
    if isinstance(conditions, (list, tuple, set)):
        cleaned: List[str] = []
        for c in conditions:
            if c is None:
                continue
            s = str(c).strip()
            if s != "":
                cleaned.append(s)
        return cleaned

    raise ValueError("conditions must be a list of strings, a string, or None")


# ----------------------------
# CRUD functions (no printing; return status)
# Return type: (ok, message)
# ----------------------------
def add_patient(
    store: Dict[str, Dict[str, Any]],
    patient_id: Any,
    name: Any,
    age: Any,
    vaccinated: Any,
    conditions: Any,
) -> Tuple[bool, str]:
    try:
        pid = normalize_patient_id(patient_id)
    except ValueError as e:
        return False, f"add failed: {e}"

    if pid in store:
        return False, f"add failed: patient_id '{pid}' already exists"

    try:
        record = {
            "name": normalize_name(name),
            "age": normalize_age(age),
            "vaccinated": normalize_vaccinated(vaccinated),
            "conditions": normalize_conditions(conditions),
        }
    except ValueError as e:
        return False, f"add failed: {e}"

    store[pid] = record
    return True, f"added patient '{pid}'"


def get_patient(store: Dict[str, Dict[str, Any]], patient_id: Any) -> Optional[Dict[str, Any]]:
    try:
        pid = normalize_patient_id(patient_id)
    except ValueError:
        return None
    return store.get(pid, None)


def update_patient(
    store: Dict[str, Dict[str, Any]],
    patient_id: Any,
    name: Any = None,
    age: Any = None,
    vaccinated: Any = None,
    conditions: Any = None,
) -> Tuple[bool, str]:
    try:
        pid = normalize_patient_id(patient_id)
    except ValueError as e:
        return False, f"update failed: {e}"

    if pid not in store:
        return False, f"update failed: patient_id '{pid}' does not exist"

    # Normalize first; apply only if all provided fields are valid.
    # This prevents partial updates.
    new_values: Dict[str, Any] = {}
    try:
        if name is not None:
            new_values["name"] = normalize_name(name)
        if age is not None:
            new_values["age"] = normalize_age(age)
        if vaccinated is not None:
            new_values["vaccinated"] = normalize_vaccinated(vaccinated)
        if conditions is not None:
            new_values["conditions"] = normalize_conditions(conditions)
    except ValueError as e:
        return False, f"update failed: {e}"

    store[pid].update(new_values)
    return True, f"updated patient '{pid}'"


def delete_patient(store: Dict[str, Dict[str, Any]], patient_id: Any) -> Tuple[bool, str]:
    try:
        pid = normalize_patient_id(patient_id)
    except ValueError as e:
        return False, f"delete failed: {e}"

    if pid not in store:
        return False, f"delete failed: patient_id '{pid}' does not exist"

    del store[pid]
    return True, f"deleted patient '{pid}'"


def list_patients(store: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    return list(store.values())
