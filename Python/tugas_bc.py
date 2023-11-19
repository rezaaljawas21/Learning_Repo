from tabulate import tabulate

siswa = [
    {
        'Nama': 'Astrid Febiyani',
        'Jenis Kelamin': 'Wanita',
        'Agama': 'Katolik',
        'NISN': '1234567890',
        'Kelas': 'X-A',
        'Email': 'alice@example.com',
        'Alamat': 'Jl. Contoh No. 123'
    },
    {
        'Nama': 'Bobi Christian',
        'Jenis Kelamin': 'Pria',
        'Agama': 'Kristen',
        'NISN': '2345678901',
        'Kelas': 'X-A',
        'Email': 'bob@example.com',
        'Alamat': 'Jl. Contoh No. 456'
    },
    {
        'Nama': 'Charlie Puth',
        'Jenis Kelamin': 'Pria',
        'Agama': 'Islam',
        'NISN': '3456789012',
        'Kelas': 'X-A',
        'Email': 'charlie@example.com',
        'Alamat': 'Jl. Contoh No. 789'
    },
    {
        'Nama': 'David Saputra',
        'Jenis Kelamin': 'Pria',
        'Agama': 'Hindu',
        'NISN': '4567890123',
        'Kelas': 'X-A',
        'Email': 'david@example.com',
        'Alamat': 'Jl. Contoh No. 1011'
    },
    {
        'Nama': 'Evelin Hadjaja',
        'Jenis Kelamin': 'Wanita',
        'Agama': 'Buddha',
        'NISN': '5678901234',
        'Kelas': 'X-A',
        'Email': 'eve@example.com',
        'Alamat': 'Jl. Contoh No. 1213'
    },
    {
        'Nama': 'Frank Daffa',
        'Jenis Kelamin': 'Pria',
        'Agama': 'Konghucu',
        'NISN': '6789012345',
        'Kelas': 'X-A',
        'Email': 'frank@example.com',
        'Alamat': 'Jl. Contoh No. 1415'
    },
    {
        'Nama': 'Grace Angelin',
        'Jenis Kelamin': 'Wanita',
        'Agama': 'Katolik',
        'NISN': '7890123456',
        'Kelas': 'X-A',
        'Email': 'grace@example.com',
        'Alamat': 'Jl. Contoh No. 1617'
    },
    {
        'Nama': 'Harry Potter',
        'Jenis Kelamin': 'Pria',
        'Agama': 'Kristen',
        'NISN': '8901234567',
        'Kelas': 'X-A',
        'Email': 'harry@example.com',
        'Alamat': 'Jl. Contoh No. 1819'
    },
    {
        'Nama': 'Iva Celine',
        'Jenis Kelamin': 'Wanita',
        'Agama': 'Kristen',
        'NISN': '9012345678',
        'Kelas': 'X-A',
        'Email': 'ivy@example.com',
        'Alamat': 'Jl. Contoh No. 2021'
    },
    {
        'Nama': 'Jack Opa',
        'Jenis Kelamin': 'Pria',
        'Agama': 'Konghucu',
        'NISN': '0123456789',
        'Kelas': 'X-A',
        'Email': 'jack@example.com',
        'Alamat': 'Jl. Contoh No. 2223'
    }
]

# Fungsi untuk menampilkan daftar semua siswa
def tampilkan_siswa():
    header = ["Nama", "Jenis Kelamin", "Agama", "NISN", "Kelas", "Email", "Alamat"]
    rows = []
    siswa.sort(key=lambda x: x['Nama'])
    for data_siswa in siswa:
        row = [data_siswa['Nama'], data_siswa['Jenis Kelamin'], data_siswa['Agama'], data_siswa['NISN'], data_siswa['Kelas'], data_siswa['Email'], data_siswa['Alamat']]
        rows.append(row)
    print(tabulate(rows, header, tablefmt="grid"))

# Fungsi untuk menampilkan daftar siswa berdasarkan nisn (cari siswa)
def tampilkan_siswa_by_nisn(cari_nisn):
    header = ["Nama", "Jenis Kelamin", "Agama", "NISN", "Kelas", "Email", "Alamat"]
    rows = []
    siswa.sort(key=lambda x: x['Nama'])
    for data_siswa in siswa:
        if cari_nisn in data_siswa['NISN']:
            row = [data_siswa['Nama'], data_siswa['Jenis Kelamin'], data_siswa['Agama'], data_siswa['NISN'], data_siswa['Kelas'], data_siswa['Email'], data_siswa['Alamat']]
            rows.append(row)
    if rows: 
        print(tabulate(rows,header, tablefmt="grid"))
    else:
        print(f"Siswa dengan NISN '{cari_nisn}' tidak ditemukan.")

