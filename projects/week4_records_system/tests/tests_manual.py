
# tests/tests_manual.py
# Manual micro-tests for week4_records_system
# Ritual: PREDICT -> RUN -> EXPLAIN -> FIX -> RE-RUN


import os
import sys

# Allow importing from ../src
HERE = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, ".."))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


from store import add_patient, get_patient, update_patient, delete_patient, list_patients  # noqa: E402


def banner(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def show_store(store):
    print("STORE NOW:")
    for pid, rec in store.items():
        print(f"  {pid} -> {rec}")


def run_tests():
    banner("SETUP")
    store = {}

    # Seed initial patient
    ok, msg = add_patient(store, "001", " Alice Smith ",
                          30, True, ["Diabetes"])
    print("seed add:", ok, msg)
    assert ok is True

    # ------------------------------------------------------------
    banner("TEST 1 — Duplicate ID")
    print("# PREDICT: add_patient with same ID should fail (ok=False). Store unchanged.")
    ok, msg = add_patient(store, "001", "Another Name",
                          40, False, ["Hypertension"])
    print("# ACTUAL:", ok, msg)
    assert ok is False
    assert get_patient(store, "001")["name"] == "Alice Smith"

    # ------------------------------------------------------------
    banner("TEST 2 — Update missing patient")
    print("# PREDICT: update_patient on missing ID should fail (ok=False).")
    ok, msg = update_patient(store, "999", vaccinated="yes")
    print("# ACTUAL:", ok, msg)
    assert ok is False

    # ------------------------------------------------------------
    banner("TEST 3 — Blank/missing age")
    print("# PREDICT: age passed as blank string should become None (valid).")
    ok, msg = add_patient(store, "002", "Bob Johnson", "   ", "no", [])
    print("# ACTUAL:", ok, msg)
    assert ok is True
    bob = get_patient(store, "002")
    assert bob["age"] is None
    assert bob["vaccinated"] is False

    # ------------------------------------------------------------
    banner('TEST 4 — vaccinated "unknown"')
    print('# PREDICT: vaccinated="unknown" should normalize to None (unknown).')
    ok, msg = add_patient(store, "003", "Cara Doe", 22, "unknown", ["Asthma"])
    print("# ACTUAL:", ok, msg)
    assert ok is True
    cara = get_patient(store, "003")
    assert cara["vaccinated"] is None

    # ------------------------------------------------------------
    banner("TEST 5 — conditions passed as string")
    print('# PREDICT: conditions="Diabetes" should become ["Diabetes"].')
    ok, msg = add_patient(store, "004", "Dan Lee", 50, "yes", "Diabetes")
    print("# ACTUAL:", ok, msg)
    assert ok is True
    dan = get_patient(store, "004")
    assert dan["conditions"] == ["Diabetes"]

    # ------------------------------------------------------------
    banner("TEST 6 — delete twice")
    print("# PREDICT: first delete ok=True, second delete ok=False.")
    ok, msg = delete_patient(store, "004")
    print("delete #1:", ok, msg)
    assert ok is True

    ok, msg = delete_patient(store, "004")
    print("delete #2:", ok, msg)
    assert ok is False

    # ------------------------------------------------------------
    banner("EXTRA CHECK — store cleanliness")
    print("# PREDICT: all stored records follow the contract types.")
    for pid, rec in store.items():
        assert isinstance(pid, str) and pid.strip() != ""
        assert isinstance(rec["name"], str) and rec["name"].strip() != ""
        assert (rec["age"] is None) or (isinstance(
            rec["age"], int) and 0 <= rec["age"] <= 120)
        assert (rec["vaccinated"] is None) or (
            isinstance(rec["vaccinated"], bool))
        assert isinstance(rec["conditions"], list)
        for c in rec["conditions"]:
            assert isinstance(c, str) and c.strip() != ""

    print("\n✅ ALL MANUAL TESTS PASSED.")
    show_store(store)

    # ------------------------------------------------------------
    banner("QUERY TESTS — queries.py")
    from queries import find_by_vaccinated, find_by_condition, patients_over_age, summary_counts  # noqa: E402

    print("# PREDICT: vaccinated True list should include only records where vaccinated == True.")
    v_true = find_by_vaccinated(store, True)
    print("# ACTUAL count:", len(v_true))
    for r in v_true:
        assert r["vaccinated"] is True

    print('# PREDICT: condition "Diabetes" should return Alice (and any others with Diabetes).')
    diabetes = find_by_condition(store, "Diabetes")
    print("# ACTUAL names:", [r["name"] for r in diabetes])
    for r in diabetes:
        assert "Diabetes" in r["conditions"]

    print("# PREDICT: patients_over_age(store, 30) returns ages >= 30, skipping None.")
    over_30 = patients_over_age(store, 30)
    print("# ACTUAL ages:", [r["age"] for r in over_30])
    for r in over_30:
        assert isinstance(r["age"], int) and r["age"] >= 30

    print("# PREDICT: summary_counts returns totals + vaccinated breakdown + top conditions.")
    s = summary_counts(store)
    print("# ACTUAL summary:", s)
    assert s["total"] == len(store)
    assert s["vaccinated_true"] + s["vaccinated_false"] + \
        s["vaccinated_unknown"] == len(store)
    assert "top_conditions" in s

    # ------------------------------------------------------------
    banner("PERSISTENCE TESTS — io.py (save/load JSON)")
    from persistence import save_store_to_json, load_store_from_json

    out_path = os.path.join(PROJECT_ROOT, "data",
                            "output", "patients_test.json")

    print("# PREDICT: save succeeds, then load returns identical keys and record count.")
    ok, msg = save_store_to_json(store, out_path)
    print("save:", ok, msg)
    assert ok is True

    ok, msg, loaded = load_store_from_json(out_path)
    print("load:", ok, msg)
    assert ok is True

    assert isinstance(loaded, dict)
    assert set(loaded.keys()) == set(store.keys())
    assert len(loaded) == len(store)

    # Spot-check one record content (structure)
    some_id = next(iter(store.keys()))
    assert loaded[some_id]["name"] == store[some_id]["name"]


if __name__ == "__main__":
    run_tests()
