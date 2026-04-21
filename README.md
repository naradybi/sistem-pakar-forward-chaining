# Sistem Pakar Diagnosis Penyakit Kulit (Forward Chaining)
Program ini merupakan implementasi sistem pakar untuk mendiagnosis penyakit kulit menggunakan metode forward chaining berbasis Python.

## 📌 Deskripsi
Sistem ini membantu pengguna dalam melakukan diagnosis awal penyakit kulit berdasarkan gejala yang dialami. Penyakit kulit sering memiliki gejala yang mirip, sehingga sulit dibedakan tanpa pengetahuan medis.

Sistem pakar ini menggunakan aturan IF–THEN untuk merepresentasikan pengetahuan dan menghasilkan diagnosis secara otomatis.

## ▶️ Jalankan Online
Program juga dapat dijalankan langsung melalui Google Colab:
https://colab.research.google.com/drive/1ersLzxJfveLw4puJBDXJHOaki7SynTOs?usp=sharing

## 🧠 Metode
Metode yang digunakan adalah forward chaining, yaitu proses inferensi yang dimulai dari fakta (gejala) menuju kesimpulan (diagnosis penyakit).

## 📊 Knowledge Base

### Data Penyakit
P1: Alergi  
P2: Bisul  
P3: Cacar Air  
P4: Jerawat  
P5: Kudis  
P6: Keloid  
P7: Campak  
P8: Sariawan  
P9: Ketombe  

### Data Gejala
G1: Kulit berbintil  
G2: Kulit kemerahan  
G3: Rasa gatal  
G4: Rasa nyeri  
G5: Demam  
G6: Pembengkakan kulit  
G7: Kulit pengelupas  
G8: Benjolan di kulit  
G9: Mata merah  
G10: Kulit kepala berminyak  
G11: Luka di bagian mulut  

### Aturan IF–THEN
R1: G1 AND G2 AND G3 → P1  
R2: G1 AND G4 AND G5 → P2  
R3: G1 AND G3 AND G5 → P3  
R4: G1 AND G2 → P4  
R5: G1 AND G3 AND G7 → P5  
R6: G3 AND G8 → P6  
R7: G5 AND G9 AND G11 → P7  
R8: G6 AND G11 → P8  
R9: G3 AND G10 → P9  

## ⚙️ Cara Penggunaan
1. Jalankan program Python  
2. Masukkan gejala (contoh: G1,G3,G5)  
3. Sistem akan menampilkan proses dan hasil diagnosis  

## ▶️ Jalankan Online
Program juga dapat dijalankan langsung melalui Google Colab:
https://colab.research.google.com/drive/1ersLzxJfveLw4puJBDXJHOaki7SynTOs?usp=sharing

## 💻 Teknologi
- Python

## 📚 Referensi
Siahaan, R. D. (2024). Sistem Pakar Diagnosis Penyakit Kulit Menggunakan Metode Forward Chaining dengan Python.  
https://journal.eng.unila.ac.id/index.php/jitet/article/view/5088/2089  

Zulkhairani. (2024). Sistem Pakar Mendeteksi Penyakit Kulit Menggunakan Metode Forward Chaining di RS HAMS Kisaran.  
https://jurnal.polgan.ac.id/index.php/jmp/article/view/14287/2906  
