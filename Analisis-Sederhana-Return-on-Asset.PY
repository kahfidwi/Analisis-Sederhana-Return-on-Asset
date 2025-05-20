
from tabulate import tabulate
import math

daftar_perusahaan = [
{"Key_id" : "BBCA2022", "Kode_Emiten" : "BBCA", "Nama_Perusahaan" : "Bank Central Asia", "Tahun" : 2022, "Laba" : 76.7, "Total_Aset" : 1075.5, "Return_on_Aset" : 7.14},
{"Key_id" : "BBCA2023", "Kode_Emiten" : "BBCA", "Nama_Perusahaan" : "Bank Central Asia", "Tahun" : 2023, "Laba" : 80.1, "Total_Aset" : 1228.3, "Return_on_Aset" : 6.55},
{"Key_id" : "BBCA2024", "Kode_Emiten" : "BBCA", "Nama_Perusahaan" : "Bank Central Asia", "Tahun" : 2024, "Laba" : 89.5, "Total_Aset" : 1314.7, "Return_on_Aset" : 6.81},
{"Key_id" : "BBNI2022", "Kode_Emiten" : "BBNI", "Nama_Perusahaan" : "Bank Negara Indonesia", "Tahun" : 2022, "Laba" : 54.3, "Total_Aset" : 891.3, "Return_on_Aset" : 6.13},
{"Key_id" : "BBNI2023", "Kode_Emiten" : "BBNI", "Nama_Perusahaan" : "Bank Negara Indonesia", "Tahun" : 2023, "Laba" : 57, "Total_Aset" : 964.8, "Return_on_Aset" : 5.94},
{"Key_id" : "BBNI2024", "Kode_Emiten" : "BBNI", "Nama_Perusahaan" : "Bank Negara Indonesia", "Tahun" : 2024, "Laba" : 61.2, "Total_Aset" : 1039.8, "Return_on_Aset" : 6.01},
{"Key_id" : "BMRI2022", "Kode_Emiten" : "BMRI", "Nama_Perusahaan" : "Bank Mandiri", "Tahun" : 2022, "Laba" : 57.0, "Total_Aset" : 964.8, "Return_on_Aset" : 7.12},
{"Key_id" : "BMRI2023", "Kode_Emiten" : "BMRI", "Nama_Perusahaan" : "Bank Mandiri", "Tahun" : 2023, "Laba" : 61.2, "Total_Aset" : 1029.8, "Return_on_Aset" : 7.93},
{"Key_id" : "BJBB2022", "Kode_Emiten" : "BJBB", "Nama_Perusahaan" : "Bank Jawa Barat dan Banten", "Tahun" : 2019, "Laba" : 7.1, "Total_Aset" : 123.5, "Return_on_Aset" : 5.81},
]


# fungsi tampilan yang sudah di sort
def tampilan_1():
    print(tabulate(sorted(daftar_perusahaan, key=lambda x: x['Key_id'],reverse="False"), headers="keys", tablefmt="fancy_grid"))

# fungsi input harga
def input_angka(angka):
    while True:
        try:
            return int(input(angka))       
        except:
            print("Input harus berupa angka! Coba lagi ")

# fungsi input float
def input_float(a_float):
    while True:
        try:
            return float(input(a_float))      
        except:
            print("Input harus berupa angka! Coba lagi ")

# fungsi input harga (str)
def input_kata(kata):
    while True:
        kata = input(kata)
        if kata.isalpha():
            return kata
        else:
            print("Input harus berupa huruf! Coba lagi ")

def kembali_menu_utama():
    yakin = input("Apakah anda yakin kembali ke menu utama? (y/n) ").lower()
    if yakin  == "y": 
        print("Kembali ke menu utama")
        pilihan()
    elif yakin == "n":
        print("Kembali ke menu sebelumnya")
        return
    else:
        print('Input harus "y" atau "n"')



