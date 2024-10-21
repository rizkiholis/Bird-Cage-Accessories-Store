from tabulate import tabulate

daftar_barang= [   
    [101,"Mur Topi ","Alumunium",0.6,90,150],
    [102,"Mur Kuping ","Plat Besi",1.2,50,300],
    [103,"Lonceng ","Plat Besi",0.4,100,200],
    [104,"Mangkok Kembang","Plat Kaleng",0.2,95,150],
    [105,"Mangkok Bulat ","Plat Kaleng",0.2,80,175]
]


daftar_akun = [ 
    {"username" : "baru",
     "password" : "lama123"}
    ]

def akses_login():
        print()
        print(f"{"=" *30}")
        print("  Selamat datang di toko VSB ")
        print(f"{"=" *30}")
        print("Silahkan untuk memilih opsi login")
        print("1.Masuk sebagai admin")
        print("2.Masuk sebagai pengguna biasa")
        print("3.Exit")

def login_user():
    while True:
        print("\nSilahkan Login")
        print("1. Masuk (jika sudah punya akun)")
        print("2. Daftar (jika belum punya akun)")
        try:
            pilihan = int(input("Masukan angka yang ingin di akses: "))
        except:
            print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
            continue

        if pilihan == 1 :
            print("Login")
            username = input("Masukan username: ") # baru
            password = input("Masukan password: ")
            loginstatus = False
            for akun in daftar_akun:
                if akun.get("username" ) == username and akun.get("password") == password:
                    print("\t>>>Login sukses.<<<")
                    loginstatus = True
                    return main_menu_user()
                    
            if loginstatus == False :
                print("<<< Username atau password salah.>>>")  

        elif pilihan == 2 :
            username = input("Masukan id baru: ")
            password = input("Masukan password baru: ")

            simpan_akun = {"username" : username ,"password" : password }

            daftar_akun.append(simpan_akun)
            print(daftar_akun)
            print("Pembuatan akun sukses")
            continue
            
def user_beli():
    print()
    keranjang = []
    total_harga = 0
    while True:
    
        if daftar_barang:               
            headers = ["ID Barang","Nama","Bahan (Material)","Ukuran(mm)","Stok (Jumlah)","Harga (Satuan)"]
            align = ["center","left","left","center","center","center"]
            table = tabulate(daftar_barang, headers, tablefmt="mixed_grid",colalign=align)
            print(table)
        else:
            print("\n=== Data Tidak Tersedia.===")
            return main_menu_user()        
        id_buy = int(input("Masukan ID barang yang ingin di beli: "))
             
        id_barang = False
        for item in daftar_barang:
            if item[0] == id_buy:
                id_barang = True
                barang_terpilih = item
                break #keluar dari loop jika barang sudah ketemu
        if id_barang == False :
            print("\n<<< ID Barang tidak ditemukan.>>>")
            continue # kembali ke awal loop

        while True:               
            jumlah = int(input("Masukan jumlah yang ingin di beli: "))
            if jumlah > barang_terpilih[4]:
                print(f"jumlah yang anda masukan terlalu banyak stok tersisa {barang_terpilih[4]}")
                continue
            else:
                break

        keranjang.append([barang_terpilih[1], jumlah, int(barang_terpilih[5]), jumlah * int(barang_terpilih[5])])
        total_harga += jumlah *(barang_terpilih[5])
        barang_terpilih[4] -= jumlah 

        if keranjang:
            print("\n=== Keranjang Belanja Anda ===")
            headers = ["Nama Barang", "Jumlah", "Harga Satuan", "Total Harga"]
            table = tabulate(keranjang, headers, tablefmt="mixed_grid")
            print(table)
            print(f"\nTotal Harga Semua Barang: {total_harga}\n")
        else:
            print("Keranjang belanja kosong.")
               
        while True:
            uang_user = int(input("Masukkan uang Anda: "))
            if uang_user >= total_harga:
                kembalian = uang_user - total_harga
                print(f"Pembayaran berhasil! Kembalian Anda: {kembalian}\n")
                break
            else:
                print(f"Uang Anda kurang, total yang harus dibayar: {total_harga}. Coba lagi.\n")
                continue

        return main_menu_user()

def main_menu_user():
    while True:
        print(f'''       
{"=" *30}
\t  Main menu
{"=" *30}
1. Menampilkan daftar barang
2. Membeli barang
3. kembali ke menu''')

        try:
            pilihan = int(input("Masukkan angka di pilihan main menu yang ingin di tampilkan: "))
        except:
            print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***") 
            continue
            
        if pilihan == 1:
            return read_menu_user()
        elif pilihan == 2:
            return user_beli()
        elif pilihan == 3 :
            break

