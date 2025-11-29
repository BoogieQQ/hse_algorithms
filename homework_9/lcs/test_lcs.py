from main import lcs

def test_example():
    string_1 = "AGGTAB"
    string_2 = "GXTXAYB"
    
    lcs_string, lcs_length = lcs(string_1, string_2)
    
    assert lcs_length == 4
    assert lcs_string == "GTAB"

def test_empty_strings():
    lcs_string, lcs_length = lcs("", "")
    assert lcs_length == 0
    assert lcs_string == ""

def test_first_empty_string():
    lcs_string, lcs_length = lcs("", "abc")
    assert lcs_length == 0
    assert lcs_string == ""

def test_second_empty_string():
    lcs_string, lcs_length = lcs("abc", "")
    assert lcs_length == 0
    assert lcs_string == ""

def test_identical_strings():
    test_str = "abc"
    lcs_string, lcs_length = lcs(test_str,  test_str)
    assert lcs_length == len(test_str)
    assert lcs_string == test_str

def test_no_common_subsequence():
    lcs_string, lcs_length = lcs("abc", "123")
    assert lcs_length == 0
    assert lcs_string == ""

def test_single_character_common():
    lcs_string, lcs_length = lcs("abc", "123a")
    assert lcs_length == 1
    assert lcs_string == "a"

def test_multiple_common_characters():
    lcs_string, lcs_length = lcs("abcd", "acbd")
    assert lcs_length == 3
    assert lcs_string in ["acd", "abd"]

def test_case_sensitive():
    lcs_string, lcs_length = lcs("Hello", "hello")
    assert lcs_length == 4
    assert lcs_string == "ello"

def test_special_characters():
    lcs_string, lcs_length = lcs("a!b@c#", "1!2@3#")
    assert lcs_length == 3
    assert lcs_string == "!@#"