# 1. Menampilkan data
def menampilkan_data():

    while True:
        print('''
    ---------------------------------------------------------
    | Menu Menampilkan Data:              
    | 1. Menampilkan Seluruh Data
    | 2. Menampilkan Data Berdasarkan Kode_Emiten Yang Sama
    | 3. Kembali ke Menu Utama
    ----------------------------------------------------------''')
        
        menu_tampilkan = input_angka("\nMasukkan angka Menu yang ingin dijalankan: ")
        
        if menu_tampilkan == 1:
            if len(daftar_perusahaan) == 0:
                print("Tidak Tersedia Data Perusahaan!")
                continue
            tampilan_1()
            
        def tampilan_2():
            if len(daftar_perusahaan) == 0:
                print("Tidak Tersedia Data Perusahaan!")
                return
            else:          
                if menu_tampilkan == 2:
                    input_kode_emiten = input_kata("Masukan Kode_Emiten perusahaan : ").upper()
                    data_emiten = []

                    for perusahaan in daftar_perusahaan:
                        if perusahaan["Kode_Emiten"] == input_kode_emiten:
                            data_emiten.append(perusahaan)

                    if data_emiten:
                        print(tabulate(data_emiten, headers="keys", tablefmt="fancy_grid"))
                    else:
                        print("Kode_Emiten tidak ditemukan!")
                        menampilkan_data()
        
        tampilan_2()
            
        if menu_tampilkan == 3:
            kembali_menu_utama()
        
        elif menu_tampilkan > 3:
            print("Angka tidak valid")



