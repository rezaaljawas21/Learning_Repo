import os
import time
from tabulate import tabulate

def clear_screen():
    # Check the operating system and use the appropriate clear screen command
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

# Inisialisasi daftar siswa
siswa = [
    {
        'Nama': 'Alice',
        'Jenis Kelamin': 'Wanita',
        'NISN': '1234567890',
        'Kelas': 'XII-A',
        'Email': 'alice@example.com',
        'Alamat': 'Jl. Contoh No. 123'
    },
    {
        'Nama': 'Bob',
        'Jenis Kelamin': 'Pria',
        'NISN': '2345678901',
        'Kelas': 'XI-B',
        'Email': 'bob@example.com',
        'Alamat': 'Jl. Contoh No. 456'
    },
    {
        'Nama': 'Charlie',
        'Jenis Kelamin': 'Pria',
        'NISN': '3456789012',
        'Kelas': 'X-A',
        'Email': 'charlie@example.com',
        'Alamat': 'Jl. Contoh No. 789'
    },
    {
        'Nama': 'David',
        'Jenis Kelamin': 'Pria',
        'NISN': '4567890123',
        'Kelas': 'IX-C',
        'Email': 'david@example.com',
        'Alamat': 'Jl. Contoh No. 1011'
    },
    {
        'Nama': 'Eve',
        'Jenis Kelamin': 'Wanita',
        'NISN': '5678901234',
        'Kelas': 'X-B',
        'Email': 'eve@example.com',
        'Alamat': 'Jl. Contoh No. 1213'
    },
    {
        'Nama': 'Frank',
        'Jenis Kelamin': 'Pria',
        'NISN': '6789012345',
        'Kelas': 'XI-A',
        'Email': 'frank@example.com',
        'Alamat': 'Jl. Contoh No. 1415'
    },
    {
        'Nama': 'Grace',
        'Jenis Kelamin': 'Wanita',
        'NISN': '7890123456',
        'Kelas': 'IX-A',
        'Email': 'grace@example.com',
        'Alamat': 'Jl. Contoh No. 1617'
    },
    {
        'Nama': 'Harry',
        'Jenis Kelamin': 'Pria',
        'NISN': '8901234567',
        'Kelas': 'XII-B',
        'Email': 'harry@example.com',
        'Alamat': 'Jl. Contoh No. 1819'
    },
    {
        'Nama': 'Ivy',
        'Jenis Kelamin': 'Wanita',
        'NISN': '9012345678',
        'Kelas': 'XI-C',
        'Email': 'ivy@example.com',
        'Alamat': 'Jl. Contoh No. 2021'
    },
    {
        'Nama': 'Jack',
        'Jenis Kelamin': 'Pria',
        'NISN': '0123456789',
        'Kelas': 'X-C',
        'Email': 'jack@example.com',
        'Alamat': 'Jl. Contoh No. 2223'
    }
]

# Fungsi untuk menambahkan siswa
def tambah_siswa(nama, nisn, kelas, alamat, email, jenis_kelamin):
    msg = ""
    if jenis_kelamin.lower() == 'pria' or jenis_kelamin.lower() == 'wanita':
        if nisn.isdigit() and len(nisn) == 10:
            # Mengecek apakah NISN sudah ada dalam daftar siswa
            if not any(siswa_data['NISN'] == nisn for siswa_data in siswa):
                data_siswa = {
                    'Nama': nama,
                    'Jenis Kelamin': jenis_kelamin,
                    'NISN': nisn,
                    'Kelas': kelas,
                    'Email': email,
                    'Alamat': alamat
                }
                siswa.append(data_siswa)
                print("Siswa berhasil ditambahkan.")
                msg = "success"
            else:
                print("NISN sudah ada dalam daftar siswa.")
                msg = "failed"
        else:
            print("Mohon maaf, NISN harus terdiri dari 10 angka.")
            msg = "failed"
    else:
        print("Mohon maaf, ada kesalahan dalam input data. Jenis kelamin harus 'Pria' atau 'Wanita'.")
        msg = "failed"
    return msg


