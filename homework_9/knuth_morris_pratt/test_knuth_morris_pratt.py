from main import kmp_search


def test_basic_target():
    text = "abcd 123"
    target = "123"
    result = kmp_search(text, target)
    assert result == [5]

def test_target_at_beginning():
    text = "abcd 123"
    target = "abcd"
    result = kmp_search(text, target)
    assert result == [0]

def test_multiple_occurrences():
    text = "abababab"
    target = "ab"
    result = kmp_search(text, target)
    assert result == [0, 2, 4, 6]

def test_target_not_found():
    text = "abcd 123"
    target = "?"
    result = kmp_search(text, target)
    assert result == []

def test_empty_target():
    text = "abcd 123"
    target = ""
    result = kmp_search(text, target)
    assert result == []

def test_empty_text():
    text = ""
    target = "ab"
    result = kmp_search(text, target)
    assert result == []

def test_both_empty():
    text = ""
    target = ""
    result = kmp_search(text, target)
    assert result == []

def test_target_longer_than_text():
    text = "ab"
    target = "abcd"
    result = kmp_search(text, target)
    assert result == []

def test_single_character():
    text = "abcabcabc"
    target = "a"
    result = kmp_search(text, target)
    assert result == [0, 3, 6]

def test_case_sensitive():
    text = "Abc abc ABC"
    target = "abc"
    result = kmp_search(text, target)
    assert result == [4]

def test_special_characters():
    text = "abc!@#123"
    target = "!@#"
    result = kmp_search(text, target)
    assert result == [3]

def test_overlapping_targets():
    text = "aaaaaa"
    target = "aaa"
    result = kmp_search(text, target)
    assert result == [0, 1, 2, 3]