# 2. Menambahkan data
def menambah():

    while True:
        print('''
    ---------------------------------------------
    | Menu Menambahkan Data:
    | 1. Menambahkan Data_Emiten Yang Sudah Ada          
    | 2. Menambahkan Data_Emiten Baru
    | 3. Kembali ke Menu Utama
    ---------------------------------------------''') 
        
        menu_tambah = input_angka("\nMasukkan angka Menu yang ingin dijalankan: ")

        def tambah_1():
            tampilkan_tambah1 = []
            if menu_tambah == 1:
                if len(daftar_perusahaan) == 0:
                    print("Tidak Tersedia Data Perusahaan!")
                    return 
                else:                
                    tampilan_1()
                    input_kode_emiten = input_kata("Masukan Kode_Emiten perusahaan : ").upper()
                
                # Menambahkan variabel "status" untuk kondisi memastikan bahwa Kode_Emiten yang ingin ditambahkan ada di daftar perusahaan.
                status = False
                
                for i in daftar_perusahaan:
                    if i["Kode_Emiten"] == input_kode_emiten:

                        status = True

                        input_nama_perusahaan = i["Nama_Perusahaan"]
                        
                        input_tahun = input_angka("Masukan tahun : ")

                        if i["Tahun"] == input_tahun:
                            print(f"Kode_Emiten {input_kode_emiten} ditahun {input_tahun} sudah ada!")
                            return

                        input_laba = input_float("Masukan laba perusahaan dalam miliar (contoh: 65.5123 miliar ditulis 65.5) : ")
                        input_aset = input_float("Masukan Total_Aset perusahaan dalam miliar (contoh: 964.8123 miliar ditulis 964.8) : ")
                        input_roa = round(input_laba/input_aset*100,2)
                        str_tahun = str(input_tahun)
                        input_kode_key = input_kode_emiten + str_tahun
                        tampilkan_tambah1 = {"Key_id":input_kode_key, "Kode_Emiten":input_kode_emiten, "Nama_Perusahaan":input_nama_perusahaan, "Tahun":input_tahun, "Laba":input_laba, "Total_Aset":input_aset, "Return_on_Aset":input_roa}
                        break

                if not status:
                    print(f"Kode_Emiten {input_kode_emiten} tidak ada di Daftar Perusahaan!")
                    return
                    
                while True:
                    print(tabulate([tampilkan_tambah1.values()], headers=tampilkan_tambah1.keys(), tablefmt="fancy_grid"))
                    yakin_tambah = input("Apakah anda yakin menambahkan data? (y/n) ").lower()

                    if yakin_tambah == "y":
                        daftar_perusahaan.append({"Key_id":input_kode_key, "Kode_Emiten":input_kode_emiten, "Nama_Perusahaan":input_nama_perusahaan, "Tahun":input_tahun, "Laba":input_laba, "Total_Aset":input_aset, "Return_on_Aset":input_roa})
                        print(f"Berhasil Menambahkan {input_kode_key}") 
                        return 

                    elif yakin_tambah == "n":
                        print(f"Batal menambahkan {input_kode_key}")
                        return

                    else:
                        print('Input harus "y" atau "n"')

        def tambah_2():
            tampilkan_tambah2 = []
            if menu_tambah == 2:

                tampilan_1()

                input_kode_emiten = input_kata("Masukan Kode_Emiten perusahaan : ").upper()

                if len(daftar_perusahaan) == 0:
                     input_nama_perusahaan = input("Masukan Nama_Perusahaan : ").title()
                     input_tahun = input_angka("Masukan tahun : ")
                     input_laba = input_float("Masukan laba perusahaan dalam miliar (contoh: 65.5123 miliar ditulis 65.5) : ")
                     input_aset = input_float("Masukan Total_Aset perusahaan dalam miliar (contoh: 964.8123 miliar ditulis 964.8): ")
                     input_roa = round(input_laba/input_aset*100,2)
                     str_tahun = str(input_tahun)
                     input_kode_key = input_kode_emiten + str_tahun
                     tampilkan_tambah2 = {"Key_id":input_kode_key, "Kode_Emiten":input_kode_emiten, "Nama_Perusahaan":input_nama_perusahaan, "Tahun":input_tahun, "Laba":input_laba, "Total_Aset":input_aset, "Return_on_Aset":input_roa}

                else:
                    for kode in daftar_perusahaan:
                        if kode["Kode_Emiten"] == input_kode_emiten:
                            print(f"Kode_Emiten {input_kode_emiten} sudah ada dalam data!")
                            return
                            
                        elif kode["Kode_Emiten"] != input_kode_emiten:
                            input_nama_perusahaan = input("Masukan Nama_Perusahaan : ").title()
                            input_tahun = input_angka("Masukan tahun : ")
                            input_laba = input_float("Masukan laba perusahaan dalam miliar (contoh: 65.5123 miliar ditulis 65.5) : ")
                            input_aset = input_float("Masukan Total_Aset perusahaan dalam miliar (contoh: 964.8123 miliar ditulis 964.8): ")
                            input_roa = round(input_laba/input_aset*100,2)
                            str_tahun = str(input_tahun)
                            input_kode_key = input_kode_emiten + str_tahun
                            tampilkan_tambah2 = {"Key_id":input_kode_key, "Kode_Emiten":input_kode_emiten, "Nama_Perusahaan":input_nama_perusahaan, "Tahun":input_tahun, "Laba":input_laba, "Total_Aset":input_aset, "Return_on_Aset":input_roa}
                            break

                while True:
                    print(tabulate([tampilkan_tambah2.values()], headers=tampilkan_tambah2.keys(), tablefmt="fancy_grid"))
                    yakin_tambah = input("Apakah anda yakin menambahkan data? (y/n) ").lower()
                    if yakin_tambah == "y":
                        daftar_perusahaan_baru = {"Key_id":input_kode_key, "Kode_Emiten":input_kode_emiten, "Nama_Perusahaan":input_nama_perusahaan, "Tahun":input_tahun, "Laba":input_laba, "Total_Aset":input_aset, "Return_on_Aset":input_roa}
                        daftar_perusahaan.append(daftar_perusahaan_baru)
                        print(f"Berhasil Menambahkan {input_kode_key}")  
                        return
                    
                    elif yakin_tambah == "n":
                        print("Batal menambahkan {input_kode_key}")
                        return
                    
                    else:
                        print('Input harus "y" atau "n"')

        tambah_1()
        tambah_2()
        
        if menu_tambah == 3:
            kembali_menu_utama()
                    
        elif menu_tambah > 3:
            print("Angka tidak valid!")
            


