# Program Input Nilai
# ======================

data_nilai = {}

def tampilkan_data():
    if len(data_nilai) == 0:
        print("\nDaftar Nilai")
        print("======================================================")
        print("| NO |   NIM   |    NAMA    | TUGAS | UTS | UAS | AKHIR |")
        print("|----|---------|------------|-------|-----|-----|-------|")
        print("|                      TIDAK ADA DATA                  |")
        print("======================================================\n")
    else:
        print("\nDaftar Nilai")
        print("======================================================")
        print("| NO |   NIM   |    NAMA    | TUGAS | UTS | UAS | AKHIR |")
        print("======================================================")
        for i, (nim, data) in enumerate(data_nilai.items(), start=1):
            print(f"| {i:2} | {nim:7} | {data['nama']:<10} | {data['tugas']:5} | {data['uts']:3} | {data['uas']:3} | {data['akhir']:5.2f} |")
        print("======================================================\n")

def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = int(input("Nilai Tugas: "))
    uts = int(input("Nilai UTS: "))
    uas = int(input("Nilai UAS: "))
    akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_nilai[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": akhir}
    print("Data berhasil ditambahkan!\n")

def ubah_data():
    nim = input("Masukkan NIM yang akan diubah: ")
    if nim in data_nilai:
        print(f"Data ditemukan: {data_nilai[nim]}")
        nama = input("Masukkan Nama baru: ")
        tugas = int(input("Nilai Tugas baru: "))
        uts = int(input("Nilai UTS baru: "))
        uas = int(input("Nilai UAS baru: "))
        akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        data_nilai[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": akhir}
        print("Data berhasil diubah!\n")
    else:
        print("Data tidak ditemukan!\n")

def hapus_data():
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in data_nilai:
        del data_nilai[nim]
        print("Data berhasil dihapus!\n")
    else:
        print("Data tidak ditemukan!\n")

def cari_data():
    nim = input("Masukkan NIM yang akan dicari: ")
    if nim in data_nilai:
        print("\nHasil Pencarian:")
        print("======================================================")
        print("|   NIM   |    NAMA    | TUGAS | UTS | UAS | AKHIR |")
        print("======================================================")
        data = data_nilai[nim]
        print(f"| {nim:7} | {data['nama']:<10} | {data['tugas']:5} | {data['uts']:3} | {data['uas']:3} | {data['akhir']:5.2f} |")
        print("======================================================\n")
    else:
        print("Data tidak ditemukan!\n")

while True:
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:")
    pilihan = input("Pilih menu: ").lower()
    if pilihan == "l":
        tampilkan_data()
    elif pilihan == "t":
        tambah_data()
    elif pilihan == "u":
        ubah_data()
    elif pilihan == "h":
        hapus_data()
    elif pilihan == "c":
        cari_data()
    elif pilihan == "k":
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid, silakan pilih menu yang tersedia!\n")
