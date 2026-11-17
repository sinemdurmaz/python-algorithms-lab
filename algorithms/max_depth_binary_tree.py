from typing import Optional, TypeVar
from data_structures.binary_tree import TreeNode

T = TypeVar("T")


def max_depth(root: Optional[TreeNode[T]]) -> int:
    """
    LeetCode #104: Maximum Depth of Binary Tree (İkili Ağacın Maksimum Derinliği)

    Kök düğümden en uzak yaprak düğüme (leaf node) kadar olan
    en uzun yol üzerindeki düğüm sayısını hesaplar.

    Algoritma Tekniği: Özyinelemeli Derinlik Öncelikli Arama (DFS / Recursion)
    Zaman Karmaşıklığı: O(N) - Ağaçtaki tüm N düğüm birer kez taranır.
    Alan Karmaşıklığı: O(H) - Ağaç yüksekliği kadar çağrı yığını (call stack) harcanır.
    """
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)
