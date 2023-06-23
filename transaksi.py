from layanan import input_servis_data

class Transaksi:
    def __init__(self, db_name, servis_table_name):
        self.db_name = db_name
        self.servis_table_name = servis_table_name

        self.servis_data = input_servis_data(db_name, servis_table_name)

    def buat_transaksi(self):
        print("=== Transaksi Layanan Servis ===")
        self.servis_data.input_servis_data()

        # Implementasi logika lain untuk transaksi seperti menyimpan data transaksi ke database

        print("Transaksi berhasil dibuat.")
