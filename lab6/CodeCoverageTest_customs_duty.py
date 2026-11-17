import pytest
from customs_duty import duty_rate, total_duty, clearance_channel

# ==========================================
# Unit Tests for duty_rate(category, origin)
# ==========================================

def test_duty_rate_prohibited_weapons():
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("weapons", "US")

def test_duty_rate_prohibited_narcotics():
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("narcotics", "FTA")

def test_duty_rate_electronics_fta():
    assert duty_rate("electronics", "FTA") == 0.10

def test_duty_rate_electronics_non_fta():
    assert duty_rate("electronics", "US") == 0.20

def test_duty_rate_clothing_fta():
    assert duty_rate("clothing", "FTA") == 0.05

def test_duty_rate_clothing_non_fta():
    assert duty_rate("clothing", "US") == 0.12

def test_duty_rate_books():
    assert duty_rate("books", "FTA") == 0
    assert duty_rate("books", "US") == 0

def test_duty_rate_default_category():
    assert duty_rate("furniture", "US") == 0.15
    assert duty_rate("toys", "FTA") == 0.15

# ===================================================
# Unit Tests for total_duty(category, value, origin, is_gift)
# ===================================================

def test_total_duty_negative_value():
    with pytest.raises(ValueError, match="negative value"):
        total_duty("books", -10, "US", False)

def test_total_duty_gift_under_threshold():
    # Gift value <= 5000 is duty free
    assert total_duty("electronics", 5000, "US", True) == 0
    assert total_duty("clothing", 1000, "FTA", True) == 0

def test_total_duty_gift_above_threshold_minimum_duty():
    # Gift value > 5000, value becomes 200, clothing FTA rate is 0.05 => 200 * 0.05 = 10 (< 50 => minimum duty 50)
    assert total_duty("clothing", 5200, "FTA", True) == 50

def test_total_duty_gift_above_threshold_normal_duty():
    # Gift value > 5000, value becomes 10000, electronics US rate is 0.20 => 10000 * 0.20 = 2000 (>= 50)
    assert total_duty("electronics", 15000, "US", True) == 2000

def test_total_duty_commercial_under_threshold():
    # Commercial value <= 1000 is duty free
    assert total_duty("electronics", 1000, "US", False) == 0
    assert total_duty("clothing", 500, "FTA", False) == 0

def test_total_duty_commercial_duty_free_category():
    # Commercial books > 1000 has 0 duty rate => duty is 0
    assert total_duty("books", 5000, "US", False) == 0

def test_total_duty_commercial_normal_duty():
    # Commercial electronics > 1000
    assert total_duty("electronics", 10000, "FTA", False) == 10000 * 0.10

# ==============================================================
# Unit Tests for clearance_channel(value, category, has_documents)
# ==============================================================

def test_clearance_channel_prohibited_item():
    assert clearance_channel(500, "weapons", True) == "refuse"
    assert clearance_channel(50000, "narcotics", False) == "refuse"

def test_clearance_channel_high_value():
    assert clearance_channel(150000, "electronics", True) == "inspect"
    assert clearance_channel(100001, "clothing", False) == "inspect"

def test_clearance_channel_medium_value_no_documents():
    assert clearance_channel(25000, "electronics", False) == "inspect"

def test_clearance_channel_medium_value_with_documents():
    assert clearance_channel(25000, "electronics", True) == "green"

def test_clearance_channel_low_value():
    assert clearance_channel(15000, "clothing", True) == "green"
    assert clearance_channel(15000, "clothing", False) == "green"