# Fungsi untuk menampilkan daftar siswa
def tampilkan_siswa():
    if not siswa:
        print("Daftar siswa kosong.")
        return

    header = ["Nama", "Jenis Kelamin", "NISN", "Kelas", "Email", "Alamat"]
    rows = []

    # Mengurutkan daftar siswa berdasarkan nama (ascending)
    siswa.sort(key=lambda x: x['Nama'])

    for data_siswa in siswa:
        row = [data_siswa['Nama'], data_siswa['Jenis Kelamin'], data_siswa['NISN'], data_siswa['Kelas'], data_siswa['Email'], data_siswa['Alamat']]
        rows.append(row)

    print(tabulate.tabulate(rows, headers=header, tablefmt="grid"))

# Fungsi untuk mencari siswa berdasarkan nama
def cari_siswa(nama):
    siswa_ditemukan = [data_siswa for data_siswa in siswa if data_siswa['Nama'] == nama]
    return siswa_ditemukan

# Fungsi untuk memperbarui siswa berdasarkan nama
def perbarui_siswa(nama, data_siswa_baru):
    for i, data_siswa in enumerate(siswa):
        if data_siswa['Nama'] == nama:
            siswa[i] = data_siswa_baru
            print("Siswa berhasil diperbarui.")

# Fungsi untuk menghapus siswa berdasarkan nama
def hapus_siswa(nama):
    for i, data_siswa in enumerate(siswa):
        if data_siswa['Nama'] == nama:
            del siswa[i]
            print("Siswa berhasil dihapus.")

# Program utama
status = ""
while True:
    print("=========================================")
    print("Sistem Manajemen Data Siswa")
    print("1. Tambah Siswa")
    print("2. Tampilkan Siswa")
    print("3. Cari Siswa")
    print("4. Perbarui Siswa")
    print("5. Hapus Siswa")
    print("6. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")
    print("=========================================")
    clear_screen()
    if pilihan == "1":
        while status != "success" or continue_:
            nama = input("Masukkan nama siswa: ")
            jenis_kelamin = input("Masukkan jenis kelamin siswa (Pria/Wanita): ")
            nisn = input("Masukkan NISN siswa: ")
            kelas = input("Masukkan kelas siswa: ")
            email = input("Masukkan alamat email siswa: ")
            alamat = input("Masukkan alamat siswa: ")
            status = tambah_siswa(nama, nisn, kelas, alamat, email, jenis_kelamin)
            #clear_screen()
    elif pilihan == "2":
        tampilkan_siswa()
    elif pilihan == "3":
        nama = input("Masukkan nama siswa yang akan dicari: ")
        siswa_ditemukan = cari_siswa(nama)
        if siswa_ditemukan:
            print("Siswa ditemukan:")
            tampilkan_siswa()
        else:
            print("Siswa tidak ditemukan.")
    elif pilihan == "4":
        nama = input("Masukkan nama siswa yang akan diperbarui: ")
        siswa_ditemukan = cari_siswa(nama)
        if siswa_ditemukan:
            data_siswa_baru = siswa_ditemukan[0].copy()
            data_siswa_baru['Nama'] = input("Masukkan nama yang diperbarui: ")
            data_siswa_baru['Jenis Kelamin'] = input("Masukkan jenis kelamin yang diperbarui (Pria/Wanita): ")
            data_siswa_baru['NISN'] = input("Masukkan NISN yang diperbarui: ")
            data_siswa_baru['Kelas'] = input("Masukkan kelas yang diperbarui: ")
            data_siswa_baru['Email'] = input("Masukkan alamat email yang diperbarui: ")
            data_siswa_baru['Alamat'] = input("Masukkan alamat yang diperbarui: ")
            perbarui_siswa(nama, data_siswa_baru)
        else:
            print("Siswa tidak ditemukan.")
    elif pilihan == "5":
        nama = input("Masukkan nama siswa yang akan dihapus: ")
        siswa_ditemukan = cari_siswa(nama)
        if siswa_ditemukan:
            hapus_siswa(nama)
        else:
            print("Siswa tidak ditemukan.")
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang valid.")