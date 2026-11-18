def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    LeetCode #219: Contains Duplicate II (Yakın Eleman Tekrarı)

    Dizide birbirine en fazla k indeks mesafesinde (abs(i - j) <= k)
    aynı değere sahip iki eleman bulunup bulunmadığını kontrol eder.

    Algoritma Tekniği: Kayan Pencere + Hash Set (Sliding Window & Hash Set)
    Zaman Karmaşıklığı: O(N) - Her eleman kümeye bir kez eklenir ve en fazla bir kez çıkarılır.
    Alan Karmaşıklığı: O(min(N, k)) - Kümede aynı anda en fazla k eleman tutulur.
    """
    if k <= 0 or not nums:
        return False

    window: set[int] = set()

    for i, num in enumerate(nums):
        # 1. Şu anki k boyutlu pencerede bu eleman zaten var mı?
        if num in window:
            return True

        # 2. Yeni elemanı pencereye ekle
        window.add(num)

        # 3. Pencere boyutu k'yı aştıysa pencereden çıkan en eski elemanı sil
        if len(window) > k:
            window.remove(nums[i - k])

    return False
