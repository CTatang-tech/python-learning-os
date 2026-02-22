
# src/main.py
# Thin runner / demo entry point.
# All logic lives in store.py / queries.py / io.py

from persistence import save_store_to_json, load_store_from_json
import os

from store import add_patient, get_patient, update_patient, delete_patient, list_patients
from queries import summary_counts
import store


def main():
    store = {}

    ok, msg = add_patient(store, "001", " Alice Smith ",
                          30, True, ["Diabetes"])
    print(msg)

    ok, msg = add_patient(store, "002", "Bob Johnson",
                          45, False, ["Hypertension"])
    print(msg)

    print("\nGet patient 001:")
    print(get_patient(store, "001"))

    ok, msg = update_patient(store, "002", vaccinated="yes")
    print("\nUpdate patient 002 vaccinated -> yes:")
    print(msg)

    print("\nList patients:")
    print(list_patients(store))

    ok, msg = delete_patient(store, "001")
    print("\nDelete patient 001:")
    print(msg)

    print("\nList patients after delete:")
    print(list_patients(store))

    print("\nSummary:")
    print(summary_counts(store))


if __name__ == "__main__":
    main()

    # Save demo
    out_path = os.path.join("data", "output", "patients.json")
    ok, msg = save_store_to_json(store, out_path)
    print("\nPersist:", msg)

    # Load demo
    ok, msg, loaded = load_store_from_json(out_path)
    print("Reload:", msg)
    print("Reloaded keys:", list(loaded.keys()))
