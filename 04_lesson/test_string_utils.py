from pickle import FALSE

import pytest
from string_utils import StringUtils
string_utils = StringUtils()

# Первая буква заглавная и возвращается в этот же текст
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123", "123"),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Удаляет пробелы в начале, если они есть
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  student", "student"),
    ("seeYou", "seeYou"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   ", ""),
    ("", ""),
])
def test_trim_negative(input_str, expected):
        assert string_utils.trim(input_str) == expected

# Возвращает `True`, если строка содержит искомый символ и `False` - если нет
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Number", "N", True),
    ("Word", "e", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("🤑", "H", False),
    ("Summer", " ", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# Удаляет все подстроки из переданной строки
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Nokiat", "t", "Nokia"),
    ("Tik a Tok", " a ", "TikTok"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("123456789", "123", "456789"),
    ("@%$", "@", "%$"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
