# Software Engineering Lab 6 & 7: Customs Duty Calculator

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/tested%20with-pytest-blue.svg)](https://pytest.org/)
[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://coverage.readthedocs.io/)
[![hypothesis](https://img.shields.io/badge/fuzzing-hypothesis-orange.svg)](https://hypothesis.readthedocs.io/)

This repository contains the complete implementation, test suites, coverage reports, and deliverables for **Software Engineering Lab 6** and **Lab 7** based on the Customs Duty Calculator project (`L6_L7_35_customs_duty`).

---

## Table of Contents

- [Overview](#overview)
- [Lab 6: Code and Branch Coverage Analysis](#lab-6-code-and-branch-coverage-analysis)
  - [Objectives](#lab-6-objectives)
  - [Deliverables](#lab-6-deliverables)
  - [Coverage Results](#lab-6-coverage-results)
- [Lab 7: Fuzzing for Input Validation Bugs](#lab-7-fuzzing-for-input-validation-bugs)
  - [Objectives](#lab-7-objectives)
  - [Fuzzing with Hypothesis](#fuzzing-with-hypothesis)
  - [Bugs Discovered & Defensive Hardening](#bugs-discovered--defensive-hardening)
- [Project Structure](#project-structure)
- [Setup and Running Tests](#setup-and-running-tests)
- [Pull Requests & Issue Tracking](#pull-requests--issue-tracking)

---

## Lab 6: Code and Branch Coverage Analysis

### Lab 6 Objectives
- Differentiate between statement (line) coverage and branch (decision) coverage.
- Measure baseline coverage for initial test cases and identify untested execution paths.
- Design targeted test cases to achieve **>=90% line coverage** and **>=90% branch coverage** (achieved **100%** on both).

### Lab 6 Deliverables
- `lab6/CodeCoverageTest_customs_duty.py`: Full line coverage test suite.
- `lab6/BranchCoverageTest_customs_duty.py`: Complete branch coverage test suite covering all decision branches.
- `lab6/test_customs_duty.py`: Consolidated test suite for pytest.
- Terminal output screenshots and coverage analysis report.

---

## Lab 7: Fuzzing for Input Validation Bugs

### Lab 7 Objectives
- Explore property-based fuzz testing using Python's `Hypothesis` library.
- Formulate "no-crash" properties across random Unicode strings, empty inputs, and null/None values.
- Uncover edge-case vulnerabilities and runtime exceptions in `customs_duty.py`.
- Apply defensive programming techniques to harden functions against malformed inputs.

### Lab 7 Deliverables
- `lab7/test_customs_duty.py`: Property-based Hypothesis fuzz tests.
- `lab7/customs_duty.py`: Hardened application code resilient to malformed and unexpected inputs.
- Step-by-step terminal output screenshots (initial buggy run, Hypothesis failure traces, fixed execution, passing fuzz test suite).
- Comprehensive PDF report.

---

## Project Structure

```text
se-lab-6-7/
├── .gitignore
├── README.md
├── lab6/
│   ├── README.md
│   ├── .coveragerc
│   ├── customs_duty.py
│   ├── test_customs_duty.py
│   ├── CodeCoverageTest_customs_duty.py
│   ├── BranchCoverageTest_customs_duty.py
│   ├── screenshots/
│   └── Lab6_Coverage_Analysis_Report.pdf
└── lab7/
    ├── README.md
    ├── customs_duty.py
    ├── test_customs_duty.py
    ├── screenshots/
    └── Lab7_Fuzz_Testing_Report.pdf
```