# 3. Mengurangi data
def mengurangi():

    global daftar_perusahaan

    while True:
        print('''
    -----------------------------------------------------
    | Menu Menghapus Data:
    | 1. Menghapus 1 Data Sesuai Dengan Key_id
    | 2. Menghapus Data Berdasarkan Dengan Kode_Emiten 
    | 3. Mengosongkan Seluruh Data         
    | 4. Kembali ke Menu Utama
    -----------------------------------------------------''') 

        menu_kurang = input_angka("\nMasukkan angka Menu yang ingin dijalankan: ")

        def hapus_1():
            if menu_kurang == 1:
                if len(daftar_perusahaan) == 0:
                    print("Tidak Tersedia Data Perusahaan!")
                    return 
                else:                  
                    tampilan_1()
                
                hapus1 = input("Masukan Key_id yang ingin dihapus: ").upper()

                status = False

                data_yang_dihapus = []

                for i in daftar_perusahaan:        
                    if i["Key_id"] == hapus1:
                        data_yang_dihapus.append(i)

                        status = True

                        while True:
                            print(tabulate(data_yang_dihapus, headers="keys", tablefmt="fancy_grid"))
                            
                            
                            yakin_tambah = input(f"Apakah anda yakin menghapus {hapus1}? (y/n) ").lower()

                            if yakin_tambah == "y":
                                daftar_perusahaan.remove(i)
                                print(f"Berhasil menghapus {hapus1}!")  
                                return
                            
                            elif yakin_tambah == "n":
                                print(f"Batal menghapus {hapus1}")
                                return
                            
                            else:
                                print('Input harus "y" atau "n"')

                if not status:
                    print(f"Key_id tersebut tidak {hapus1} di daftar perusahaan! ")
                        
        def hapus_2():
            if menu_kurang == 2:
                if len(daftar_perusahaan) == 0:
                    print("Tidak Tersedia Data Perusahaan!")
                    return 
                else:                  
                    tampilan_1()

                hapus2 = input("Masukan Kode_Emiten yang ingin dihapus: ").upper()

                status = False

                for i in daftar_perusahaan:
                    if i["Kode_Emiten"] == hapus2:
                        
                        while True:
                            yakin_tambah = input(f"Apakah anda yakin menghapus {hapus2} (y/n) ").lower()
                            if yakin_tambah == "y":
                                daftar_perusahaan.remove(i)
                                print(f'Berhasil menghapus {hapus2}!')
                                status = True
                                return
                            
                            elif yakin_tambah == "n":
                                print(f'Batal menghapus {hapus2}')
                                return
                            
                            else:
                                print('Input harus "y" atau "n"')
                
                if not status:
                    print(f'Kode_Emiten {hapus2} tidak ada di daftar perusahaan')

        def hapus_3():
            if menu_kurang == 3:
                if len(daftar_perusahaan) == 0:
                    print("Tidak Tersedia Data Perusahaan!")
                    return 

                else:  
                    while True:
                        yakin_tambah = input("Apakah anda yakin mengosongkan semua value data? (y/n) ").lower()

                        if yakin_tambah == "y":
                            daftar_perusahaan.clear()
                            print(f"Berhasil menghapus semua data!")  
                            return

                        elif yakin_tambah == "n":
                            print("Batal menghapus semua data")
                            return
                        
                        else:
                            print('Input harus "y" atau "n"')

        hapus_1()
        hapus_2()
        hapus_3()
        
        if menu_kurang == 4:
            kembali_menu_utama()

        elif menu_kurang > 4:
            print("Angka tidak valid!")



