judul_kolom = ['Kode Barang', 'Nama Barang', 'Stok Barang', 'Harga Satuan', 'Nama Sales']
barang = [['PP001', 'Baseball Cap Nike', 12, 750000, 'Sales A'],
          ['PP002', 'Flannel Patagonia', 20, 300000, 'Sales B'], 
          ['PP003', 'Kaos Vans', 24, 250000, 'Sales C'], 
          ['PP004', 'Celana Chino ', 12, 225000, 'Sales D'], 
          ['PP005', 'Sepatu Vans Sk8', 25, 800000, 'Sales C']]
format_spasi = '{:<24}' * len(judul_kolom)

def prog_app():
     while True:
        print('''===============================================
                 MENU UTAMA
               PRELIM PROJECT
===============================================
            Pilih User Sebagai:
            1 : Sebagai Penjual
            2 : Sebagai Pembeli
            3 : Hentikan Aplikasi
_______________________________________________''')
        pilih_user = input('Masukan angka menu yang diinginkan: ')
        print()

        if pilih_user == '1':
            penjual()
        elif pilih_user == '2':
            pembeli()
        elif pilih_user == '3':
            print('### Terima kasih sudah memakai aplikasi ini ###')
            print()
            break
        else:
            print('!!! Angka menu yang anda masukan tidak tersedia !!!')
            print()
            continue

def tampilan_daftar_barang():
    print('=======================================Daftar Barang Prelim Project=======================================')
    print(format_spasi.format(*judul_kolom))
    print('==========================================================================================================')
    for i in range(len(barang)) :
        print(format_spasi.format(*barang[i]))
    print('__________________________________________________________________________________________________________')
    print()

def followup(x):
    if x == 'Y':
        print()
    elif x == 'T':
        print()
        print('!!! Aktifitas dibatalkan !!!')
        print()
    else:
        print('Masukan keyword yang benar')
        print()

def pembeli():
    while True:
        print('''==========================================================
          SELAMAT DATANG DI TOKO PRELIM PROJECT
                     User: Pembeli
==========================================================
        Menu 1 : Menampilkan data penjualan barang
        Menu 2 : Membeli barang
        Menu 3 : Kembali ke menu utama
__________________________________________________________''')
        pilih_menu_pembeli = input('Masukan angka menu yang diinginkan: ')
        print()

        if pilih_menu_pembeli == '1':
            tampilan_daftar_barang()
            print()
        elif pilih_menu_pembeli == '2':
            tampilan_daftar_barang()
            print()
            input_kode_barang = input('Masukan Kode Barang yang Ingin dibeli: ').upper()
            print()
            var_tem_pembeli = 1
            while var_tem_pembeli <= len(barang):
                if input_kode_barang == barang[var_tem_pembeli - 1][0]:
                    input_jumlah_beli = input('Masukan jumlah pembelian: ') 
                    print()
                    if input_jumlah_beli.isdigit() == True:
                        input_jumlah_beli = int(input_jumlah_beli)
                        if input_jumlah_beli <= int(barang[var_tem_pembeli-1][2]): 
                            total_harga_beli = input_jumlah_beli*(barang[var_tem_pembeli-1][3]) 
                            print(f'Anda akan membeli {barang[var_tem_pembeli-1][1]} sebanyak {input_jumlah_beli} Pcs seharga Rp{total_harga_beli}')
                            simpan_data_beli = input('Apakah Anda ingin melanjutkan pembayaran? (Y/T):').upper()
                            followup(simpan_data_beli) 
                            if simpan_data_beli == 'Y':
                                input_uang = input('Masukan jumlah uang: ')
                                print()
                                if input_uang.isdigit() == True:
                                    input_uang = int(input_uang)
                                    print()
                                else:
                                    print()
                                    print('!!! Masukan jumlah uang berupa angka (tanpa huruf dan karakter) !!!')
                                    print()
                                    continue
                                if input_uang == total_harga_beli:
                                    print()
                                    print('### Transaksi berhasil ###')
                                    print()
                                    barang[var_tem_pembeli-1][2] -= input_jumlah_beli 
                                    print('=======================================Daftar Barang Prelim Project=======================================')
                                    print(format_spasi.format(*judul_kolom))
                                    print('==========================================================================================================')
                                    print(format_spasi.format(*barang[var_tem_pembeli-1]))
                                    print('__________________________________________________________________________________________________________')
                                    print()
                                    var_tem_pembeli += 1
                                    break
                                elif input_uang > total_harga_beli:
                                    print()
                                    print('### Transaksi berhasil ###')
                                    print(f'### Uang anda kembali Rp{input_uang-total_harga_beli} ###')
                                    print()
                                    barang[var_tem_pembeli-1][2] -= input_jumlah_beli 
                                    print('=======================================Daftar Barang Prelim Project=======================================')
                                    print(format_spasi.format(*judul_kolom))
                                    print('==========================================================================================================')
                                    print(format_spasi.format(*barang[var_tem_pembeli-1]))
                                    print('__________________________________________________________________________________________________________')
                                    print()
                                    var_tem_pembeli += 1
                                    break
                                else:
                                    print()
                                    print('!!! Transaksi dibatalkan !!!')
                                    print(f'!!! Uang yang anda masukan kurang Rp{total_harga_beli-input_uang} !!!')
                                    print()
                                    break  
                            else:
                                print
                                break
                        else:
                            print()
                            print('!!! Stok barang tidak mencukupi dengan jumlah yang ingin anda beli !!!')
                            print() 
                            break 
                    else:
                        print()
                        print('!!! Masukan jumlah beli berupa angka (tanpa huruf dan karakter) !!!')
                        print()
                        continue
                else:
                    var_tem_pembeli += 1
            else:
                print()
                print('!!! Kode yang anda masukan tidak tersedia !!!')
                print()
                continue           
        elif pilih_menu_pembeli == '3':
            break   
        else:
            print()
            print('!!! Masukan angka menu yang benar !!!')
            print() 
            continue    
