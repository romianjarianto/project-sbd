import mysql.connector
from datetime import date, datetime, timedelta


# Kelas dasar untuk input data
class CustomerDataInput:
    def __init__(self, db_name):
        self.db_name = db_name

    def input_data(self):
        raise NotImplementedError("Metode input_data harus diimplementasikan!")

    def delete_data(self):
        raise NotImplementedError("Metode delete_data harus diimplementasikan!")

    def update_data(self):
        raise NotImplementedError("Metode update_data harus diimplementasikan!")
            
    def close_program(self):
        print("\nProgram ditutup.")
        

# Kelas turunan yang menggunakan inheritance
class SQLDataCustomer(CustomerDataInput):
    def __init__(self, db_name, customer_table_name):
        super().__init__(db_name)
        self.customer_table_name = customer_table_name

    def input_data(self):
        # Membuat koneksi ke database
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = self.db_name)
        c = conn.cursor()

        print("\nDATA CUSTOMER")
        print("=============")

        # Menerima input data dari pengguna
        no_ktp = int(input("Masukkan Nomor KTP: "))
        nama = str(input("Masukkan Nama: "))
        alamat = str(input("Masukkan Alamat: "))
        
        
        # Menyimpan data ke database
        c.execute(f"INSERT INTO {self.customer_table_name} (no_ktp, nama_customer, alamat_customer) VALUES (%s, %s, %s)", (no_ktp, nama, alamat))
        conn.commit()
        
        # Menutup koneksi database
        conn.close()
        

    def delete_data(self):
        # Membuat koneksi ke database
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = self.db_name)
        c = conn.cursor()

        # Menampilkan data yang ada dalam database
        print("Data saat ini:")
        c.execute(f"SELECT * FROM {self.customer_table_name}")
        rows = c.fetchall()
        for row in rows:
            print(row)

        # Menerima input data yang akan dihapus
        id_to_delete = int(input("Masukkan Nomor KTP yang akan dihapus: "))

        # Menghapus data dari database
        c.execute(f"DELETE FROM {self.customer_table_name} WHERE no_ktp=%s", (id_to_delete,))
        conn.commit()

        # Menampilkan data setelah penghapusan
        print("Data setelah penghapusan:")
        c.execute(f"SELECT * FROM {self.customer_table_name}")
        rows = c.fetchall()
        for row in rows:
            print(row)

        # Menutup koneksi database
        conn.close()

    def update_data(self):
        # Membuat koneksi ke database
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = self.db_name)
        c = conn.cursor()

        # Menampilkan data yang ada dalam database
        print("Data saat ini:")
        c.execute(f"SELECT * FROM {self.customer_table_name}")
        rows = c.fetchall()
        for row in rows:
            print(row)

        # Menerima input data yang akan diperbarui
        no_ktp = int(input("Masukkan Nomor KTP yang akan diperbarui: "))
        new_no_ktp = int(input("Masukkan Nomor KTP baru: "))
        new_nama = input("Masukkan Nama baru: ")
        new_alamat = str(input("Masukkan Alamat baru: "))

        # Memperbarui data di database
        c.execute(f"UPDATE {self.customer_table_name} SET no_ktp=%s, nama_customer=%s, alamat_customer=%s WHERE no_ktp=%s", (new_no_ktp, new_nama, new_alamat, no_ktp))
        conn.commit()

        # Menampilkan data setelah pembaruan
        print("Data setelah pembaruan:")
        c.execute(f"SELECT * FROM {self.customer_table_name}")
        rows = c.fetchall()
        for row in rows:
            print(row)

        # Menutup koneksi database
        conn.close()

    def select_data(self):
        # Membuat koneksi ke database
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = self.db_name)
        c = conn.cursor()

        # Menampilkan data yang ada dalam database
        c.execute(f"SELECT * FROM {self.customer_table_name}")
        rows = c.fetchall()
        for row in rows:
            print(row)

        # Menutup koneksi database
        conn.close()