# 4. Mengupdate data
def perubahan():
        
    while True:
        print('''
    -----------------------------------
    | Menu Update Data:
    | 1. Mengubah Kode_Emiten
    | 2. Mengubah Nama_Perusahaan
    | 3. Mengubah Nilai Return_on_Aset         
    | 4. Kembali ke Menu Utama
    -----------------------------------''') 

        menu_update = input_angka("\nMasukkan angka Menu yang ingin dijalankan: ")

        def ubah_1():
            if menu_update == 1:
                if len(daftar_perusahaan) == 0:
                    print("Tidak Tersedia Data Perusahaan!")
                    return

                tampilan_1()

                ubah1 = input("Masukan Kode_Emiten yang ingin diubah: ").upper()
                
                status = False

                for i in daftar_perusahaan:
                    if i["Kode_Emiten"] == ubah1:

                        yakin_update= input("Apakah ingin melanjutkan mengubah data? (y/n) ").lower()

                        if yakin_update == "y": 
                            status = True

                            hasil_ubah1 = input("Masukan Kode_Emiten yang baru: ").upper()

                        elif yakin_update == "n":
                            print("Kembali ke menu update")
                            perubahan()
                        else:
                            print('Input harus "y" atau "n"')                       
                            return

                        while True:
                            
                            yakin_tambah = input(f"Apakah anda yakin merubah {ubah1}? (y/n) ").lower()
                            
                            if yakin_tambah == "y":
                                i["Kode_Emiten"] = hasil_ubah1
                                i["Key_id"] = hasil_ubah1 + str(i["Tahun"])
                                print(f"Berhasil merubah {ubah1} menjadi {hasil_ubah1}!")
                                return
                            
                            elif yakin_tambah == "n":
                                print(f"Batal merubah {ubah1}")
                                return
                            
                            else:
                                print('Input harus "y" atau "n"')
                                continue

                if not status:
                    print(f"{"Kode_Emiten"} tersebut tidak terdaftar di daftar perusahaan")

        def ubah_2():
            if menu_update == 2:
                if len(daftar_perusahaan) == 0:
                    print("Tidak Tersedia Data Perusahaan!")
                    return
                
                tampilan_1()
                
                ubah2 = input("Masukan Kode_Emiten yang ingin diubah: ").upper()

                status = False

                for i in daftar_perusahaan:
                    if i["Kode_Emiten"] == ubah2:
                        

                        yakin_update= input("Apakah ingin melanjutkan mengubah data? (y/n) ").lower()

                        if yakin_update == "y": 
                            status = True
                            hasil_ubah2 = input("Masukan Nama_Perusahaan yang baru: ").title()


                        elif yakin_update == "n":
                            print("Kembali ke menu update")
                            return 
                        else:
                            print('Input harus "y" atau "n"')  
                            return             



                        while True:
                            yakin_tambah = input(f"Apakah anda yakin merubah nama perusahaan? (y/n) ").lower()

                            if yakin_tambah == "y":
                                for i in daftar_perusahaan:
                                    if i["Kode_Emiten"] == ubah2:
                                        i["Nama_Perusahaan"] = hasil_ubah2
                                print(f"Berhasil merubah {ubah2} menjadi {hasil_ubah2}!")  
                                return
                            
                            elif yakin_tambah == "n":
                                print(f"Batal merubah nama {ubah2}")
                                return
                            
                            else:
                                print('Input harus "y" atau "n"')
                                continue

                if not status:
                    print("Kode_Emiten tersebut tidak terdaftar di daftar perusahaan")       

        def ubah_3():
            if menu_update == 3:
                if len(daftar_perusahaan) == 0:
                    print("Tidak Tersedia Data Perusahaan!")
                    return 

                tampilan_1()  

                ubah3 = input("Masukan Key_id untuk Data ROA yang ingin diubah: ").upper() 

                status = False 

                for i in daftar_perusahaan:
                    if i["Key_id"] == ubah3:
                        
                        yakin_update= input("Apakah ingin melanjutkan mengubah data? (y/n) ").lower()

                        if yakin_update == "y": 
                            
                            status = True

                            hasil_ubah_laba = input_float("Masukan Laba Perusahaan yang baru dalam miliar (contoh: 65.5123 miliar ditulis 65.5): ")
                            hasil_ubah_aset = input_float("Masukan Total_Aset Perusahaan yang baru dalam miliar (contoh: 964.8123 miliar ditulis 964.8): ")
                            hasil_ubah_roa = round(hasil_ubah_laba/hasil_ubah_aset*100,2)

                        elif yakin_update == "n":
                            print("Kembali ke menu update")
                            perubahan()
                        else:
                            print('Input harus "y" atau "n"')     
                        
                        while True:
                            yakin_ubah = input(f"Apakah anda yakin merubah ROA dari {ubah3}? (y/n) ").lower()

                            if yakin_ubah == "y":
                                i["Laba"] = hasil_ubah_laba
                                i["Total_Aset"] = hasil_ubah_aset
                                i["Return_on_Aset"] = hasil_ubah_roa
                                print(f'Berhasil merubah ROA {ubah3}! ')
                                return
                            
                            elif yakin_ubah == "n":
                                print(f'Batal merubah {ubah3}')
                                return
                            
                            else:
                                print('Input harus "y" atau "n"')
                                continue
                                
                if not status:
                    print("Key_id tersebut tidak tersedia di Daftar Perusahaan")

        ubah_1()
        ubah_2()
        ubah_3()

        if menu_update == 4:
            kembali_menu_utama()
        
        elif menu_update > 4:
            print("Angka tidak valid!")


