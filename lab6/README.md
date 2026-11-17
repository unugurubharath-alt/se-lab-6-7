# Lab 6: Code and Branch Coverage Analysis

## About

This directory contains the implementation, test suites, coverage reports, and deliverables for **Lab 6: Code and Branch Coverage Analysis** for the **Customs Duty Calculator** (`customs_duty.py`).

## Deliverables Summary

| Deliverable | File | Status |
|-------------|------|--------|
| Statement Coverage Tests | [`CodeCoverageTest_customs_duty.py`](CodeCoverageTest_customs_duty.py) | **100%** Line Coverage (36/36 stmts) |
| Branch Coverage Tests | [`BranchCoverageTest_customs_duty.py`](BranchCoverageTest_customs_duty.py) | **100%** Branch Coverage (28/28 branches) |
| Consolidated Pytest Suite | [`test_customs_duty.py`](test_customs_duty.py) | 20 passing unit tests |
| Initial Coverage Screenshot | [`screenshots/initial_line_coverage.png`](screenshots/initial_line_coverage.png) | 36% baseline coverage |
| 100% Line Coverage Screenshot | [`screenshots/code_coverage_100.png`](screenshots/code_coverage_100.png) | 100% line coverage |
| 100% Branch Coverage Screenshot | [`screenshots/branch_coverage_100.png`](screenshots/branch_coverage_100.png) | 100% branch coverage |
| Coverage Analysis Report (PDF) | [`Lab6_Coverage_Analysis_Report.pdf`](Lab6_Coverage_Analysis_Report.pdf) | Complete PDF deliverable |

---

## Functions Under Test

1. **`duty_rate(category, origin)`**:
   - Raises `ValueError` for prohibited goods (`weapons`, `narcotics`).
   - Calculates preferential tariffs for `electronics` (FTA: 10%, non-FTA: 20%).
   - Calculates preferential tariffs for `clothing` (FTA: 5%, non-FTA: 12%).
   - Duty-free for `books` (0%).
   - Standard tariff for any other category (15%).

2. **`total_duty(category, value, origin, is_gift)`**:
   - Validates that declared value is non-negative (`value >= 0`).
   - Applies gift exemption threshold (duty-free up to 5,000; duty calculated on excess).
   - Applies commercial threshold (duty-free up to 1,000; full value taxed if exceeded).
   - Enforces statutory minimum duty: if `0 < duty < 50`, duty is set to 50.

3. **`clearance_channel(value, category, has_documents)`**:
   - Returns `"refuse"` for prohibited items.
   - Returns `"inspect"` if value > 100,000.
   - Returns `"inspect"` if value > 20,000 without accompanying documents.
   - Returns `"green"` (cleared) for all compliant shipments.

---

## How to Run Coverage Analysis

### 1. Statement (Line) Coverage
```bash
coverage run -m pytest CodeCoverageTest_customs_duty.py
coverage report -m
```

### 2. Branch (Decision) Coverage
```bash
coverage run --branch -m pytest BranchCoverageTest_customs_duty.py
coverage report -m
```

---

## Results Summary Table

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Line Coverage | $\ge 90\%$ | **100%** (36/36) | PASSED |
| Branch Coverage | $\ge 90\%$ | **100%** (28/28) | PASSED |
| Test Execution | All pass | **21 / 21 pass** | PASSED |