# Fungsi untuk menambahkan siswa
def tambah_siswa(nama, jenis_kelamin, agama, nisn, kelas, email, alamat):
    while True:
        if jenis_kelamin == 'Pria' or jenis_kelamin == 'Wanita':
            if nisn.isdigit() and len(nisn) == 10:
                if not any(data_siswa['NISN'] == nisn for data_siswa in siswa):
                    data_siswa = {
                        'Nama': nama,
                        'Jenis Kelamin': jenis_kelamin,
                        'Agama': agama,
                        'NISN': nisn,
                        'Kelas': kelas,
                        'Email': email,
                        'Alamat': alamat
                    }
                    siswa.append(data_siswa)
                    print("Siswa berhasil ditambahkan.")
                    break  # Keluar dari perulangan jika input valid
                else:
                    print("NISN sudah ada dalam daftar siswa.")
            else:
                print("Mohon maaf, NISN harus terdiri dari 10 angka dan hanya berisi digit.")
        else:
            print("Mohon maaf, ada kesalahan dalam input data. Jenis kelamin harus 'Pria' atau 'Wanita'.")
        # Mengulang permintaan input jika input tidak valid 
        nama = input("Masukkan nama siswa: ")
        jenis_kelamin = input("Masukkan jenis kelamin siswa (Pria/Wanita): ")
        agama = input("Masukkan agama siswa: ")
        nisn = input("Masukkan NISN siswa: ")
        kelas = input("Masukkan kelas siswa: ")
        email = input("Masukkan alamat email siswa: ")
        alamat = input("Masukkan alamat siswa: ")

# Fungsi untuk memperbarui siswa dengan NISN
def perbarui_siswa(nisn):
    for data_siswa in siswa:
        if data_siswa["NISN"] == nisn:
            print("Data siswa yang ingin diubah:")
            for key, value in data_siswa.items():
                if key != "NISN":
                    print(f"{key}: {value}")

            kolom = input("Masukkan nama kolom yang ingin diubah: ").title()
            
            if kolom in data_siswa:

                nilai_baru = input(f"Masukkan nilai baru untuk {kolom}: ")
                
                # Yakin ingin mengganti nilai?
                pilihan = input(f"Apakah anda yakin ingin mengubah nilai {kolom} : {data_siswa[kolom]} dengan {kolom} : {nilai_baru} ? tekan [Y] untuk lanjut merubah nilai!")

                # kalau pilihan = ya, lanjut merubah nilai, selain itu keluar
                if pilihan.lower() == 'y':
                    data_siswa[kolom] = nilai_baru
                    print("Data siswa berhasil diubah!")
                else:
                    print("Nilai tidak jadi diubah!")
                    break
            else:
                print("Kolom tidak valid.")
            break
    else:
        print("Siswa dengan NISN tersebut tidak ditemukan.")  

# Fungsi untuk menghapus siswa berdasarkan nama
def hapus_siswa_by_nisn(nisn):
    for data_siswa in siswa:
        if data_siswa['NISN'] == nisn:
            siswa.remove(data_siswa) 
            print("Siswa berhasil dihapus.")
            break 
    else:
        print("Siswa tidak ditemukan.")

# Program utama
while True:
    print("============================================================")
    print("Sistem Manajemen Data Siswa Saint's John School")
    print("1. Tampilkan Siswa")
    print("2. Tambah Siswa")
    print("3. Perbarui Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")
    print("============================================================")

    if pilihan == "1":
      while True:
            print("Sistem Manajemen Data Siswa Saint's John School")
            print("1. Tampilkan Semua Siswa")
            print("2. Cari Siswa")
            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                tampilkan_siswa()
            elif pilihan == "2":
                nisn = input("Masukkan NISN siswa yang akan dicari: ")
                tampilkan_siswa_by_nisn(nisn)
            input_ = input("Apakah anda ingin keluar dari menu ini? [Y]/[N]")
            if input_ == 'Y' or input_ == 'y':
                break
            else:
                continue
    elif pilihan == "2":
      while True:
        nama = input("Masukkan nama siswa: ")
        jenis_kelamin = input("Masukkan jenis kelamin siswa (Pria/Wanita): ")
        agama = input("Masukkan agama siswa: ")
        nisn = input("Masukkan NISN siswa: ")
        kelas = input("Masukkan kelas siswa: ")
        email = input("Masukkan alamat email siswa: ")
        alamat = input("Masukkan alamat siswa: ")
        tambah_siswa(nama, jenis_kelamin, agama, nisn, kelas, email, alamat)
        input_ = input("Apakah anda ingin keluar dari menu ini? [Y]/[N]")
        if input_ == 'Y' or input_ == 'y':
            break
        else:
            continue
    elif pilihan == "3":
        while True:
            nisn = input("Masukkan NISN yang akan diperbarui: ")
            tampilkan_siswa_by_nisn(nisn)
            input_ = input("Apakah anda ingin melanjutkan update siswa? [Y]/[N]")
            if input_.lower() == 'y':
                siswa_ditemukan = perbarui_siswa(nisn)
            else:
                pass
            input_ = input("Apakah anda ingin keluar dari menu ini? [Y]/[N]")
            if input_ == 'Y' or input_ == 'y':
                break
            else:
                continue
    elif pilihan == "4":
        while True:
            nisn = input("Masukkan NISN yang akan dihapus: ")
            input_ = input("Apakah anda ingin melanjutkan hapus data siswa? [Y]/[N]")
            if input_.lower() == 'y':
                hapus_siswa_by_nisn(nisn)
            else:
                pass
            input_ = input("Apakah anda ingin keluar dari menu ini? [Y]/[N]")
            if input_ == 'Y' or input_ == 'y':
                break
            else:
                continue
    elif pilihan == "5":
        print("Sampai Jumpa di Lain Hari & Tetap Semangat ya :)")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang valid.")