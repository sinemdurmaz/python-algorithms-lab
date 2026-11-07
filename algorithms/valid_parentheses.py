from data_structures.stack import Stack


def is_valid_parentheses(s: str) -> bool:
    """
    LeetCode #20: Valid Parentheses (Dengeli Parantezler)
    
    Verilen string içindeki parantezlerin ('()', '{}', '[]') doğru sırada ve
    dengeli bir şekilde açılıp kapandığını doğrular.
    
    Veri Yapısı: Stack (Yığın)
    Zaman Karmaşıklığı: O(N) - String baştan sona yalnızca bir kez taranır.
    Alan Karmaşıklığı: O(N) - En kötü durumda (örn: "(((((") tüm karakterler yığına girer.
    """
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = Stack[str]()

    for char in s:
        # Açılış parantezi ise yığına (Stack) ekle
        if char in bracket_map.values():
            stack.push(char)
        # Kapanış parantezi ise
        elif char in bracket_map:
            # Yığın boşsa (eşleşecek açılış yoksa) veya tepedekiyle uyuşmuyorsa
            if stack.is_empty() or stack.pop() != bracket_map[char]:
                return False

    # Tüm açılışlar kapanışlarıyla başarıyla eşleşip yığın boşaldıysa True döner
    return stack.is_empty()