# pembeli()



def penjual() :
    while True:
        print('''==========================================================
          SELAMAT DATANG DI TOKO PRELIM PROJECT
                     User: Penjual
==========================================================
        Menu 1 : Menampilkan data penjualan barang
        Menu 2 : Menambah data penjualan barang
        Menu 3 : Mengubah data penjualan barang
        Menu 4 : Menghapus data penjualan barang
        Menu 5 : Kembali ke menu utama
__________________________________________________________''')
        pilih_menu = input('Masukan angka menu yang diinginkan: ')
        print()

        if pilih_menu == '1':
            menu_1()
        elif pilih_menu == '2':
            menu_2()
        elif pilih_menu == '3':
            menu_3()
        elif pilih_menu == '4':
            menu_4()
        elif pilih_menu == '5':
            break
        else:
            print()
            print('!!! Masukan angka menu yang benar !!!')
            print()
            continue
        





def menu_1():
    while True:
        print('========PILIH MENU YANG DIINGINKAN========')
        print('1. Menampilkan semua data')
        print('2. Menampilkan kode barang yang diinginkan')
        print('3. Kembali ke menu utama penjual')
        print('__________________________________________')
        input_menu1 = input('Masukan angka yang diinginkan: ')
        print()
        if input_menu1 == '1':
            print()
            tampilan_daftar_barang()

        elif input_menu1 == '2':
            kode_barang = input('Masukan kode barang yang diinginkan: ').upper()
            print()
            var_temp = 1
            while var_temp <= len(barang):
                if kode_barang == barang[var_temp - 1][0]:
                    print('=======================================Daftar Barang Prelim Project=======================================')
                    print(format_spasi.format(*judul_kolom))
                    print('==========================================================================================================')
                    print(format_spasi.format(*barang[var_temp-1]))
                    print('__________________________________________________________________________________________________________')
                    print()
                    break
                else:
                    var_temp += 1
            else:
                print()
                print('!!! Kode barang yang di input tidak tersedia !!!')
                print()
        elif input_menu1 == '3':
            break
        else :
            print()
            print ('!!! Masukan menu angka yang benar !!!')
            print()
            continue
# menu_1()

