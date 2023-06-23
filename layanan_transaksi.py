import mysql.connector
from datetime import datetime
from login_register import access, register

class Layanan:
    def __init__(self, db_name, layanan_table_name, transaksi_table_name):
        self.db_name = db_name
        self.layanan_table_name = layanan_table_name
        self.transaksi_table_name = transaksi_table_name
        self.layanan_terpilih = []
    

    def pilih_layanan(self):
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = self.db_name
        )
        cursor = connection.cursor()

        while True:
            self.tampilkan_layanan(cursor)

            layanan_id = input("Masukkan ID layanan yang ingin dipilih (0 untuk selesai): ")
            if layanan_id == "0":
                break

            query = f"SELECT * FROM {self.layanan_table_name} WHERE id_layanan = {layanan_id}"
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                self.layanan_terpilih.append(result)
                print("Layanan berhasil dipilih.")
            else:
                print("ID layanan tidak valid. Silakan coba lagi.")

        connection.close()

    def tampilkan_layanan(self, cursor):
        query = f"SELECT * FROM {self.layanan_table_name}"
        cursor.execute(query)
        results = cursor.fetchall()

        print("Pilihan Layanan:")
        for layanan in results:
            print(f"ID: {layanan[0]}, Nama: {layanan[1]}, Estimasi Biaya: Rp {layanan[2]:,}")
        print()


    def hitung_total_biaya(self):
        #Menghitung total Biaya dari sum estimasi_biaya from database
        total_biaya = sum(layanan[2] for layanan in self.layanan_terpilih)
        print("\nLayanan yang dipilih:")
        print("=========================================")

        # Menampilkan layanan yang dipilih yang diambil dari database
        for layanan in self.layanan_terpilih:
            print(f"- {layanan[1]}, Estimasi Biaya: Rp {layanan[2]:,}")
        
        print(f"Total Biaya: Rp {total_biaya:,}")
        print("=========================================")
        print("\n")

        while True:
            jumlah_bayar = float(input("Masukkan jumlah pembayaran: "))
            if jumlah_bayar < total_biaya:
                print("Jumlah pembayaran kurang dari total biaya.")
                print("\n")
            else:
                kembalian = jumlah_bayar - total_biaya
                print(f"Kembalian: Rp {kembalian:,}")
                print("\n=========================================")
                print("\nTERIMA KASIH TELAH MENGGUNAKAN JASA KAMI ^_^")
                print("\n=========================================")
                break


        # Kode untuk menyimpan transaksi ke dalam database
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = self.db_name
        )
        cursor = conn.cursor()

        # Mengakses no_ktp dari fungsi access()
        

        # Insert detail layanan ke dalam tabel detail_layanan
        for layanan in self.layanan_terpilih:
            insert_detail_query = f"INSERT INTO {self.transaksi_table_name} (no_transaksi, no_ktp, id_layanan, tanggal, total_biaya) VALUES (%s, %s, %s, %s, %s)"
            value = ('', '', layanan[0], datetime.now(), total_biaya)
            cursor.execute(insert_detail_query, value)

        conn.commit()
        conn.close()