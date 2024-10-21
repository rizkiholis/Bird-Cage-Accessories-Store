TEMA : TOKO AKSESORIS GANTUNGAN SANGKAR BURUNG

Ini adalah capstone project yang berfokus pada produk aksesoris gantungan sangkar burung dari Toko VSB. 
proyek ini dibuat menggunakan python dengan menggunakan sistem CRUD yang bertujuan untuk mengelola data produk dengan kategori yang berbeda-beda

TOKO AKSESORIS GANTUNGAN SANGKAR BURUNG merupakan konsep yang sangat menarik, terutama untuk mereka yang memiliki minat dalam dunia perburungan,
banyak pemilik burung peliharaan yang mencari aksesoris-aksesoris yang bagus untuk meningkatkan kenyamanan dan keindahan sangkar burung mereka,
proyek ini memungkinkan saya untuk mengeksplorasi cara menciptakan solusi yang relevan bagi mereka yang memiliki minat dalam dunia perburungan,
dengan adanya teknologi yang semakin canggih dan platform digital yang sudah mendunia, maka kesempatan untuk mengembangkan platform e-commerce menjadi lebih mudah.

alasan saya memilih tema toko, karena toko ini memiliki 2 akses, yaitu data yang di akses oleh admin dan data yang hanya bisa di akses oleh pengguna biasa yang hanya memiliki fitur tertentu (berbeda dengan fitur admin), hal ini menjadi tantangan bagi saya karena saya harus memahami lebih dalam tentang pengelolaan data dan interaksi dengan pengguna meskipun ini hanya dalam konteks simulasi.

Saya membuat dua fitur : 1.ADMIN , 2.PENGGUNA BIASA

Sebelum masuk ke program, seseorang akan diminta untuk login terlebih dahulu 
1.Login sebagai ADMIN (username dan password admin hanya memiliki 1 akun , hal ini bertujuan agar kondusif dalam melakukan sesuatu)

2.Login sebagai PENGGUNA BIASA (jika pengguna belum punya akun untuk masuk, maka disediakan menu daftar akun agar bisa masuk ke aplikasi)

berikut fitur fitur yang bisa di akses oleh ADMIN

1.Menu menampilkan daftar barang (read_menu)
menampilkan semua barang : (menampilkan semua barang yang ada di daftar barang)
menampilkan data berdasarkan id barang : (menampilkan data yang ingin ditampilkan berdasarkan id barang yang di masukan oleh admin)

2.Menu penambahan data barang (create_menu) :(jika admin ingin menambahkan barang baru , yang mana menambah barang ini diawali dengan memasukan id barang terlebih                                                   dahulu,jika id barang sudah ada maka id tersebut tidak bisa digunakan , jika sebaliknya maka id barang dapat digunakan.                                                jika id barang dapat digunakan maka admin diminta untuk mengisi data data untuk ditampilkan di daftar barang.)

3.Menu pengubahan data barang (update_menu) : (jika admin ingin merubah sesuatu yang ada di daftar barang seperti harga/stok dan lain lain, yang mana pengubahan data                                                 ini akan di awali dengan memasukan id barang yang bertujuan untuk menampilkan data sesuai id barang , jika id barang                                                   tersedia maka admin bisa merubahnya dengan memilih kolom manakah yang akan di ubah) 

4.Menu penghapusan data barang (delete_menu) : (jika admin ingin menghapus salah satu data karena sudah tidak produksi lagi , maka penghapusan data ini akan dilakukan                                                 sesuai id barang yang ingin di hapus, admin akan diminta untuk menghapus id barang yang mana yang ingin di hapus,                                                       ketika sudah pilih id mana yang akan di hapus maka item tersebut akan terhapus)

berikut fitur fitur yang bisa di akses oleh PENGGUNA BIASA 

1.Menu menampilkan daftar barang (read_menu) : (ini sama halnya seperti (read_menu)admin )
menampilkan semua barang 
menampilkan berdasarkan data barang 

2.Membeli barang : (pengguna bisa membeli suatu barang yang ada di daftar barang berdasarkan id barang yang ingin di beli , dan nanti pengguna akan di minta memilih                       barang mana yang akan di beli , dan berapa jumlah yang ingin dibeli tapi ketika jumlahnya melebihi stok yang ada di daftar_barang maka akan muncul                     pemberitahuan bahwa stok tidak cukup, ketika jumlah yang di masukan tidak lebih dari stok yang ada di daftar_barang, maka akan melanjutkan ke sesi                     pembayaran)

Sekian penjelasan mengenai project yang sudah saya kerjakan 
TERIMA KASIH

Note:
untuk mengakses akun admin 
username= 'admin' 
password= 'admin123'
