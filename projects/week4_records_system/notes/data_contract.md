
**patient_id:** string, must be unique, allow leading zeros (e.g. "001")

**name:** string, trimmed, not empty

**age:** int or None, valid range 0–120

**vaccinated:** bool or None (None means unknown)

**conditions:** list of strings (can be empty). If string is passed, convert to one-item list.