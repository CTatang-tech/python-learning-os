
# src/queries.py
# Read-only query helpers for the patient store.
# IMPORTANT: queries must NOT mutate the store.

from __future__ import annotations
from typing import Any, Dict, List, Optional
from collections import Counter


def find_by_vaccinated(
    store: Dict[str, Dict[str, Any]],
    status: Optional[bool],
) -> List[Dict[str, Any]]:
    """
    Return all patient records where vaccinated == status
    status can be True, False, or None (unknown).
    """
    results: List[Dict[str, Any]] = []
    for rec in store.values():
        if rec.get("vaccinated") == status:
            results.append(rec)
    return results


def find_by_condition(
    store: Dict[str, Dict[str, Any]],
    condition_name: str,
) -> List[Dict[str, Any]]:
    """
    Return all patient records containing a given condition (case-insensitive match).
    """
    target = condition_name.strip().lower()
    if target == "":
        return []

    results: List[Dict[str, Any]] = []
    for rec in store.values():
        conds = rec.get("conditions", [])
        for c in conds:
            if str(c).strip().lower() == target:
                results.append(rec)
                break
    return results


def patients_over_age(
    store: Dict[str, Dict[str, Any]],
    min_age: int,
) -> List[Dict[str, Any]]:
    """
    Return all patients with age >= min_age. Patients with age None are skipped.
    """
    results: List[Dict[str, Any]] = []
    for rec in store.values():
        age = rec.get("age")
        if isinstance(age, int) and age >= min_age:
            results.append(rec)
    return results


def summary_counts(store: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Return summary stats:
    - total patients
    - vaccinated_true / vaccinated_false / vaccinated_unknown
    - vaccinated_rate_known (True / (True+False)) as float or None if no known statuses
    - top_conditions: list of (condition, count) sorted descending
    """
    total = len(store)

    v_true = 0
    v_false = 0
    v_unknown = 0

    cond_counter: Counter[str] = Counter()

    for rec in store.values():
        v = rec.get("vaccinated")
        if v is True:
            v_true += 1
        elif v is False:
            v_false += 1
        else:
            v_unknown += 1

        for c in rec.get("conditions", []):
            cc = str(c).strip()
            if cc:
                cond_counter[cc] += 1

    known = v_true + v_false
    vaccinated_rate_known = (v_true / known) if known > 0 else None

    return {
        "total": total,
        "vaccinated_true": v_true,
        "vaccinated_false": v_false,
        "vaccinated_unknown": v_unknown,
        "vaccinated_rate_known": vaccinated_rate_known,
        "top_conditions": cond_counter.most_common(10),
    }
