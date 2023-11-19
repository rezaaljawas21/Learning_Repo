def fungsi(siswa_):
    sisw
    return siswa_['Nama']

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

siswa.sort(key=fungsi)
print(siswa)