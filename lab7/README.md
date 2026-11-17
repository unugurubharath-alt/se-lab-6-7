# Lab 7: Fuzzing for Input Validation Bugs

## About

This directory contains the implementation, property-based fuzz tests, hardened code, and deliverables for **Lab 7: Fuzzing for Input Validation Bugs** using the **Hypothesis** fuzzing library.

## Deliverables Summary

| Deliverable | File | Description |
|-------------|------|-------------|
| Hardened Application Script | [`customs_duty.py`](customs_duty.py) | Defensively programmed customs declaration processor |
| Hypothesis Fuzz Test Suite | [`test_customs_duty.py`](test_customs_duty.py) | Property-based tests verifying "no-crash" invariants |
| Step 2 Terminal Screenshot | [`screenshots/step2_buggy_output.png`](screenshots/step2_buggy_output.png) | Normal execution of starter application |
| Step 4 Terminal Screenshot | [`screenshots/step4_fuzz_failing.png`](screenshots/step4_fuzz_failing.png) | Falsifying examples and crashes found by Hypothesis |
| Step 5 Terminal Screenshot | [`screenshots/step5_fixed_output.png`](screenshots/step5_fixed_output.png) | Execution of hardened application |
| Step 6 Terminal Screenshot | [`screenshots/step6_fuzz_passing.png`](screenshots/step6_fuzz_passing.png) | All Hypothesis fuzz tests passing cleanly |
| Fuzz Testing Report (PDF) | [`Lab7_Fuzz_Testing_Report.pdf`](Lab7_Fuzz_Testing_Report.pdf) | Complete PDF document deliverable |

---

## Step-by-Step Execution Guide

### Step 1: Install Dependencies
```bash
pip install hypothesis pytest
```

### Step 2: Run Buggy Starter Application
```bash
python customs_duty.py
```

### Step 3 & 4: Execute Hypothesis Fuzz Testing (Exposing Crashes)
```bash
pytest test_customs_duty.py
```
**Bugs Discovered:**
- `s=None` -> `AttributeError: 'NoneType' object has no attribute 'split'`
- `s=''` -> `ValueError: not enough values to unpack`
- `s=':'` or `s='@'` -> `ValueError: could not convert string to float`
- `s=''` in `hs_chapter` -> `ValueError: invalid literal for int() with base 10: ''`

### Step 5: Harden Application Code
The application script `customs_duty.py` was hardened with defensive programming:
- Validated types (`isinstance(text, str)`)
- Checked delimiter presence (`len(parts) == 2`)
- Wrapped conversions in `try-except` for `ValueError`, `TypeError`, `OverflowError`
- Rejected negative numbers, `NaN`, and `Infinity`
- Validated HS code digits and bounds (01 to 99)

Run the fixed processor:
```bash
python customs_duty.py
```

### Step 6: Re-Run Hypothesis Fuzz Tests
```bash
pytest test_customs_duty.py
```
**Result:** 3 passed (100% of generated test cases pass with 0 crashes).
