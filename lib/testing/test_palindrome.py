from palindrome import longest_palindromic_substring
import pytest

def test_longest_palindromic_substring():
    assert longest_palindromic_substring("babad") == "aba" or longest_palindromic_substring("babad") == "bab"
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("character") == "ara"
    assert longest_palindromic_substring("reference") == "refer"
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("ac") == "a" or longest_palindromic_substring("ac") == "c"
    assert longest_palindromic_substring("banana") == "anana"
    
    
def test_empty_string():
    assert longest_palindromic_substring("") == ""
    
    
def test_invalid_input_type():
    try:
        longest_palindromic_substring(None)
    except TypeError:
        print("Caught expected type error!")
        