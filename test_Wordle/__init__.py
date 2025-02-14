"""Test to ensure proper function of wordle."""
from wordle import Wordle

# Pytest test suite

def test_check_guess():
    """Test the check guess function"""
    assert Wordle.check_guess("puppy", "puppy") == "✅✅✅✅✅"
    assert Wordle.check_guess("puppy", "pyapy") == "✅❓❌✅✅"
    assert Wordle.check_guess("puppy", "ppppp") == "✅❓✅✅❌"
    assert Wordle.check_guess("puppy", "xxxxx") == "❌❌❌❌❌"

def test_generate_word():
    """Test generat_word, function"""
    assert isinstance(Wordle.generate_word(), str)
    assert len(Wordle.generate_word()) == 5
