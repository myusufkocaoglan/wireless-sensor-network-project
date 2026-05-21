Akıllı Çöp Konteyneri İçin ROS Tabanlı Kablosuz Algılayıcı Ağ Simülasyonu

Proje Açıklaması

Bu proje, Kablosuz Algılayıcı Ağlar (Wireless Sensor Networks - WSN) dersi kapsamında geliştirilmiştir.

Projede, çöp konteynerlerinin doluluk durumu ve yangın riskinin izlenmesi amacıyla ROS tabanlı bir kablosuz sensör ağı simülasyonu gerçekleştirilmiştir.

Her konteyner bir sensör node’u olarak çalışmaktadır. Node’lar sıcaklık ve ağırlık verilerini üretmekte ve ROS topic’leri üzerinden yayınlamaktadır. RViz ortamında konteyner durumu gerçek zamanlı olarak görselleştirilmektedir.

---

Kullanılan Teknolojiler

- Ubuntu 20.04
- ROS Noetic
- RViz
- Python
- std_msgs
- visualization_msgs

---

Sistem Mimarisi

```text
Sensör Node'u
      ↓
ROS Topic Yayını
      ↓
RViz Marker Node
      ↓
RViz Görselleştirme
```

---

Sensör Mantığı

Simülasyonda aşağıdaki sensör verileri üretilmektedir:

- Ağırlık Sensörü
- Sıcaklık Sensörü

Üretilen verilere göre konteyner durumu belirlenmektedir.

---

Durumlar

| Durum | Açıklama |
|---|---|
| NORMAL | Normal çalışma |
| FULL | Konteyner dolu |
| FIRE_RISK | Yangın riski |

---

RViz Görselleştirme

RViz ortamında konteyner durumu renkli marker ile gösterilmektedir.

- Yeşil → Normal
- Sarı → Dolu
- Kırmızı → Yangın Riski

---

ROS Topic Yapısı

```text
/bin1/data
/visualization_marker
```

---

Çalıştırma Adımları

Terminal 1

```bash
roscore
```

---

Terminal 2

```bash
source ~/catkin_ws/devel/setup.bash
rosrun smart_bin_wsn bin_node.py
```

---

Terminal 3

```bash
source ~/catkin_ws/devel/setup.bash
rosrun smart_bin_wsn rviz_node.py
```

---

Terminal 4

```bash
rviz
```

RViz içinde:

- Fixed Frame → `map`
- Add → Marker
- Topic → `/visualization_marker`

---

Simülasyon Çıktıları

Sistem rastgele sıcaklık ve ağırlık verileri üretmektedir.

Örnek çıktı:

```text
BIN_ID:1 | Weight:85kg | Temp:31C | Status:NORMAL
```

```text
BIN_ID:1 | Weight:115kg | Temp:45C | Status:FULL
```

```text
BIN_ID:1 | Weight:72kg | Temp:61C | Status:FIRE_RISK
```

---

Proje Amacı

Bu projede amaç:

- Akıllı şehir uygulamaları geliştirmek
- Çöp toplama süreçlerini optimize etmek
- Yangın riskini erken tespit etmek
- Kablosuz algılayıcı ağ mantığını ROS ortamında simüle etmektir.
