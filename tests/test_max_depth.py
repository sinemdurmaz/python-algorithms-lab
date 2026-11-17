import pytest
from data_structures.binary_tree import BinaryTree
from algorithms.max_depth_binary_tree import max_depth


@pytest.mark.parametrize("tree_levels, expected_depth", [
    ([3, 9, 20, None, None, 15, 7], 3),     # Klasik LeetCode #104 örneği
    ([1, None, 2], 2),                       # İki seviyeli sağa eğik ağaç
    ([], 0),                                 # Boş ağaç
    ([1], 1),                                # Tek düğüm
    ([1, 2, 3, 4, 5, 6, 7], 3),              # Tam dengeli 3 seviyeli ağaç
    ([1, 2, None, 3, None, 4], 4),           # Tek yöne uzayan derin ağaç
])
def test_max_depth_scenarios(tree_levels: list, expected_depth: int):
    """LeetCode #104 İkili Ağaç Maksimum Derinlik senaryolarını test eder."""
    tree = BinaryTree.from_level_order(tree_levels)
    assert max_depth(tree.root) == expected_depth
