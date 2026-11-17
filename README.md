# Software Engineering Lab 6 & 7: Customs Duty Calculator

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/tested%20with-pytest-blue.svg)](https://pytest.org/)
[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://coverage.readthedocs.io/)
[![hypothesis](https://img.shields.io/badge/fuzzing-hypothesis-orange.svg)](https://hypothesis.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Student Name:** Bharath  
**GitHub Username:** [unugurubharath-alt](https://github.com/unugurubharath-alt)  
**Assigned Template Repository:** [SETAPESU26/L6_L7_35_customs_duty](https://github.com/SETAPESU26/L6_L7_35_customs_duty)  
**Active Project Repository:** [unugurubharath-alt/se-lab-6-7](https://github.com/unugurubharath-alt/se-lab-6-7)

---

## Executive Summary

This repository contains the complete implementation, test suites, terminal output screenshots, and comprehensive PDF deliverables for:
1. **Lab 6: Code and Branch Coverage Analysis**
   - Baseline line coverage: 36% -> **100%** line coverage achieved.
   - Baseline branch coverage: 31% -> **100%** branch coverage achieved.
   - Test files: [`lab6/CodeCoverageTest_customs_duty.py`](lab6/CodeCoverageTest_customs_duty.py) and [`lab6/BranchCoverageTest_customs_duty.py`](lab6/BranchCoverageTest_customs_duty.py).
   - Report: [`lab6/Lab6_Coverage_Analysis_Report.pdf`](lab6/Lab6_Coverage_Analysis_Report.pdf).
2. **Lab 7: Fuzzing for Input Validation Bugs**
   - Property-based fuzz testing using **Hypothesis**.
   - Uncovered critical input validation crashes (`AttributeError`, `ValueError` on empty strings, None, malformed delimiters).
   - Fixed and hardened application using defensive programming techniques.
   - All Hypothesis fuzz tests passing cleanly (100%).
   - Report: [`lab7/Lab7_Fuzz_Testing_Report.pdf`](lab7/Lab7_Fuzz_Testing_Report.pdf).

---

## GitHub Workflow: Issues Raised and Closed by Pull Requests

Every feature and bug fix was implemented via dedicated GitHub issues, feature branches, and pull requests:

| Issue | Title | Pull Request | Status |
|-------|-------|--------------|--------|
| [#1](https://github.com/unugurubharath-alt/se-lab-6-7/issues/1) | Lab 6: Achieve >=90% Line Code Coverage | [#2](https://github.com/unugurubharath-alt/se-lab-6-7/pull/2) | Merged & Closed |
| [#3](https://github.com/unugurubharath-alt/se-lab-6-7/issues/3) | Lab 6: Achieve >=90% Branch Coverage | [#4](https://github.com/unugurubharath-alt/se-lab-6-7/pull/4) | Merged & Closed |
| [#5](https://github.com/unugurubharath-alt/se-lab-6-7/issues/5) | Lab 7: Implement Hypothesis Fuzz Testing | [#6](https://github.com/unugurubharath-alt/se-lab-6-7/pull/6) | Merged & Closed |
| [#7](https://github.com/unugurubharath-alt/se-lab-6-7/issues/7) | Lab 7: Harden customs duty processor | [#8](https://github.com/unugurubharath-alt/se-lab-6-7/pull/8) | Merged & Closed |
| [#9](https://github.com/unugurubharath-alt/se-lab-6-7/issues/9) | Docs: Generate Lab 6 and Lab 7 PDF Deliverables | [#10](https://github.com/unugurubharath-alt/se-lab-6-7/pull/10) | Merged & Closed |

---

## Project Structure

```text
se-lab-6-7/
├── .gitignore
├── README.md
├── Lab6_Coverage_Analysis_Report.pdf
├── Lab7_Fuzz_Testing_Report.pdf
├── lab6/
│   ├── README.md
│   ├── .coveragerc
│   ├── customs_duty.py
│   ├── test_customs_duty.py
│   ├── CodeCoverageTest_customs_duty.py
│   ├── BranchCoverageTest_customs_duty.py
│   ├── screenshots/
│   │   ├── initial_line_coverage.png
│   │   ├── code_coverage_100.png
│   │   └── branch_coverage_100.png
│   └── Lab6_Coverage_Analysis_Report.pdf
└── lab7/
    ├── README.md
    ├── customs_duty.py
    ├── test_customs_duty.py
    ├── screenshots/
    │   ├── step2_buggy_output.png
    │   ├── step4_fuzz_failing.png
    │   ├── step5_fixed_output.png
    │   └── step6_fuzz_passing.png
    └── Lab7_Fuzz_Testing_Report.pdf
```

---

## Instructions to Run Tests

### Prerequisites
```bash
pip install pytest coverage hypothesis fpdf2 pillow
```

### Lab 6 Commands
```bash
cd lab6

# Statement Coverage
coverage run -m pytest CodeCoverageTest_customs_duty.py
coverage report -m

# Branch Coverage
coverage run --branch -m pytest BranchCoverageTest_customs_duty.py
coverage report -m
```

### Lab 7 Commands
```bash
cd lab7

# Run application
python customs_duty.py

# Run Hypothesis fuzz tests
pytest test_customs_duty.py
```
