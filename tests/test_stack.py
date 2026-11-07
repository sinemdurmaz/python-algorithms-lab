import pytest
from data_structures.stack import Stack
from algorithms.valid_parentheses import is_valid_parentheses


def test_stack_basic_operations():
    """Stack push, pop, peek, size ve is_empty operasyonlarını test eder."""
    stack = Stack[int]()
    assert stack.is_empty() is True
    assert stack.size() == 0

    # Push
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.is_empty() is False
    assert stack.size() == 3

    # Peek (En üstteki 30 olmalı ama çıkarılmamalı)
    assert stack.peek() == 30
    assert stack.size() == 3

    # Pop (LIFO - En son giren 30 ilk çıkmalı)
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty() is True


def test_stack_empty_pop_raises_error():
    """Boş stack'ten eleman çekmeye veya tepeye bakmaya çalışıldığında IndexError fırlatılmalı."""
    stack = Stack[str]()
    with pytest.raises(IndexError, match="Boş bir yığından"):
        stack.pop()

    with pytest.raises(IndexError, match="Boş bir yığının"):
        stack.peek()


@pytest.mark.parametrize("input_str, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("", True),
    ("(((", False),
    (")))", False),
    ("{[()]}", True),
])
def test_valid_parentheses(input_str: str, expected: bool):
    """LeetCode #20 Dengeli parantez senaryolarını test eder."""
    assert is_valid_parentheses(input_str) == expected
