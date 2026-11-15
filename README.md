# 🧠 Python Algorithms & Data Structures Lab

Her gün bir **Veri Yapısı (Data Structure)** ve **Algoritma (LeetCode)** çözerek GitHub katkı grafiğini (streak) canlı tuttuğum, temiz kod (Clean Code) ve test güdümlü geliştirme (TDD) odaklı pratik depom.

---

## 📅 Günlük Çözüm Günlüğü (Streak Tracker)

| Gün | Konu & Kategori | Veri Yapısı / Algoritma | Zorluk | Zaman | Alan | Test |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **01** | **Stacks & Strings** | [Stack (LIFO)](data_structures/stack.py) & [Valid Parentheses (LeetCode #20)](algorithms/valid_parentheses.py) | Kolay | $O(N)$ | $O(N)$ | `11/11 PASSED` ✅ |
| **02** | **Queues & Rate Limiting** | [Queue (FIFO)](data_structures/queue.py) & [RecentCounter (LeetCode #933)](algorithms/recent_counter.py) | Kolay | $O(1)$ | $O(W)$ | `14/14 PASSED` ✅ |
| **03** | **Hash Tables & Arrays** | [Two Sum (LeetCode #1)](algorithms/two_sum.py) (Hash Map) | Kolay | $O(N)$ | $O(N)$ | `20/20 PASSED` ✅ |
| **04** | **Binary Search** | [Binary Search (LeetCode #704)](algorithms/binary_search.py) | Kolay | $O(\log N)$ | $O(1)$ | `28/28 PASSED` ✅ |
| **05** | **Greedy & Arrays** | [Best Time to Buy and Sell Stock (LeetCode #121)](algorithms/buy_sell_stock.py) | Kolay | $O(N)$ | $O(1)$ | `37/37 PASSED` ✅ |
| **06** | **Two Pointers & Strings** | [Valid Palindrome (LeetCode #125)](algorithms/valid_palindrome.py) | Kolay | $O(N)$ | $O(1)$ | `53/53 PASSED` ✅ |
| **07** | **Linked Lists** | [ListNode & LinkedList](data_structures/linked_list.py) & [Reverse Linked List (LeetCode #206)](algorithms/reverse_linked_list.py) | Kolay | $O(N)$ | $O(1)$ | `61/61 PASSED` ✅ |
| **08** | **Fast & Slow Pointers** | [Linked List Cycle (LeetCode #141)](algorithms/has_cycle.py) (Floyd's Algorithm) | Kolay | $O(N)$ | $O(1)$ | `69/69 PASSED` ✅ |
| **09** | **Linked Lists & Splice** | [Merge Two Sorted Lists (LeetCode #21)](algorithms/merge_sorted_lists.py) (Dummy Head) | Kolay | $O(N + M)$ | $O(1)$ | `76/76 PASSED` ✅ |

---

## ⚡ Gün 9: Merge Two Sorted Lists (Dummy Head & Splice)

* **Algoritma:** `algorithms/merge_sorted_lists.py`
  * Sahte baş düğüm (Dummy Head) deseniyle sınır durumları temizce yöneten ve yeni düğüm tahsis etmeden ($O(1)$ ek bellek) iki sıralı bağlı listeyi fermuar gibi birleştiren $O(N + M)$ zamanlı algoritma.
* **Görsel Rehber:** [merge_lists_rehberi.html](merge_lists_rehberi.html)

---

## 🐢🐇 Gün 8: Linked List Cycle (Floyd's Tortoise & Hare)

* **Algoritma:** `algorithms/has_cycle.py`
  * Küme (HashSet) kullanmadan $O(1)$ ek bellekle, kaplumbağa (1 adım) ve tavşan (2 adım) işaretçileriyle bağlı listedeki sonsuz döngüleri tespit eden Floyd algoritması.
* **Görsel Rehber:** [cycle_rehberi.html](cycle_rehberi.html)

---

## 🔗 Gün 7: Singly Linked List & In-Place Reversal

* **Veri Yapısı:** `data_structures/linked_list.py`
  * `ListNode[T]` ve `LinkedList[T]` sınıfları. Düğümler bellekte dağınık tutulur ve işaretçilerle birbirine bağlanır.
* **Algoritma:** `algorithms/reverse_linked_list.py`
  * `prev`, `curr`, `next_node` üçlü işaretçi mantığıyla hiçbir yeni düğüm oluşturmadan ($O(1)$ ek bellek) bağlantıları tersine çeviren $O(N)$ zamanlı in-place algoritma.
* **Görsel Rehber:** [linked_list_rehberi.html](linked_list_rehberi.html)

---

## 🪞 Gün 6: Valid Palindrome (İki İşaretçi / Two Pointers)

* **Algoritma:** `algorithms/valid_palindrome.py`
  * Ekstra bellek tahsis etmeden ($O(1)$ Space), cümlenin iki ucundan merkeze doğru ilerleyen ve noktalama işaretlerini atlayarak harfleri eşleştiren klasik İki İşaretçi (Two Pointers) yaklaşımı.
* **Görsel Rehber:** [palindrome_rehberi.html](palindrome_rehberi.html)

---

## 📈 Gün 5: Best Time to Buy and Sell Stock (Açgözlü / Tek Geçiş)

* **Algoritma:** `algorithms/buy_sell_stock.py`
  * Gelecekteki fiyatları tahmin edemediğimiz borsada, geçmişteki en dip fiyatı (`min_price`) hafızada tutarak her gün kârı hesaplayan ve tek geçişte ($O(N)$ zaman, $O(1)$ alan) maksimum kârı bulan Greedy yaklaşımı.
* **Görsel Rehber:** [stock_profit_rehberi.html](stock_profit_rehberi.html)

---

## 🎯 Gün 4: İkili Arama (Binary Search)

* **Algoritma:** `algorithms/binary_search.py`
  * Sıralı listelerde her adımda arama uzayını ikiye bölerek $O(\log N)$ logaritmik hızında arama yapan klasik Böl ve Yönet algoritması.
* **Görsel Rehber:** [binary_search_rehberi.html](binary_search_rehberi.html)

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
