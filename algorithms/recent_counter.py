from data_structures.queue import Queue


class RecentCounter:
    """
    LeetCode #933: Number of Recent Calls (Kuyruk ile Zaman Penceresi Hesaplama)
    
    Son 3000 milisaniye (3 saniye) içindeki aktif istek sayısını döner.
    Gelen isteklerin zaman damgası t her zaman artandır (t1 < t2 < t3...).
    
    Veri Yapısı: Queue (FIFO)
    Zaman Karmaşıklığı: Amortized O(1) - Her istek kuyruğa 1 kez girer ve en fazla 1 kez çıkar.
    Alan Karmaşıklığı: O(W) - W, 3000 ms penceresi içindeki maksimum istek sayısıdır.
    """
    def __init__(self) -> None:
        self.requests = Queue[int]()

    def ping(self, t: int) -> int:
        """Yeni bir istek geldiğinde zaman damgası (t) eklenir ve pencere hesaplanır."""
        self.requests.enqueue(t)

        # 3000 ms'den daha eski olan istekleri kuyruğun başından temizle
        while not self.requests.is_empty() and self.requests.front() < t - 3000:
            self.requests.dequeue()

        # Kalan istek sayısı son 3000 ms penceresindeki aktif sayıdır
        return self.requests.size()
