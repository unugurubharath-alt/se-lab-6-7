from hypothesis import given, strategies as st, settings
from customs_duty import parse_declaration, duty_amount, hs_chapter

# Configure hypothesis to run cleanly in memory
settings.register_profile("ci", database=None)
settings.load_profile("ci")

@given(st.text() | st.none())
def test_parse_declaration_no_crash(s):
    try:
        parse_declaration(s)
    except Exception as e:
        assert False, f"parse_declaration crashed with: {e}"

@given(st.text() | st.none())
def test_duty_amount_no_crash(s):
    try:
        duty_amount(s)
    except Exception as e:
        assert False, f"duty_amount crashed with: {e}"

@given(st.text() | st.none())
def test_hs_chapter_no_crash(s):
    try:
        hs_chapter(s)
    except Exception as e:
        assert False, f"hs_chapter crashed with: {e}"
