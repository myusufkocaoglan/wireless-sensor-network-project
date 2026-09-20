# 🗑️ Smart Waste Monitoring System with Wireless Sensor Networks

[🇹🇷 Türkçe](#-türkçe) | [🇬🇧 English](#-english)

---

# 🇹🇷 Türkçe

## 📌 Proje Hakkında

Bu proje, **Kablosuz Sensör Ağları (Wireless Sensor Networks - WSN)** kullanılarak akıllı çöp konteynerlerinin durumlarının izlenmesini simüle eden bir sistemdir.

Sistem, konteynerlerden alınan **ağırlık** ve **sıcaklık** verilerini değerlendirerek konteynerlerin mevcut durumunu belirler. Elde edilen sonuçlar **ROS Noetic** altyapısı kullanılarak işlenir ve **RViz** üzerinde görselleştirilir.

Projenin temel amacı, sensör tabanlı akıllı atık yönetimi sistemlerinin çalışma mantığını simüle etmek ve farklı sensör verilerinin merkezi bir sistem üzerinde nasıl değerlendirilebileceğini göstermektir.

## 🎯 Projenin Amaçları

* Kablosuz sensör ağlarının akıllı şehir uygulamalarındaki kullanımını incelemek
* Çöp konteynerlerinin doluluk durumunu sensör verileriyle takip etmek
* Sıcaklık verileri üzerinden olası yangın risklerini tespit etmek
* Sensör verilerini ROS ortamında işlemek
* Konteynerlerin durumlarını RViz üzerinde görselleştirmek
* Daha verimli atık toplama sistemleri için temel bir simülasyon oluşturmak

## ⚙️ Sistem Çalışma Mantığı

Sistem, konteynerlerden gelen sensör verilerini değerlendirerek her konteyner için bir durum belirler.

| Durum       | Açıklama                                                 |
| ----------- | -------------------------------------------------------- |
| `NORMAL`    | Konteyner normal çalışma koşullarındadır.                |
| `FULL`      | Konteynerin doluluk seviyesi belirlenen sınırı aşmıştır. |
| `FIRE_RISK` | Sıcaklık değeri olası yangın riskine işaret etmektedir.  |

Bu durumlar ROS üzerinden işlenerek RViz ortamında görsel olarak takip edilebilir.

## 🛠️ Kullanılan Teknolojiler

* **Python**
* **ROS Noetic**
* **RViz**
* **Ubuntu**
* **Wireless Sensor Networks (WSN)**
* **Sensor Data Simulation**

## 📡 Kullanılan Sensör Verileri

### Ağırlık Sensörü

Konteyner içerisindeki atık miktarını tahmin etmek ve konteynerin doluluk durumunu belirlemek için kullanılır.

### Sıcaklık Sensörü

Konteyner içerisindeki sıcaklık değişimlerini takip etmek ve olağan dışı sıcaklık seviyelerinde potansiyel yangın riskini belirlemek için kullanılır.

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler

Projeyi çalıştırmak için aşağıdaki ortamın hazır olması gerekir:

* Ubuntu
* ROS Noetic
* Python
* RViz

ROS çalışma alanınızı oluşturduktan sonra projeyi ilgili `src` dizinine klonlayabilirsiniz:

```bash
cd ~/catkin_ws/src
git clone https://github.com/myusufkocaoglan/wireless-sensor-network-project.git
```

Ardından çalışma alanını derleyin:

```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

ROS master'ı başlatın:

```bash
roscore
```

Daha sonra proje içerisindeki ilgili ROS node'larını çalıştırarak sensör simülasyonunu başlatabilirsiniz.

RViz'i açmak için:

```bash
rviz
```

## 🌐 Kullanım Alanları

Bu sistemin temel yaklaşımı aşağıdaki alanlarda kullanılabilir:

* Akıllı şehir sistemleri
* Akıllı atık yönetimi
* Çöp toplama rotalarının optimizasyonu
* Uzaktan konteyner takibi
* Yangın riskinin erken tespiti
* IoT ve sensör ağı uygulamaları

## 👨‍💻 Geliştirici

**Muhammed Yusuf Kocaoğlan**

Computer Engineer

---

# 🇬🇧 English

## 📌 About the Project

This project simulates a **smart waste monitoring system based on Wireless Sensor Networks (WSN)**.

The system evaluates **weight** and **temperature** sensor data collected from waste containers to determine their current status. The sensor data is processed using **ROS Noetic**, while the status of the containers can be visualized through **RViz**.

The main purpose of the project is to demonstrate the fundamental architecture of a sensor-based smart waste management system and show how different sensor measurements can be processed within a centralized monitoring environment.

## 🎯 Project Objectives

* Explore the use of Wireless Sensor Networks in smart city applications
* Monitor waste container fill levels using sensor data
* Detect potential fire risks based on temperature measurements
* Process sensor data within the ROS environment
* Visualize container status using RViz
* Create a basic simulation for more efficient waste collection systems

## ⚙️ How the System Works

The system evaluates incoming sensor measurements and assigns a status to each waste container.

| Status      | Description                                               |
| ----------- | --------------------------------------------------------- |
| `NORMAL`    | The container is operating under normal conditions.       |
| `FULL`      | The container has exceeded the defined fill threshold.    |
| `FIRE_RISK` | The measured temperature indicates a potential fire risk. |

These states are processed through ROS and can be monitored visually using RViz.

## 🛠️ Technologies Used

* **Python**
* **ROS Noetic**
* **RViz**
* **Ubuntu**
* **Wireless Sensor Networks (WSN)**
* **Sensor Data Simulation**

## 📡 Sensor Data

### Weight Sensor

Used to estimate the amount of waste inside the container and determine its fill status.

### Temperature Sensor

Used to monitor temperature changes inside the container and identify unusually high temperatures that may indicate a potential fire risk.

## 🚀 Installation and Usage

### Requirements

The following environment is required to run the project:

* Ubuntu
* ROS Noetic
* Python
* RViz

Clone the repository into the `src` directory of your ROS workspace:

```bash
cd ~/catkin_ws/src
git clone https://github.com/myusufkocaoglan/wireless-sensor-network-project.git
```

Build the workspace:

```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

Start ROS Master:

```bash
roscore
```

Then run the relevant ROS nodes included in the project to start the sensor simulation.

Launch RViz with:

```bash
rviz
```

## 🌐 Potential Applications

The fundamental approach demonstrated in this project can be applied to:

* Smart city systems
* Smart waste management
* Waste collection route optimization
* Remote container monitoring
* Early fire-risk detection
* IoT and sensor network applications

## 👨‍💻 Developer

**Muhammed Yusuf Kocaoğlan**

Computer Engineer

---

## 📄 License

This project was developed for educational and academic purposes.
