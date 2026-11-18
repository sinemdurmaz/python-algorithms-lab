def find_max_average(nums: list[int], k: int) -> float:
    """
    LeetCode #643: Maximum Average Subarray I (Maksimum Ortalama Alt Dizi)

    n elemanlı bir tam sayı dizisinde k uzunluğundaki ardışık alt diziler
    arasında maksimum ortalamaya sahip olanın ortalamasını hesaplar.

    Algoritma Tekniği: Sabit Boyutlu Kayan Pencere (Fixed-size Sliding Window)
    Zaman Karmaşıklığı: O(N) - Dizi boyunca pencere 1'er adım kayar.
    Alan Karmaşıklığı: O(1) - Sabit ek bellek kullanılır.
    """
    if len(nums) < k or k <= 0:
        raise ValueError("Dizi uzunluğu k değerinden küçük olamaz ve k pozitif olmalıdır.")

    # 1. İlk k boyutlu pencerenin toplamını hesapla
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # 2. Pencereyi sağa doğru kaydır: çıkan elemanı çıkar, giren elemanı ekle
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return float(max_sum / k)
