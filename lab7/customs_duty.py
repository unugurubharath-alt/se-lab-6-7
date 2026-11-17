import math


def parse_declaration(text):
    """
    Parses a customs declaration string in format 'category:value'.
    Hardened defensively against non-strings, malformed delimiters, empty fields,
    negative numbers, NaN, and Infinity. Returns (category, float(value)) or None.
    """
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    category = parts[0].strip().lower()
    val_str = parts[1].strip()
    if not category:
        return None
    try:
        val = float(val_str)
        if math.isnan(val) or math.isinf(val) or val < 0:
            return None
        return category, val
    except (ValueError, TypeError, OverflowError):
        return None


def duty_amount(text):
    """
    Parses a duty expression in format 'value@rate' and calculates duty.
    Hardened defensively against non-strings, missing delimiters, non-numeric values,
    negative numbers, NaN, Infinity, and numerical overflows. Returns float or None.
    """
    if not isinstance(text, str):
        return None
    parts = text.split('@')
    if len(parts) != 2:
        return None
    try:
        val = float(parts[0].strip())
        rate = float(parts[1].strip())
        if math.isnan(val) or math.isinf(val) or math.isnan(rate) or math.isinf(rate):
            return None
        if val < 0 or rate < 0:
            return None
        result = val * rate / 100
        if math.isnan(result) or math.isinf(result):
            return None
        return result
    except (ValueError, TypeError, OverflowError):
        return None


def hs_chapter(code):
    """
    Extracts the 2-digit Harmonized System (HS) chapter number from code string.
    Hardened defensively against non-strings, missing dots, non-numeric characters,
    and out-of-range chapters. Returns integer chapter (1-99) or None.
    """
    if not isinstance(code, str):
        return None
    parts = code.split('.')
    prefix = parts[0].strip()
    if len(prefix) < 2:
        return None
    two_digits = prefix[:2]
    if not two_digits.isdigit():
        return None
    val = int(two_digits)
    if val < 1 or val > 99:
        return None
    return val


def main():
    print("==== Running parse_declaration ====")
    user_input = input("Enter category:value (e.g. electronics:25000): ")
    result = parse_declaration(user_input)
    print("Category and Value:", result)

    print("\n==== Running duty_amount ====")
    user_input = input("Enter value@rate (e.g. 25000@20): ")
    result = duty_amount(user_input)
    print("Duty Amount:", result)

    print("\n==== Running hs_chapter ====")
    user_input = input("Enter an HS code (e.g. 8517.12): ")
    result = hs_chapter(user_input)
    print("Chapter:", result)


if __name__ == "__main__":
    main()