def read_menu_user():
    while True :
        print("\nRead menu")
        print("1.Tampilkan seluruh data barang")
        print("2.Tampilkan data berdasarkan ID barang")
        print("3.Kembali ke main menu")
        try:
            pilihan = int(input("Masukkan angka di pilihan main menu yang ingin di tampilkan: "))
        except:
            print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
            continue 

        if pilihan == 1:
            print()
            if daftar_barang:                
                headers = ["ID Barang","Nama","Bahan (Material)","Ukuran(mm)","Stok (Jumlah)","Harga (Satuan)"]
                align = ["center","left","left","center","center","center"]
                table = tabulate(daftar_barang, headers, tablefmt="mixed_grid",colalign=align)
                print(table)
            else:
                print("\n=== Data Tidak Tersedia.===")

        elif pilihan == 2:
            if daftar_barang:
                try:
                    kunci = int(input("Masukan ID barang yang ingin ditampilkan: "))
                except:
                    print("\n*** Pilihan tidak valid! Mohon masukan ID barang yang benar.***")
                    continue
            
                id_ditemukan = False  # Inisialisasi variabel data_ditemukan

                for item in daftar_barang:
                    if item[0] == kunci:
                        print("\n===== Detail Barang =====")
                        print(f"ID     : {item[0]}")
                        print(f"Nama   : {item[1]}")
                        print(f"Bahan  : {item[2]}")
                        print(f"Ukuran : {item[3]}")
                        print(f"Stok   : {item[4]}")
                        print(f"Harga  : {item[5]}")
                        print("=========================")
                        id_ditemukan = True
                    
                if id_ditemukan == False :
                    print("\n~~~ ID barang Tidak Ditemukan.~~~")
            else:
                print("\n=== Data Tidak Ditemukan.===")
        elif pilihan == 3 :
            return main_menu_user()
        else:
            print("\n=== Pilihan tidak valid! Mohon masukan dengan angka yg tersedia.===")
            continue

def login_admin():
    while True:
        username = input("masukan username: ")
        password = input("masukan password: ")
        if username == "admin" and password == 'admin123':
            print("\n>>> Login sebagai admin sukses.<<<")
            return main_menu_admin()           
        else:
            print("\n<<< Username atau Password yang anda masukan salah.>>>")
            continue
     
def main_menu_admin():

    while True:
        print(f'''       
{"=" *30}
\t  Main menu
{"=" *30}
1. Menampilkan daftar barang
2. Menambah barang
3. Mengubah barang
4. Menghapus barang
5. Kembali ke menu login''')
        try:
            pilihan = int(input("Masukkan angka di pilihan main menu yang ingin di tampilkan: "))
        except:
            print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***") 
            continue
            
        if pilihan == 1:
            return read_menu_admin()
        elif pilihan == 2:
            return create_menu()
        elif pilihan == 3:
            return update_menu()
        elif pilihan == 4:
            return delete_menu()
        elif pilihan == 5:
            break
            
        else:
            print('''\n=== Pilihan tidak valid! Angka yang anda masukan tidak ada di main menu,
Mohon masukan angka yang ada main menu.===''')

def read_menu_admin():
    while True :
        print("\nRead menu")
        print("1.Tampilkan seluruh data barang")
        print("2.Tampilkan data berdasarkan ID barang")
        print("3.Kembali ke main menu")
        try:
            pilihan = int(input("Masukkan angka di pilihan main menu yang ingin di tampilkan: "))
        except:
            print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
            continue 

        if pilihan == 1:
            print()
            if daftar_barang:
                
                headers = ["ID Barang","Nama","Bahan (Material)","Ukuran(mm)","Stok (Jumlah)","Harga (Satuan)"]
                align = ["center","left","left","center","center","center"]
                table = tabulate(daftar_barang, headers, tablefmt="mixed_grid",colalign=align)
                print(table)
            else:
                print("\n=== Data Tidak Tersedia.===")

        elif pilihan == 2:
            if daftar_barang:
                try:
                    kunci = int(input("Masukan ID barang yang ingin ditampilkan: "))
                except:
                    print("\n*** Pilihan tidak valid! Mohon masukan ID barang yang benar.***")
                    continue
            
                id_ditemukan = False  # Inisialisasi variabel data_ditemukan

                for item in daftar_barang:
                    if item[0] == kunci:
                        print("\n===== Detail Barang =====")
                        print(f"ID     : {item[0]}")
                        print(f"Nama   : {item[1]}")
                        print(f"Bahan  : {item[2]}")
                        print(f"Ukuran : {item[3]}")
                        print(f"Stok   : {item[4]}")
                        print(f"Harga  : {item[5]}")
                        print("=========================")
                        id_ditemukan = True
                    
                if id_ditemukan == False:
                    print("\n~~~ ID barang Tidak Ditemukan.~~~")
            else:
                print("\n=== Data Tidak Ditemukan.===")
           
        elif pilihan == 3:
            return main_menu_admin()
        else:
            print("\n=== Pilihan tidak valid! Mohon masukan dengan angka yg tersedia.===")
            continue

