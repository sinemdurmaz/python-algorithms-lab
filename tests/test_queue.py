import pytest
from data_structures.queue import Queue
from algorithms.recent_counter import RecentCounter


def test_queue_fifo_order():
    """Kuyruğun FIFO (İlk Giren İlk Çıkar) sırasını test eder."""
    q = Queue[str]()
    assert q.is_empty() is True
    assert q.size() == 0

    # Kuyruğa eleman ekle: Müşteri A, Müşteri B, Müşteri C
    q.enqueue("Müşteri A")
    q.enqueue("Müşteri B")
    q.enqueue("Müşteri C")

    assert q.is_empty() is False
    assert q.size() == 3

    # Front: İlk sıradaki Müşteri A olmalı ama sıradan çıkmamalı
    assert q.front() == "Müşteri A"
    assert q.size() == 3

    # Dequeue: İlk giren ilk çıkar
    assert q.dequeue() == "Müşteri A"
    assert q.dequeue() == "Müşteri B"
    assert q.dequeue() == "Müşteri C"
    assert q.is_empty() is True


def test_queue_empty_dequeue_raises_error():
    """Boş kuyruktan eleman almaya çalışıldığında IndexError fırlatılmalı."""
    q = Queue[int]()
    with pytest.raises(IndexError, match="Boş bir kuyruktan"):
        q.dequeue()

    with pytest.raises(IndexError, match="Boş bir kuyruğun"):
        q.front()


def test_recent_counter_algorithm():
    """LeetCode #933 RecentCounter zaman penceresi test senaryosu."""
    counter = RecentCounter()

    # t = 1 ms -> Pencere [-2999, 1] -> İstekler: [1] -> Sayı: 1
    assert counter.ping(1) == 1

    # t = 100 ms -> Pencere [-2900, 100] -> İstekler: [1, 100] -> Sayı: 2
    assert counter.ping(100) == 2

    # t = 3001 ms -> Pencere [1, 3001] -> İstekler: [1, 100, 3001] -> Sayı: 3
    assert counter.ping(3001) == 3

    # t = 3002 ms -> Pencere [2, 3002] -> İstek 1 elenir! -> İstekler: [100, 3001, 3002] -> Sayı: 3
    assert counter.ping(3002) == 3
