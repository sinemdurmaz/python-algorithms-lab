# 🧠 Python Algorithms & Data Structures Lab

Her gün bir **Veri Yapısı (Data Structure)** ve **Algoritma (LeetCode)** çözerek GitHub katkı grafiğini (streak) canlı tuttuğum, temiz kod (Clean Code) ve test güdümlü geliştirme (TDD) odaklı pratik depom.

---

## 📅 Günlük Çözüm Günlüğü (Streak Tracker)

| Gün | Konu & Kategori | Veri Yapısı / Algoritma | Zorluk | Zaman | Alan | Test |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **01** | **Stacks & Strings** | [Stack (LIFO)](data_structures/stack.py) & [Valid Parentheses (LeetCode #20)](algorithms/valid_parentheses.py) | Kolay | $O(N)$ | $O(N)$ | `11/11 PASSED` ✅ |

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
