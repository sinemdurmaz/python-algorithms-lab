from collections import deque
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    """
    İkili Ağaç Düğümü (Binary Tree Node).
    """

    def __init__(
        self,
        val: T,
        left: Optional["TreeNode[T]"] = None,
        right: Optional["TreeNode[T]"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class BinaryTree(Generic[T]):
    """
    İkili Ağaç (Binary Tree) Veri Yapısı.
    Hiyerarşik veri yapısı; her düğümün en fazla 2 çocuğu (sol ve sağ) olabilir.
    """

    def __init__(self, root: Optional[TreeNode[T]] = None) -> None:
        self.root = root

    @classmethod
    def from_level_order(cls, values: list[Optional[T]]) -> "BinaryTree[T]":
        """
        LeetCode standart seviye sırası (Level-order / BFS) listesinden
        ikili ağaç inşa eden fabrika metodu. Örn: [4, 2, 7, 1, 3, 6, 9]
        """
        if not values or values[0] is None:
            return cls(None)

        root = TreeNode(values[0])
        queue: deque[TreeNode[T]] = deque([root])
        idx = 1
        n = len(values)

        while queue and idx < n:
            curr = queue.popleft()

            # Sol çocuk
            if idx < n and values[idx] is not None:
                curr.left = TreeNode(values[idx])  # type: ignore[arg-type]
                queue.append(curr.left)
            idx += 1

            # Sağ çocuk
            if idx < n and values[idx] is not None:
                curr.right = TreeNode(values[idx])  # type: ignore[arg-type]
                queue.append(curr.right)
            idx += 1

        return cls(root)

    def to_level_order(self) -> list[Optional[T]]:
        """Ağacı seviye sırası (BFS) listesine dönüştürür."""
        if self.root is None:
            return []

        result: list[Optional[T]] = []
        queue: deque[Optional[TreeNode[T]]] = deque([self.root])

        while queue:
            node = queue.popleft()
            if node is not None:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Sondaki gereksiz None'ları temizle
        while result and result[-1] is None:
            result.pop()

        return result
