# 🧠 Python Algorithms & Data Structures Lab

Her gün bir **Veri Yapısı (Data Structure)** ve **Algoritma (LeetCode)** çözerek GitHub katkı grafiğini (streak) canlı tuttuğum, temiz kod (Clean Code) ve test güdümlü geliştirme (TDD) odaklı pratik depom.

---

## 📅 Günlük Çözüm Günlüğü (Streak Tracker)

| Gün | Konu & Kategori | Veri Yapısı / Algoritma | Zorluk | Zaman | Alan | Test |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **01** | **Stacks & Strings** | [Stack (LIFO)](data_structures/stack.py) & [Valid Parentheses (LeetCode #20)](algorithms/valid_parentheses.py) | Kolay | $O(N)$ | $O(N)$ | `11/11 PASSED` ✅ |
| **02** | **Queues & Rate Limiting** | [Queue (FIFO)](data_structures/queue.py) & [RecentCounter (LeetCode #933)](algorithms/recent_counter.py) | Kolay | $O(1)$ | $O(W)$ | `14/14 PASSED` ✅ |
| **03** | **Hash Tables & Arrays** | [Two Sum (LeetCode #1)](algorithms/two_sum.py) (Hash Map) | Kolay | $O(N)$ | $O(N)$ | `20/20 PASSED` ✅ |

---

## 🔍 Gün 3: Two Sum & Hash Map Optimizasyonu

* **Algoritma:** `algorithms/two_sum.py`
  * İç içe iki döngülü $O(N^2)$ kaba kuvvet yaklaşımı yerine, Python sözlüğü (Hash Map) kullanarak $O(N)$ sürede tamamlayıcı sayıyı (`target - num`) arayan optimizasyon.
* **Görsel Rehber:** [two_sum_rehberi.html](two_sum_rehberi.html)

---

## 🥖 Gün 2: Queue (Kuyruk) & İstek Sayacı

* **Veri Yapısı:** `data_structures/queue.py`
  * Generic `Queue[T]` sınıfı (`collections.deque` optimizasyonuyla).
  * `enqueue()`, `dequeue()`, `front()`, `is_empty()`, `size()` operasyonlarının tümü **$O(1)$** sürede çalışır.
* **Algoritma:** `algorithms/recent_counter.py`
  * Son 3000 ms zaman aralığındaki istekleri takip eden, süresi dolanları baştan temizleyen kuyruk algoritması.
* **Görsel Rehber:** [queue_rehberi.html](queue_rehberi.html)

---

## 🥞 Gün 1: Stack (Yığın) & Dengeli Parantezler

* **Veri Yapısı:** `data_structures/stack.py`
  * Generic `Stack[T]` sınıfı.
  * `push()`, `pop()`, `peek()`, `is_empty()`, `size()` operasyonlarının tümü **$O(1)$** sürede çalışır.
* **Algoritma:** `algorithms/valid_parentheses.py`
  * Açılış parantezleri yığına eklenir; her kapanışta tepedeki parantezle eşleşme kontrol edilir.
* **Görsel Rehber:** [stack_ve_algoritma_rehberi.html](stack_ve_algoritma_rehberi.html)

---

## 🧪 Testleri Çalıştırma

Tüm veri yapıları ve algoritmalar `pytest` ile test edilmiştir:

```bash
# Sanal ortamı aktif et
source .venv/bin/activate

# Testleri koş
pytest -v
```

---

*Geliştirici:* **Sinem Durmaz** &bull; [GitHub](https://github.com/sinemdurmaz)