def menu_2():
    while True:
        print('========PILIH MENU YANG DIINGINKAN========')
        print('1. Menambahkan barang baru')
        print('2. Kembali ke menu utama penjual')
        print('__________________________________________')
        input_menu2 = input('Masukan menu angka yang diinginkan: ')
        print()

        if input_menu2 == '1':
            input_kode_barang = input('Masukan kode barang: ').upper()
            var_temp_2 = 1
            while var_temp_2 <= len(barang):
                if input_kode_barang == barang[var_temp_2-1][0]:
                    print()
                    print('!!! Kode barang yang anda masukan sudah tersedia !!!')
                    print()
                    break
                else:
                    var_temp_2 += 1
            else:
                nama_barang = input('Masukan nama barang: ').title()          
                stok_barang = input('Masukan stok barang: ') 
                if stok_barang.isdigit() == True:
                    stok_barang = int(stok_barang)
                else:
                    print()
                    print('!!! Masukan hanya berupa angka (tanpa huruf dan karakter) !!!')
                    print()
                    continue
                harga_satuan = input('Masukan harga satuan barang: ')
                if harga_satuan.isdigit() == True:
                    harga_satuan = int(harga_satuan)
                else:
                    print()
                    print('!!! Masukan hanya berupa angka (tanpa huruf dan karakter) !!!')
                    print()
                    continue
                nama_sales = input('Masukan nama sales barang: ').title()
                list_baru_barang = [input_kode_barang, nama_barang, stok_barang, harga_satuan, nama_sales]
                simpan_data_1 = input('Apakah Anda ingin menyimpan data barang baru ini? (Y/T):').upper()
                followup(simpan_data_1) 
                if simpan_data_1 == 'Y':
                    barang.append(list_baru_barang)
                    print('Berikut adalah daftar barang terbaru')
                    barang.sort()
                    print()
                    tampilan_daftar_barang()
        elif input_menu2 == '2':
            print()
            break
        else:
            print()
            print('!!! Masukan menu angka yang benar !!!')
            print()
            continue

# menu_2()

