import os
from customer import SQLDataCustomer
from mobil import SQLDataMobil
# from layanan import ServisData
# from transaksi import Transaksi

def main():
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    
    print("SELAMAT DATANG DI DEALER KAMI")
    print("\n=============================")

    db_name = "servismobil"
    customer_table_name = "customer"
    mobil_table_name = "mobil"
    # servis_table_name = "servis"

    
    customer_data = SQLDataCustomer(db_name, customer_table_name)
    mobil_data = SQLDataMobil(db_name, mobil_table_name)
    # servis_data = ServisData(db_name, servis_table_name)
    # transaksi = Transaksi(db_name, servis_table_name)

    while True:
        print("\nPilihan Menu:")
        print("1. Input Customer")
        print("2. Input Mobil")
        print("3. Input Layanan Servis")
        print("4. Buat Transaksi Layanan Servis")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1-3): ")

        if choice == "1":
            customer_data.input_data()
        elif choice == "2":
            mobil_data.input_data()
        # elif choice == "3":
        #     servis_data.Servisdata()
        # elif choice == "4":
        #     servis_data.Transaksi()
        elif choice == "3":
            print("Program ditutup.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

    # Implementasikan logika program utama
    # Misalnya, tampilkan menu dan menerima input dari pengguna