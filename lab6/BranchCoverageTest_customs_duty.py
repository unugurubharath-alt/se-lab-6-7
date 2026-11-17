import pytest
from customs_duty import duty_rate, total_duty, clearance_channel

# =====================================================================
# Branch Coverage Tests for duty_rate(category, origin)
# =====================================================================

def test_branch_duty_rate_prohibited_true():
    # Branch: category in PROHIBITED -> True
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("weapons", "FTA")
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("narcotics", "US")

def test_branch_duty_rate_electronics():
    # Branch: category == "electronics" -> True
    # Sub-branch: origin == "FTA" -> True
    assert duty_rate("electronics", "FTA") == 0.10
    # Sub-branch: origin == "FTA" -> False
    assert duty_rate("electronics", "US") == 0.20

def test_branch_duty_rate_clothing():
    # Branch: category == "clothing" -> True
    # Sub-branch: origin == "FTA" -> True
    assert duty_rate("clothing", "FTA") == 0.05
    # Sub-branch: origin == "FTA" -> False
    assert duty_rate("clothing", "US") == 0.12

def test_branch_duty_rate_books():
    # Branch: category == "books" -> True
    assert duty_rate("books", "FTA") == 0
    assert duty_rate("books", "WORLD") == 0

def test_branch_duty_rate_other_category():
    # Branch: all category == ... conditions evaluate to False
    assert duty_rate("automotive", "US") == 0.15
    assert duty_rate("stationery", "FTA") == 0.15


# =====================================================================
# Branch Coverage Tests for total_duty(category, value, origin, is_gift)
# =====================================================================

def test_branch_total_duty_negative_value():
    # Branch: value < 0 -> True
    with pytest.raises(ValueError, match="negative value"):
        total_duty("books", -1, "US", False)

def test_branch_total_duty_gift_under_or_equal_threshold():
    # Branch: is_gift -> True
    # Sub-branch: value <= 5000 -> True
    assert total_duty("electronics", 5000, "US", True) == 0
    assert total_duty("clothing", 0, "FTA", True) == 0

def test_branch_total_duty_gift_above_threshold_minimum_duty():
    # Branch: is_gift -> True, value <= 5000 -> False
    # Sub-branch: 0 < duty < 50 -> True (duty replaced by 50)
    # value = 5200, remaining = 200, duty_rate = 0.05 => duty = 10 -> becomes 50
    assert total_duty("clothing", 5200, "FTA", True) == 50

def test_branch_total_duty_gift_above_threshold_normal_duty():
    # Branch: is_gift -> True, value <= 5000 -> False
    # Sub-branch: duty >= 50 -> (0 < duty < 50 is False)
    # value = 6000, remaining = 1000, duty_rate = 0.20 => duty = 200
    assert total_duty("electronics", 6000, "US", True) == 200

def test_branch_total_duty_gift_above_threshold_zero_duty():
    # Branch: is_gift -> True, value <= 5000 -> False
    # Sub-branch: duty == 0 -> (0 < duty < 50 is False)
    # category = "books", rate = 0 => duty = 0
    assert total_duty("books", 7000, "US", True) == 0

def test_branch_total_duty_commercial_under_or_equal_threshold():
    # Branch: is_gift -> False
    # Sub-branch: value <= 1000 -> True
    assert total_duty("electronics", 1000, "US", False) == 0
    assert total_duty("clothing", 0, "FTA", False) == 0

def test_branch_total_duty_commercial_above_threshold_normal():
    # Branch: is_gift -> False, value <= 1000 -> False
    # Sub-branch: duty >= 50
    # value = 2000, electronics US rate = 0.20 => duty = 400
    assert total_duty("electronics", 2000, "US", False) == 400

def test_branch_total_duty_commercial_above_threshold_zero_rate():
    # Branch: is_gift -> False, value <= 1000 -> False
    # Sub-branch: duty == 0
    assert total_duty("books", 2000, "FTA", False) == 0


# =====================================================================
# Branch Coverage Tests for clearance_channel(value, category, has_documents)
# =====================================================================

def test_branch_clearance_prohibited_true():
    # Branch: category in PROHIBITED -> True
    assert clearance_channel(500, "weapons", True) == "refuse"
    assert clearance_channel(200000, "narcotics", False) == "refuse"

def test_branch_clearance_high_value_true():
    # Branch: category in PROHIBITED -> False
    # Branch: value > 100000 -> True
    assert clearance_channel(150000, "electronics", True) == "inspect"
    assert clearance_channel(100001, "clothing", False) == "inspect"

def test_branch_clearance_medium_value_no_documents():
    # Branch: category in PROHIBITED -> False, value <= 100000 -> True
    # Compound: value > 20000 (True) AND not has_documents (True) -> True
    assert clearance_channel(50000, "electronics", False) == "inspect"

def test_branch_clearance_medium_value_with_documents():
    # Branch: value > 20000 (True) AND not has_documents (False) -> False
    assert clearance_channel(50000, "electronics", True) == "green"

def test_branch_clearance_low_value_no_documents():
    # Branch: value > 20000 (False) AND not has_documents (True) -> False
    assert clearance_channel(15000, "clothing", False) == "green"

def test_branch_clearance_low_value_with_documents():
    # Branch: value > 20000 (False) AND not has_documents (False) -> False
    assert clearance_channel(15000, "clothing", True) == "green"

def test_branch_clearance_boundary_20000():
    # Boundary value == 20000 (not > 20000)
    assert clearance_channel(20000, "books", False) == "green"

def test_branch_clearance_boundary_100000():
    # Boundary value == 100000 (not > 100000)
    assert clearance_channel(100000, "books", True) == "green"
