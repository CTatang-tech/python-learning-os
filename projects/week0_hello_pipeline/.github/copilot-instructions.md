# Copilot Instructions: week0_hello_pipeline

## Project Overview
A data cleaning pipeline that reads immunization records from CSV, normalizes messy data (missing ages, inconsistent vaccination responses), and outputs cleaned CSV + summary statistics. Week 0 learning project — intentionally simple, strict error handling (crashes loudly on invalid person_id).

## Architecture & Data Flow

**Input** → `input/immunization_sample.csv`
```
person_id (required) | age (optional, -1 if missing) | vaccinated (normalized to: yes/no/unknown)
```

**Processing** → `src/main.py` (3-stage pipeline):
1. **read_rows()** - Parse CSV as list of dicts; crashes if file missing
2. **transform()** - Apply cleaning rules via `clean_age()` and `clean_vaccinated()`
3. **write_cleaned_csv() + compute_summary()** - Output results

**Output** → Two files in `output/`:
- `immunization_cleaned.csv` - Normalized records
- `summary.txt` - Human-readable stats (vaccinated rate, missing age count)

## Key Conventions & Patterns

### Data Model
- **Person dataclass** (`Row`): person_id (int), age (int, -1 = missing), vaccinated (str literal: "yes"|"no"|"unknown")
- Missing/invalid data marked with sentinel values, not None (easier to serialize to CSV)

### Cleaning Rules
- **Age**: Strip whitespace; return -1 if empty string or non-numeric
- **Vaccinated**: Normalize to lowercase, accept "yes"/"no" exactly, default to "unknown" for anything else
- **person_id**: Required—crash loudly if missing or non-numeric (Week 0 philosophy: fail fast)

### Path Handling
- Use `pathlib.Path` relative to `PROJECT_DIR = Path(__file__).resolve().parents[1]`
- Example: `PROJECT_DIR / "input" / "immunization_sample.csv"`
- Create parent directories with `.mkdir(parents=True, exist_ok=True)`

### Encoding
- Always specify `encoding="utf-8"` on file I/O
- CSV I/O: use `csv.DictReader` / `csv.writer` (not pandas—keep it lightweight)

## Integration Points
- **notebook.ipynb** - Driver; orchestrates `src/main.py` (currently empty; will call main functions)
- No external dependencies beyond stdlib (csv, pathlib, dataclasses)

## Development Workflow
- Test the pipeline: Run main() from notebook or as script
- Modify cleaning rules in `clean_age()` / `clean_vaccinated()` 
- Check output files exist in `output/` and contain expected normalized data

## Common Tasks
- **Add a new field**: Add column to CSV input → add to Row dataclass → update cleaning logic → update CSV writer
- **Change cleaning rules**: Edit clean_age() or clean_vaccinated(); test against sample input
- **Debug data**: Add print statements in transform() to inspect raw vs cleaned values
