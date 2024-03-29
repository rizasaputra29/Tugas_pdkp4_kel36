# Fungsi dengan return type dan parameter
def hitung_rata_rata(nilai, jumlah_nilai):
    return nilai / jumlah_nilai

# Metode tanpa return type dan parameter
def cetak_pesan():
    print("Program Penghitungan Kelulusan")

def main():
    cetak_pesan()

    jumlah_nilai = int(input("Masukkan jumlah nilai ujian: "))
    total_nilai = 0

    # Perulangan for untuk menghitung total nilai
    for i in range(jumlah_nilai):
        while True:
            try:
                nilai = float(input(f"Masukkan nilai ujian ke-{i+1}: "))
                if nilai < 0 or nilai > 100:
                    print("Nilai harus berada di antara 0 dan 100.")
                else:
                    total_nilai += nilai
                    break
            except ValueError:
                print("Masukkan nilai yang valid!")

    # fungsi dengan return type
    rata_rata = hitung_rata_rata(total_nilai, jumlah_nilai)

    # pengkondisian if else
    if rata_rata >= 70:
        print("Selamat, Anda lulus!")
    else:
        print("Maaf, Anda tidak lulus.")

if __name__ == "__main__":
    main()
