import os
from mobil import SQLDataMobil
from login_register import access, begin, login, register
from layanan_transaksi import Layanan
# from transaksi import Transaksi

def main():
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    
    print("SELAMAT DATANG DI DEALER KAMI")
    print("\n=============================")

    db_name = "servismobil"
    mobil_table_name = "mobil"
    transaksi_table_name = "transaksi"
    layanan_table_name = "layanan_servis"

    mobil_data = SQLDataMobil(db_name, mobil_table_name)
    layanan = Layanan(db_name, layanan_table_name, transaksi_table_name)


    while True:
        print("\nPilihan Menu:")
        print("1. Login/Register")
        print("2. Input Mobil")
        print("3. Input Layanan Servis")
        print("4. Keluar")

        choice = input("Masukkan pilihan (1-5): ")

        if choice == "1":
            access()
        elif choice == "2":
            mobil_data.input_data()
        elif choice == "3":
            layanan.pilih_layanan()
            layanan.hitung_total_biaya()
        elif choice == "4":
            print("Program ditutup.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()