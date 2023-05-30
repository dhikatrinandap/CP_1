   # **Capstone Project Modul 1**

   **Python**

Capstone project yang dilakukan ini merupakan pengaplikasian atas pemebelajaran pada modul 1. Pembelajaran pada modul 1 mengenai program/aplikasi Python. Selama proses pemebalajaran dikenalkan hal-hal dasar mengenai pengoperasian program tersebut. 

Mengenai capstone project ini yaitu membuat program sederhana dengan bertemakan data penjualan suatu toko dimana dalam proses pengaplikasiannya bisa melakukan Create, Read, Update, dan Delete atau biasa disingkat dengan nama CRUD. 

[![G1.jpg](https://i.postimg.cc/4Nj4rVCY/G1.jpg)](https://postimg.cc/nCYtmshx)

User pengguna program sederhana ini bisa memilih user sebagai penjual atau sebagai pembeli. Jika user sebagai penjual bisa melakukan CRUD itu sendiri

[![G2.jpg](https://i.postimg.cc/7LGWjJkZ/G2.jpg)](https://postimg.cc/R3mdHFhk)

- Create (Menambah barang)

[![G5.jpg](https://i.postimg.cc/g2dhfCbX/G5.jpg)](https://postimg.cc/sv61W0Xs)

User sebagai penjual bisa menambahkan barang baru dan harus di isi lengkap mulai dari kode barang, nama barang, stok barang, harga satuan barang, dan nama sales barang.

- Read (Membaca/menampilkan barang)

[![G4.jpg](https://i.postimg.cc/Gm7pqVL1/G4.jpg)](https://postimg.cc/sMWy2nGn)

Bisa menampikan keseluruhan data barang yang dimiliki atau bisa juga menampilkan data suatu barang dengan memasukan primary key (kode barang). Sehingga barang yang ditampilkan akan keluar sesuai dengan input kode barang yang dimasukan oleh user.

- Update (Mengubah barang)

[![G6.jpg](https://i.postimg.cc/Qdw3B3NV/G6.jpg)](https://postimg.cc/CRGtt9qV)

User sebagai penjual bisa mengubah suatu barang yang sudah ada mulai dari nama barang, stok barang, harga satuan barang, dan nama sales. Kecuali kode barang tidak bisa diubah, karena kode barang merupakan kode yang memiliki karakteristik unik (yang hanya dimiliki sendiri).

- Delete (Menhapus barang)

[![G7.jpg](https://i.postimg.cc/MZ5J7RZC/G7.jpg)](https://postimg.cc/6T8Pw8vc)

User sebagai penjual bisa menghapus suatu barang dengan memasukan primary key (kode barang) sehingga nama barang, stok barang, harga satuan barang serta nama sales akan langsung terhapus semua.

Dari keempat fitur ini saling berkesinambungan, misalkan saat user menambah, mengubah, atau menghapus dapat di read atau dibaca dan menampilkan daftar barang keseluruhan yang terbaru. Kemudian jika user sebagai pembeli hanya bisa melihat daftar barang keseluruhan dan dapat melakukan pembelian:

[![G3.jpg](https://i.postimg.cc/QC4zRQHV/G3.jpg)](https://postimg.cc/RJtGtn1z)

- Read (Membaca/menampilkan barang)
Sama seperti user sebagai penjual, user sebagai pembeli juga bisa meilhat daftar tampilan barang keseluruhan.

- Purchase (Pembelian barang)
User sebagai pembeli bisa melakukan pembelian dengan menginput kode barang, jumlah barang yang ingin dibeli. Kemudian aka nada konfirmasi berupa jumlah barang yang akan dibeli dan total harga pembelian. Lalu untuk melanjutkan transaksi pembayaran user memasukan sejumlah uang uang, jika uang yang diinput lebih maka akan ada konfirmasi berupa uang kembali. Namun jika uang yang diinput kurang dari total yang ditagihkan maka transaksi otomatis dibatalkan.

