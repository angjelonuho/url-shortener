import string
import pytest
from app.utils import generate_shortcode

def test_generate_shortcode_length():
    shortcode = generate_shortcode()
    assert len(shortcode) == 6

def test_generate_shortcode_characters():
    shortcode = generate_shortcode()
    assert all(c.isalnum() or c == '_' for c in shortcode)