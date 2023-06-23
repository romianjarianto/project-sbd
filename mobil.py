import mysql.connector
from customer import CustomerDataInput
from datetime import date, datetime, timedelta

# Kelas dasar untuk input data
class MobilDataInput:
    def __init__(self, db_name):
        self.db_name = db_name

    def input_data(self):
        raise NotImplementedError("Metode input_data harus diimplementasikan!")

    def delete_data(self):
        raise NotImplementedError("Metode delete_data harus diimplementasikan!")

    def update_data(self):
        raise NotImplementedError("Metode update_data harus diimplementasikan!")

    def select_data(self):
        raise NotImplementedError("Metode select_data harus diimplementasikan!")

    def close_program(self):
        print("Program ditutup.")

# Kelas turunan yang menggunakan inheritance
class SQLDataMobil(MobilDataInput):
    def __init__(self, db_name, mobil_table_name):
        super().__init__(db_name)
        self.mobil_table_name = mobil_table_name
        

    def input_data(self):
        # Membuat koneksi ke database
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = self.db_name)

        c = conn.cursor()

        print("\nDATA MOBIL")
        print("==========")
        # Menerima input data dari pengguna
        no_rangka = input("Masukkan nomor rangka mobil: ")
        nama_mobil = input("Masukkan nama mobil: ")
        jenis_mobil = input("Masukkan jenis mobil: ")



        # Menyimpan data ke database
        c.execute(f"INSERT INTO {self.mobil_table_name} (no_rangka, no_ktp, nama_mobil, jenis_mobil) VALUES (%s, %s, %s, %s)", (no_rangka,"", nama_mobil, jenis_mobil))
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
        c.execute(f"SELECT * FROM {self.mobil_table_name}")
        rows = c.fetchall()
        for row in rows:
            print(row)

        # Menerima input data yang akan dihapus
        id_to_delete = int(input("Masukkan ID data yang akan dihapus: "))

        # Menghapus data dari database
        c.execute(f"DELETE FROM {self.mobil_table_name} WHERE id=%s", (id_to_delete,))
        conn.commit()

        # Menampilkan data setelah penghapusan
        print("Data setelah penghapusan:")
        c.execute(f"SELECT * FROM {self.mobil_table_name}")
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
        c.execute(f"SELECT * FROM {self.mobil_table_name}")
        rows = c.fetchall()
        for row in rows:
            print(row)

        # Menerima input data yang akan diperbarui
        id_to_update = int(input("Masukkan ID data yang akan diperbarui: "))
        new_nomor_rangka = input("Masukkan nomor rangka baru: ")
        new_nama_mobil = input("Masukkan nama mobil baru: ")
        new_jenis_mobil = input("Masukkan jenis mobil baru: ")

        # Memperbarui data di database
        c.execute(f"UPDATE {self.mobil_table_name} SET nomor_rangka=%s, nama_mobil=%s, jenis_mobil=%s WHERE id=%s", (new_nomor_rangka, new_nama_mobil, new_jenis_mobil, id_to_update))
        conn.commit()

        # Menampilkan data setelah pembaruan
        print("Data setelah pembaruan:")
        c.execute(f"SELECT * FROM {self.mobil_table_name}")
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
        c.execute(f"SELECT * FROM {self.mobil_table_name}")
        rows = c.fetchall()
        for row in rows:
            print(row)

        # Menutup koneksi database
        conn.close()

