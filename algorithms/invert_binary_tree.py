from typing import Optional, TypeVar
from data_structures.binary_tree import TreeNode

T = TypeVar("T")


def invert_tree(root: Optional[TreeNode[T]]) -> Optional[TreeNode[T]]:
    """
    LeetCode #226: Invert Binary Tree (İkili Ağacı Tersine Çevirme / Ayna Yansıması)

    Verilen bir ikili ağacın her düğümündeki sol ve sağ alt ağaçları
    ayna yansıması oluşturacak şekilde yer değiştirir.

    Algoritma Tekniği: Özyinelemeli Derinlik Öncelikli Arama (DFS / Recursion)
    Zaman Karmaşıklığı: O(N) - Ağaçtaki tüm N düğüm tam bir kez ziyaret edilir.
    Alan Karmaşıklığı: O(H) - Çağrı yığını (call stack) ağaç yüksekliği H kadardır.
                             Dengeli ağaçta O(log N), tek yönlü ağaçta O(N).
    """
    if root is None:
        return None

    # Sol ve sağ çocukları ters çevirerek yer değiştir
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)

    return root