def create_menu():
    while True:
        print("\nMenu penambahan barang")
        print("1.Menambah barang baru")
        print("2.Kembali ke main menu")
        try:
            pilih = int(input("Masukan angka di pilihan main menu yang ingin ditampilkan: "))
        except:
            print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
            continue
        
        if pilih == 1 :
            try:
                kunci = int(input("Masukan ID barang: "))
            except:
                print("\n*** Pilihan tidak valid! Mohon untuk masukan ID barang dengan benar.***")
                continue

            id_ditemukan = False
            for item in daftar_barang:
                if item[0] == kunci:
                    print("\n~~~ ID barang sudah tersedia.~~~")
                    id_ditemukan = True 
                    break #menghentikan proses jika id sudah tersedia 
                
            if id_ditemukan == False :
                # proses akan dilanjutkan jika jika id belum ditemukan
                try:
                    print("\n>>> ID barang dapat digunakan.<<<")
                    print(">>> Silahkan isi data barang dibawah ini.<<<")
                    nama = str(input("Silahkan masukkan nama produk: ")).title() 
                    bahan = str(input("Tentukan jenis bahan produk: ")).title()
                    ukuran = float(input("Masukan ukuran produk: "))
                    stok = int(input("Tentukan jumlah stok produk: "))
                    harga = int(input("Masukan harga produk: "))
                except:
                    print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
                    continue #agar user bisa mencoba lagi
                try:
                    list_sementara = [kunci,nama,bahan,ukuran,stok,harga]

                    save = input("Apakah data ingin di simpan (y/n): ").lower()
                    if save == 'y':
                        daftar_barang.append(list_sementara)
                        print("\n===== Detail Barang =====")
                        print(f"ID     : {kunci}")
                        print(f"Nama   : {nama}")
                        print(f"Bahan  : {bahan}")
                        print(f"Ukuran : {ukuran}")
                        print(f"Stok   : {stok}")
                        print(f"Harga  : {harga}")
                        print("=========================")
                        print("~~~ Data berhasil di simpan.~~~")

                    elif save == 'n':
                        print("\n<<< Penambahan data dibatalkan.>>>")
                    else:
                        print("\n=== Mohon masukan huruf y atau n.===")
                except:
                    print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
                    continue

        elif pilih == 2 :
            return main_menu_admin()
        else:
            print("\n=== Mohon masukan angka yang tersedia.===")
            continue

