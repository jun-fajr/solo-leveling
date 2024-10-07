# Sistem Penentuan Tingkat Kemahiran Maksimal Juned

Proyek ini adalah program Python yang bertujuan untuk menentukan tingkat kemahiran maksimal Juned dalam sebuah pertandingan olahraga dengan melawan lawan-lawan yang memiliki tingkat kemahiran tertentu. Program ini akan menghitung kemahiran Juned berdasarkan lawan yang dikalahkan dan peningkatan yang didapat setelah setiap kemenangan.

## Deskripsi

Juned diberikan kesempatan untuk melawan beberapa lawan dengan tingkat kemahiran yang berbeda. Setelah mengalahkan setiap lawan, tingkat kemahiran Juned akan meningkat. Juned hanya bisa melawan lawan yang memiliki tingkat kemahiran yang lebih rendah atau sama dengan tingkat kemahirannya saat ini. Tujuannya adalah untuk menentukan urutan lawan yang harus dilawan untuk memaksimalkan tingkat kemahiran Juned.

## Fitur

- Input jumlah lawan dan tingkat kemahiran awal Juned.
- Input tingkat kemahiran lawan (Ai) dan peningkatan kemahiran (Bi) setelah mengalahkan setiap lawan.
- Output tingkat kemahiran maksimal Juned setelah mengalahkan lawan-lawan tersebut.

## Instalasi

1. Pastikan Anda memiliki Python 3.10.11 terinstal di komputer Anda.
2. Clone repositori ini:
   ```bash
   git clone https://github.com/jun-fajr/solo-leveling.git
   ```
3. Arahkan ke direktori proyek:
   ```bash
   cd solo-leveling
   ```

## Cara Menggunakan

1. Jalankan program dengan perintah berikut:

   ```bash
   python main.py
   ```

   atau

   ```bash
   python main2.py
   ```

2. Ikuti petunjuk untuk memasukkan input:

   - Masukkan jumlah lawan (`N`).
   - Masukkan tingkat kemahiran awal Juned (`M`).
   - Masukkan tingkat kemahiran masing-masing lawan (`Ai`).
   - Masukkan peningkatan kemahiran setelah mengalahkan lawan (`Bi`).

3. Program akan menampilkan tingkat kemahiran maksimal yang dapat dicapai Juned.

## Contoh Input dan Output

**Contoh Input 1 (main.py):**

```
Masukkan N dan M: 4 2
Masukkan Ai (tingkat kemahiran lawan): 8 9 3 2
Masukkan Bi (penambahan kemahiran setelah menang): 5 4 1 3
```

**Output main.py:**

```
Tingkat kemahiran maksimal: 6
```

**Contoh Input 2 (main2.py):**

```
Masukkan N: 4
Masukkan M: 2
Masukkan Ai (tingkat kemahiran lawan) untuk lawan ke-1: 8
Masukkan Ai (tingkat kemahiran lawan) untuk lawan ke-2: 9
Masukkan Ai (tingkat kemahiran lawan) untuk lawan ke-3: 3
Masukkan Ai (tingkat kemahiran lawan) untuk lawan ke-4: 2
Masukkan Bi (penambahan kemahiran setelah menang) untuk lawan ke-1: 5
Masukkan Bi (penambahan kemahiran setelah menang) untuk lawan ke-2: 4
Masukkan Bi (penambahan kemahiran setelah menang) untuk lawan ke-3: 1
Masukkan Bi (penambahan kemahiran setelah menang) untuk lawan ke-4: 3
```

**Output main2.py:**

```
Tingkat kemahiran maksimal: 6
```

## Penulis

Nama: Junizar Fajri
Email: jun.fajr@gmail.com

## Lisensi

Proyek ini dilisensikan di bawah Custom License
