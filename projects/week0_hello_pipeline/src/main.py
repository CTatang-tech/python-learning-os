from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


# ---------- Config ----------
PROJECT_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_DIR / "input" / "immunization_sample.csv"
OUTPUT_DIR = PROJECT_DIR / "output"
CLEANED_PATH = OUTPUT_DIR / "immunization_cleaned.csv"
SUMMARY_PATH = OUTPUT_DIR / "summary.txt"


# ---------- Data model ----------
@dataclass
class Row:
    person_id: int
    age: int              # -1 means missing/unknown
    vaccinated: str       # "yes" | "no" | "unknown"


# ---------- Cleaning helpers ----------
def clean_age(raw: str) -> int:
    raw = (raw or "").strip()
    if raw == "":
        return -1
    try:
        return int(raw)
    except ValueError:
        return -1


def clean_vaccinated(raw: str) -> str:
    raw = (raw or "").strip().lower()
    if raw in {"yes", "no"}:
        return raw
    return "unknown"


# ---------- IO ----------
def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def transform(rows: list[dict]) -> list[Row]:
    cleaned: list[Row] = []
    for r in rows:
        # person_id should be valid; if not, crash loudly (Week 0 is allowed to be strict)
        person_id = int((r.get("person_id") or "").strip())

        age = clean_age(r.get("age", ""))
        vaccinated = clean_vaccinated(r.get("vaccinated", ""))

        cleaned.append(Row(person_id=person_id, age=age, vaccinated=vaccinated))
    return cleaned


def write_cleaned_csv(rows: list[Row], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["person_id", "age", "vaccinated"])
        for r in rows:
            writer.writerow([r.person_id, r.age, r.vaccinated])


# ---------- Summary / metrics ----------
def compute_summary(rows: list[Row]) -> str:
    total = len(rows)
    missing_age = sum(1 for r in rows if r.age == -1)

    yes = sum(1 for r in rows if r.vaccinated == "yes")
    no = sum(1 for r in rows if r.vaccinated == "no")
    unk = sum(1 for r in rows if r.vaccinated == "unknown")

    known = yes + no
    vaccinated_rate_known = (yes / known) if known > 0 else 0.0

    lines = [
        "Hello Pipeline — Summary",
        "------------------------",
        f"Total people: {total}",
        f"Missing age count: {missing_age}",
        f"Vaccination counts:",
        f"  yes: {yes}",
        f"  no: {no}",
        f"  unknown: {unk}",
        f"Vaccinated rate (known only): {vaccinated_rate_known:.2%}",
    ]
    return "\n".join(lines) + "\n"


def write_summary(text: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# ---------- “Tests” (tiny assertions) ----------
def run_sanity_checks(cleaned: list[Row]) -> None:
    # Required success criteria checks
    assert any(r.age == -1 for r in cleaned), "Expected at least one missing age mapped to -1"
    assert any(r.vaccinated == "unknown" for r in cleaned), "Expected at least one 'unknown' vaccination"
    # Basic invariants
    assert all(r.vaccinated in {"yes", "no", "unknown"} for r in cleaned), "Invalid vaccinated value found"


def main() -> None:
    raw = read_rows(INPUT_PATH)
    cleaned = transform(raw)

    run_sanity_checks(cleaned)

    write_cleaned_csv(cleaned, CLEANED_PATH)
    summary = compute_summary(cleaned)
    write_summary(summary, SUMMARY_PATH)

    print(summary)
    print(f"✅ Wrote cleaned CSV: {CLEANED_PATH}")
    print(f"✅ Wrote summary:     {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