def menu_3():
    while True:
        print('========PILIH MENU YANG DIINGINKAN========')
        print('1. Mengubah data barang')
        print('2. Kembali ke menu utama penjual')
        print('__________________________________________')
        input_menu3 = input('Masukan angka yang diinginkan: ')
        print()

        if input_menu3 == '1':
            input_kode_barang = input('Masukan kode barang: ').upper()
            print()
            var_temp_3 = 1
            while var_temp_3 <= len(barang) :
                if input_kode_barang == barang[var_temp_3-1][0] :
                    print(format_spasi.format(*judul_kolom))
                    print(format_spasi.format(*barang[var_temp_3-1]))
                    print()
                    simpan_data_2 = input(f'Apakah Anda ingin mengubah barang {input_kode_barang} ini? (Y/T):').upper()
                    followup(simpan_data_2) 
                    if simpan_data_2 == 'Y':
                        update_nama_kolom = input('Masukan nama kolom yang ingin diubah: ').title()
                        if update_nama_kolom == judul_kolom[0]: 
                            print()
                            print('!!! Kode barang tidak bisa diubah !!!')
                            print()
                            break
                        elif update_nama_kolom == judul_kolom[1]:
                            nama_baru = input('Masukan nama barang baru: ').title()
                            simpan_data_2 = input(f'Apakah Anda ingin mengubah nama barang {barang[var_temp_3-1][1]} menjadi {nama_baru}? (Y/T):').upper()
                            followup(simpan_data_2)
                            if simpan_data_2 == 'Y':
                                barang[var_temp_3-1][1] = nama_baru
                                print(format_spasi.format(*judul_kolom))
                                print(format_spasi.format(*barang[var_temp_3-1]))
                                print()
                                var_temp_3 += 1
                                break
                            else:
                                break
                        elif update_nama_kolom == judul_kolom[2]:
                            stok_baru = input('Masukan stok barang baru: ')
                            if stok_baru.isdigit() == True:
                                stok_baru = int(stok_baru)
                            else:
                                print()
                                print('!!! Masukan hanya berupa angka (tanpa huruf dan karakter) !!!')
                                print()
                                break
                            simpan_data_2 = input(f'Apakah Anda ingin mengubah stok barang {barang[var_temp_3-1][2]} menjadi {stok_baru}? (Y/T):').upper()
                            followup(simpan_data_2)
                            if simpan_data_2 == 'Y':
                                barang[var_temp_3-1][2] = stok_baru
                                print(format_spasi.format(*judul_kolom))
                                print(format_spasi.format(*barang[var_temp_3-1]))
                                print()
                                var_temp_3 += 1
                                break
                            else:
                                break
                        elif update_nama_kolom == judul_kolom[3]: 
                            harga_baru = input('Masukan harga satuan barang baru: ')
                            if harga_baru.isdigit() == True:
                                harga_baru = int(harga_baru)
                            else:
                                print()
                                print('!!! Masukan hanya berupa angka (tanpa huruf dan karakter) !!!')
                                print()
                                break
                            simpan_data_2 = input(f'Apakah Anda ingin mengubah {barang[var_temp_3-1][3]} menjadi {harga_baru}? (Y/T):').upper()
                            followup(simpan_data_2)
                            if simpan_data_2 == 'Y':
                                barang[var_temp_3-1][3] = harga_baru
                                print(format_spasi.format(*judul_kolom))
                                print(format_spasi.format(*barang[var_temp_3-1]))
                                print()
                                var_temp_3 += 1
                                break
                            else:
                                break
                        elif update_nama_kolom == judul_kolom[4]:
                            sales_baru = input('Masukan nama sales baru: ').title()
                            simpan_data_2 = input(f'Apakah Anda ingin mengubah {barang[var_temp_3-1][4]} menjadi {sales_baru}? (Y/T):').upper()
                            followup(simpan_data_2)
                            if simpan_data_2 == 'Y':
                                barang[var_temp_3-1][4] = sales_baru
                                print(format_spasi.format(*judul_kolom))
                                print(format_spasi.format(*barang[var_temp_3-1]))
                                print()
                                var_temp_3 += 1
                                break
                            else:
                                break
                        else:
                            print()
                            print('!!! Nama kolom yang dimasukan tidak tersedia !!!')
                            print()
                            break
                    else:
                        break
     
                else:
                    var_temp_3 += 1
            else:
                print()
                print('!!! Kode barang tidak tersedia !!!')
                print()
                continue
        elif input_menu3 == '2':
            break
        else:
            print()
            print('!!! Masukan menu angka yang benar !!!')
            print()
            continue
# menu_3()

def menu_4():
    while True:
        print('========PILIH MENU YANG DIINGINKAN========')
        print('1. Menghapus data barang')
        print('2. Kembali ke menu utama penjual')
        print('__________________________________________')
        input_menu4 = input('Masukan angka yang diinginkan: ')
        print()
        if input_menu4 == '1':
            hapus_barang = input('Masukan kode barang: ').upper()
            var_temp_4 = 1
            while var_temp_4 <= len(barang) :
                if hapus_barang == barang[var_temp_4-1][0] :
                    print('=======================================Daftar Barang Prelim Project=======================================')
                    print(format_spasi.format(*judul_kolom))
                    print('==================================================================t=======================================')
                    print(format_spasi.format(*barang[var_temp_4-1]))
                    print('___________________________________________________________________________________________________________')
                    print()
                    simpan_data_3 = input(f'Apakah Anda ingin menghapus barang {barang[var_temp_4-1][1]} ini? (Y/T):').upper()
                    followup(simpan_data_3)
                    if simpan_data_3 == 'Y':
                        barang.pop(var_temp_4-1)
                        tampilan_daftar_barang()
                        print()
                        break
                    else:
                        break
                else:
                    var_temp_4 +=1
                    continue
            else:
                print()
                print('!!! Kode barang yang di input tidak tersedia !!!')
                print()
        elif input_menu4 == '2':
            break
        else:
            print()
            print('!!! Masukan menu angka yang benar !!!')
            print()
            continue

# menu_4()

prog_app()




