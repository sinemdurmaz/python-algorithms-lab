import pytest
from data_structures.binary_tree import BinaryTree, TreeNode
from algorithms.invert_binary_tree import invert_tree


def test_binary_tree_basic_creation():
    """TreeNode ve BinaryTree temel oluşturma ve seviye sırası metodlarını test eder."""
    tree = BinaryTree.from_level_order([4, 2, 7, 1, 3, 6, 9])
    assert tree.root is not None
    assert tree.root.val == 4
    assert tree.root.left.val == 2
    assert tree.root.right.val == 7
    assert tree.to_level_order() == [4, 2, 7, 1, 3, 6, 9]


def test_empty_binary_tree():
    """Boş ağaç senaryolarını test eder."""
    tree = BinaryTree.from_level_order([])
    assert tree.root is None
    assert tree.to_level_order() == []
    assert invert_tree(None) is None


@pytest.mark.parametrize("initial_levels, expected_inverted", [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),  # Klasik LeetCode #226 örneği
    ([2, 1, 3], [2, 3, 1]),                          # Küçük 2 seviyeli ağaç
    ([1], [1]),                                      # Tek düğüm
    ([], []),                                        # Boş ağaç
    ([1, 2], [1, None, 2]),                          # Yalnızca sol çocuğu olan asimetrik ağaç
    ([1, None, 2], [1, 2]),                          # Yalnızca sağ çocuğu olan asimetrik ağaç
    (["A", "B", "C"], ["A", "C", "B"]),              # Generic tip desteği (String)
])
def test_invert_binary_tree(initial_levels: list, expected_inverted: list):
    """LeetCode #226 İkili Ağacı Tersine Çevirme senaryolarını test eder."""
    tree = BinaryTree.from_level_order(initial_levels)
    inverted_root = invert_tree(tree.root)
    inverted_tree = BinaryTree(inverted_root)
    assert inverted_tree.to_level_order() == expected_inverted
