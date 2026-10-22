
def normalisasi_nama(nama):
    """Membersihkan spasi dan merapikan kapitalisasi nama."""
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    """Membuat inisial dari setiap kata pada nama."""
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    """Mengubah kode kelas menjadi huruf besar dan memakai tanda hubung."""
    kata = kode.strip().upper().split()
    return "-".join(kata)


def main():
    nama = input("Nama: ")
    kode = input("Kode kelas: ")

    nama_bersih = normalisasi_nama(nama)
    kode_bersih = normalisasi_kode(kode)
    jumlah_kata = len(nama_bersih.split())
    inisial = buat_inisial(nama_bersih)

    print("\n=== HASIL NORMALISASI DATA MAHASISWA ===")
    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")


if __name__ == "__main__":
    main()