def update_menu():
    
    while True:
        print("\nMenu perubahan data")
        print("1.Ubah data barang")
        print("2.kembali ke main menu")
        try:
            pilih= int(input("Masukan angka di pilihan main menu yang ingin ditampilkan: "))
        except:
            print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
            continue

        if pilih == 1 :
            headers = ["ID Barang","Nama","Bahan (Material)","Ukuran(mm)","Stok (Jumlah)","Harga (Satuan)"]
            align = ["center","left","left","center","center","center"]
            table = tabulate(daftar_barang, headers, tablefmt="mixed_grid",colalign=align)
            print(table)
            try:
                kunci = int(input("Masukan ID barang yang ingin di ubah: "))
            except:
                print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
                continue
            
            id_ditemukan = False
            for item in daftar_barang:
                if item[0] == kunci:
                    print("Detail Barang")
                    data = [item]
                    headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                    align = ["center","left","left","center","center","center"]
                    table = tabulate(data, headers, tablefmt="heavy_grid",colalign=align)
                    print(table)

                    list_sementara = [item[0],item[1],item[2],item[3],item[4],item[5]]

                    id_ditemukan = True
                    ubah = input("Apakah data ini akan di ubah (y/n): ").lower()
                    if ubah == 'y':
                        kolom = input("Kolom manakah yang ingin di ubah: ").lower()
                        if kolom == 'nama':                              
                            nama = list_sementara[1]
                            print("="*25)
                            print(f"Nama   : {nama}")
                            print("="*25)
                            ubah_kolom = input("Masukan nama produk yang baru: ").title()
                            ubah_asli = input("Apakah data ini akan di ubah? (y/n): ").lower()
                            if ubah_asli == 'y':
                                nama = ubah_kolom
                                for i in daftar_barang:
                                    if i[0]== kunci:
                                        i[1] = nama 
                                        print()
                                        print("Data Sebelum di ubah")
                                        data = [list_sementara]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="fancy_grid",colalign=align)
                                        print(table)

                                        print()
                                        print("Data Setelah di ubah")
                                        data = [i]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="fancy_grid",colalign=align)
                                        print(table)

                                print(">"*35, "Perubahan data berhasil disimpan", "<"*35)
                            elif ubah_asli == 'n':
                                print("\n<<< Perubahan data dibatalkan.>>>")
                            else:
                                print("\n=== Mohon masukan dengan huruf y atau n.===")
                        elif kolom == 'bahan':
                            bahan = list_sementara[2]
                            print("="*25)
                            print(f"Bahan   : {bahan}")
                            print("="*25)
                            ubah_kolom = input("Masukan bahan produk yang baru: ").title()
                            ubah_asli = input("Apakah data ini akan di ubah? (y/n): ").lower()
                            if ubah_asli == 'y':
                                bahan = ubah_kolom
                                for i in daftar_barang:
                                    if i[0] == kunci:
                                        i[2] = bahan
                                        print()
                                        print("Data Sebelum di ubah")
                                        data = [list_sementara]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="simple_grid",colalign=align)
                                        print(table)

                                        print()
                                        print("Data Setelah di ubah")
                                        data = [i]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="simple_grid",colalign=align)
                                        print(table)

                                print(">"*35, "Perubahan data berhasil disimpan", "<"*35)
                            elif ubah_asli == 'n':
                                print("\n<<< Perubahan data dibatalkan.>>>")
                            else:
                                print("\n=== Mohon masukan dengan huruf y atau n.===")
                        elif kolom == 'ukuran':
                            ukuran = list_sementara[3]
                            print("="*25)
                            print(f"Ukuran   : {ukuran}")
                            print("="*25)
                            ubah_kolom = float(input("Masukan ukuran produk yang telah diperbarui: "))
                            ubah_asli = input("Apakah data ini akan di ubah? (y/n): ").lower()
                            if ubah_asli == 'y':
                                ukuran = ubah_kolom
                                for i in daftar_barang:
                                    if i[0] == kunci:
                                        i[3] = ukuran
                                        print()
                                        print("Data Sebelum di ubah")
                                        data = [list_sementara]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="double_grid",colalign=align)
                                        print(table)

                                        print()
                                        print("Data Setelah di ubah")
                                        data = [i]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="double_grid",colalign=align)
                                        print(table)

                                print(">"*35, "Perubahan data berhasil disimpan", "<"*35)
                            elif ubah_asli == 'n':
                                print("\n<<< Perubahan data dibatalkan.>>>")
                            else:
                                print("\n=== Mohon masukan dengan huruf y atau n.===")
                        elif kolom == 'stok':
                            stok = list_sementara[4]
                            print("="*25)
                            print(f"Stok   : {stok}")
                            print("="*25)
                            ubah_kolom = int(input("Masukan stok yang terbaru: "))
                            ubah_asli = input("Apakah data ini akan di ubah? (y/n): ").lower()
                            if ubah_asli == 'y':
                                stok = ubah_kolom
                                for i in daftar_barang:
                                    if i[0] == kunci:
                                        i[4] = stok
                                        print()
                                        print("Data Sebelum di ubah")
                                        data = [list_sementara]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="rounded_grid",colalign=align)
                                        print(table)

                                        print()
                                        print("Data Setelah di ubah")
                                        data = [i]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="rounded_grid",colalign=align)
                                        print(table)

                                print(">"*35, "Perubahan data berhasil disimpan", "<"*35)
                            elif ubah_asli == 'n':
                                print("\n<<< Perubahan data dibatalkan.>>>")
                            else:
                                print("\n=== Mohon masukan dengan huruf y atau n.===")
                        elif kolom == 'harga':
                            harga = list_sementara[5]
                            print("="*25)
                            print(f"Harga   : {harga}")
                            print("="*25)
                            ubah_kolom = int(input("Masukan harga yang telah diperbarui: "))
                            ubah_asli = input("Apakah data ini akan di ubah? (y/n): ").lower()
                            if ubah_asli == 'y':
                                harga = ubah_kolom
                                for i in daftar_barang:
                                    if i[0] == kunci:
                                        i[5] = harga
                                        print()
                                        print("Data Sebelum di ubah")
                                        data = [list_sementara]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="grid",colalign=align)
                                        print(table)

                                        print()
                                        print("Data Setelah di ubah")
                                        data = [i]
                                        headers =["ID Barang","Nama","Bahan(Material)","Ukuran(mm)","Stok(Jumlah)","Harga(Satuan)"]                        
                                        align = ["center","left","left","center","center","center"]
                                        table = tabulate(data, headers, tablefmt="grid",colalign=align)
                                        print(table)

                                print(">"*35, "Perubahan data berhasil disimpan", "<"*35)
                            elif ubah_asli == 'n':
                                print("\n<<< Perubahan data dibatalkan.>>>")
                            else:
                                print("\n=== Mohon masukan dengan huruf y atau n.===")
                        else:
                            print("\n=== Mohon masukan dengan benar.===")
                    elif ubah == 'n':
                        print("\n>>> Perubahan data dibatalkan.<<<")
                    else:
                        print("\n=== Mohon masukan dengan huruf y atau n.===")
            if id_ditemukan == False:
                print("\n>>> Data yang anda cari tidak tersedia.<<<")
        elif pilih == 2:
            return main_menu_admin()       
        else:
            print("\n=== Mohon untuk masukan angka yg tersedia.===")
            continue