def perbandingan():
    while True:
        print('''
    -------------------------------------
    | Menu Perbandingan Data:
    | 1. Membandingkan 2 Data Perusahaan
    | 2. Membandingkan Data Per Tahun        
    | 3. Kembali ke Menu Utama
    -------------------------------------''') 

        menu_perbandingan = input_angka("\nMasukkan angka Menu yang ingin dijalankan: ")

        def perbandingan1():    

            if menu_perbandingan == 1:
                perbandingan_1 = []
                perbandingan_2 = []

                if len(daftar_perusahaan) == 0:
                    print("Tidak Tersedia Data Perusahaan!")
                    return     
                               
                tampilan_1()
                
                while True:
                
                    input_perbandingan1 = input("Masukan Key_id Perusahaan 1 : ").upper()

                    status = False
                    
                    for i in daftar_perusahaan:
                        if i["Key_id"] == input_perbandingan1:
                            status = True
                            perbandingan_1.append(i)
                            break

                    if status:
                        break
                    else:
                        print("Key_id tidak ditemukan!")

                while True:

                    input_perbandingan2 = input("Masukan Key_id Perusahaan 2 : ").upper()

                    status = False

                    for i in daftar_perusahaan:
                        if i["Key_id"] == input_perbandingan2:
                            status = True
                            perbandingan_2.append(i)
                            break

                    if status:
                        break
                    else:
                        print("Key_id tidak ditemukan!")

                print()
                print(tabulate(perbandingan_1, headers="keys", tablefmt="fancy_grid"))
                print(tabulate(perbandingan_2, headers="keys", tablefmt="fancy_grid"))
                print()

                # - ROA di atas 15% dianggap sangat baik
                # - ROA antara 10% - 15% dianggap baik
                # - ROA antara 5% - 10% dianggap cukup baik
                # - ROA di bawah 5% dianggap kurang baik    
                if perbandingan_1[0]["Return_on_Aset"] >= 15:
                    print(f"Perusahaan 1 dengan Key_id {perbandingan_2[0]["Key_id"]} dianggap sangat baik ")        
                elif perbandingan_1[0]["Return_on_Aset"] >= 10:
                    print(f"Perusahaan 1 dengan Key_id {perbandingan_2[0]["Key_id"]} dianggap baik ")  
                elif perbandingan_1[0]["Return_on_Aset"] >= 5:
                    print(f"Perusahaan 1 dengan Key_id {perbandingan_2[0]["Key_id"]} dianggap cukup baik ")  
                else:
                    print(f"Perusahaan 1 dengan Key_id {perbandingan_2[0]["Key_id"]} dianggap kurang baik ")
                print(f"Laba yang didapat Perusahaan 1 adalah {perbandingan_1[0]["Return_on_Aset"]/10} % dari Total_Aset yang dimilki ")

                if perbandingan_2[0]["Return_on_Aset"] >= 15:
                    print(f"Perusahaan 2 dengan Key_id {perbandingan_2[0]["Key_id"]} dianggap sangat baik ")        
                elif perbandingan_2[0]["Return_on_Aset"] >= 10:
                    print(f"Perusahaan 2 dengan Key_id {perbandingan_2[0]["Key_id"]} dianggap baik ")  
                elif perbandingan_2[0]["Return_on_Aset"] >= 5:
                    print(f"Perusahaan 2 dengan Key_id {perbandingan_2[0]["Key_id"]} dianggap cukup baik ")  
                else:
                    print(f"Perusahaan 2 dengan Key_id {perbandingan_2[0]["Key_id"]} dianggap kurang baik ")                  
                print(f"Laba yang didapat Perusahaan 2 adalah {perbandingan_2[0]["Return_on_Aset"]/10} % dari Total_Aset yang dimilki ")
                print()

                perbandingan1_laba = math.fabs(round(perbandingan_2[0]["Laba"]-perbandingan_1[0]["Laba"]))
                perbandingan1_aset = math.fabs(round(perbandingan_2[0]["Laba"]-perbandingan_1[0]["Total_Aset"]))
                perbandingan1_roa = math.fabs(round(perbandingan_2[0]["Laba"]-perbandingan_1[0]["Return_on_Aset"]))
                print(f"\nPerbandingan Laba ke 2 Perusahaan tersebut adalah {perbandingan1_laba} miliar")
                print(f"Perbandingan Total_Aset ke 2 Perusahaan tersebut adalah {perbandingan1_aset} miliar")
                print(f"Perbandingan Return_on_Aset ke 2 Perusahaan tersebut adalah {perbandingan1_roa} miliar")



        def perbandingan2():    

            if menu_perbandingan == 2:

                perbandingan_3 = []

                if len(daftar_perusahaan) == 0:
                    print("Tidak Tersedia Data Perusahaan!")
                    return     
                               
                tampilan_1()
                
                input_perbandingan3 = input_angka("Masukan Tahun Perusahaan : ")
                   
                for i in daftar_perusahaan:
                    if i["Tahun"] == input_perbandingan3:
                        perbandingan_3.append(i)

                if len(perbandingan_3) == 0:
                    print("Tidak Data Perusahaan di Tahun Tersebut!")
                else:
                    print()
                    print(tabulate(perbandingan_3, headers="keys", tablefmt="fancy_grid"))

                    laba_max = perbandingan_3[0]["Laba"]
                    total_aset_max = perbandingan_3[0]["Total_Aset"]
                    roa_max = perbandingan_3[0]["Return_on_Aset"]

                    laba_min = perbandingan_3[0]["Laba"]
                    total_aset_min = perbandingan_3[0]["Total_Aset"]
                    roa_min = perbandingan_3[0]["Return_on_Aset"]

                    for i in perbandingan_3:
                        if i["Laba"] > laba_max:
                            laba_max = i["Laba"]
                        if i["Laba"] < laba_min:
                            laba_min = i["Laba"]
                        if i["Total_Aset"] > total_aset_max:
                            total_aset_max = i["Total_Aset"]
                        if i["Total_Aset"] < total_aset_min:
                            total_aset_min = i["Total_Aset"]
                        if i["Return_on_Aset"] > roa_max:
                            roa_max = i["Return_on_Aset"]
                        if i["Return_on_Aset"] < roa_min:
                            roa_min = i["Return_on_Aset"]
                    
                    print(f'''
Nilai dari Laba Perusahaan paling tinggi ditahun {input_perbandingan3} adalah {laba_max}
Nilai dari Laba Perusahaan paling kecil ditahun {input_perbandingan3} adalah {laba_min}

Nilai dari Total_Aset Perusahaan paling tinggi ditahun {input_perbandingan3} adalah {total_aset_max}
Nilai dari Total_Aset Perusahaan paling kecil ditahun {input_perbandingan3} adalah {total_aset_min}

Nilai dari Total_Aset Perusahaan paling tinggi ditahun {input_perbandingan3} adalah {roa_max}
Nilai dari Total_Aset Perusahaan paling kecil ditahun {input_perbandingan3} adalah {roa_min}
''')                
        perbandingan1()
        perbandingan2()

        if menu_perbandingan == 3:
            kembali_menu_utama()
        
        elif menu_perbandingan > 3:
            print("Angka tidak valid!")



# 5. Exit Program
def exit():
    yakin = input("Apakah anda yakin keluar dari program? (y/n) ").lower()
    if yakin  == "y": 
        print("\nExit Program\n")
        quit()
    elif yakin == "n":
        pilihan()
    else:
        print('Input harus "y" atau "n"')
        exit()
    


def pilihan():
    print("""
=========================
Menu Utama:             |
1. Menampilkan Data     |
2. Menambahkan Data     |
3. Menghapus Data       |
4. Mengupdate Data      |
5. Membandingkan Data   |
6. Exit Program         |
=========================""")

    menu = input_angka("\nMasukkan Angka Menu Yang Ingin Dijalankan: ")
        
    if menu == 1:
        menampilkan_data()                       
    elif menu == 2:
        menambah()
    elif menu == 3:
        mengurangi()
    elif menu == 4:
        perubahan() 
    elif menu == 5:
        perbandingan() 
    elif menu == 6:
        exit()                               
    else:
        print("Input yang anda masukan tidak sesuai")

pilihan()