def delete_menu():
    while True:
        print("\nMenu penghapusan data")
        print("1.Hapus data barang")
        print("2.Kembali ke main menu")
        try:
            pilih = int(input("Masukan angka di pilihan main menu yang ingin ditampilkan: "))
        except:
            print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
            continue

        if pilih ==1 :
            headers = ["ID Barang","Nama","Bahan (Material)","Ukuran(mm)","Stok (Jumlah)","Harga (Satuan)"]
            align = ["center","left","left","center","center","center"]
            table = tabulate(daftar_barang, headers, tablefmt="mixed_grid",colalign=align)
            print(table)
            try:
                kunci = int(input("Masukan ID barang yang ingin di hapus: "))
            except:
                print("\n*** Pilihan tidak valid! Mohon masukan ID barang yang benar.***")
                continue

            id_ditemukan = False
            for item in daftar_barang:
                if item[0] == kunci:
                    print("\n===== Detail Barang =====")
                    print(f"ID     : {item[0]}")
                    print(f"Nama   : {item[1]}")
                    print(f"Bahan  : {item[2]}")
                    print(f"Ukuran : {item[3]}")
                    print(f"Stok   : {item[4]}")
                    print(f"Harga  : {item[5]}")
                    print("=========================")
                    id_ditemukan = True 
                    hapus = input("Apakah data ingin dihapus (y/n): ")
                    if hapus == 'y':
                        daftar_barang.remove(item)
                        print("\n~~~ Data telah berhasil dihapus.~~~")
                    elif hapus == 'n':
                        print("\n<<< Penghapusan data dibatalkan.>>>")
                    else:
                        print("\n=== Mohon  masukan huruf y atau n.===")
            if id_ditemukan == False:
                print("\n~~~ Data yang anda cari tidak tersedia.~~~")
        elif pilih == 2 :
            return main_menu_admin()

        else:
            print("\n=== Mohon untuk masukan angka yg tersedia.===")
            continue

def main_menu():
    while True:
        akses_login()
        try:
            pilihan = int(input("Masukkan angka di pilihan main menu yang ingin di tampilkan: "))
        except:
            print("\n*** Pilihan tidak valid! Mohon masukan dengan angka yang benar.***")
            continue
        if pilihan == 1 :
            login_admin()            
        elif pilihan == 2 :
            login_user()            
        elif pilihan == 3:
            print("^^^ Program selesai, Terima kasih.^^^")
            break
        else:
            print('''\n=== Pilihan tidak valid! Angka yang anda masukan tidak ada di main menu,
Mohon masukan angka yang ada main menu.===''')

main_menu()

       