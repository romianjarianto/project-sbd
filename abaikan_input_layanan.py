def input_servis_data():

        print("Pilihan Layanan:")
        print("1. Ganti Oli")
        print("2. Poles Kaca")
        print("3. Poles Bodi")
        print("4. Cuci Mobil")
        print("5. Servis AC")

        layanan = input("Masukkan pilihan layanan (1-5): ")

        if layanan == "1":
            jenis_layanan = "Ganti Oli"
            estimasi_biaya = 100000
        elif layanan == "2":
            jenis_layanan = "Poles Kaca"
            estimasi_biaya = 50000
        elif layanan == "3":
            jenis_layanan = "Poles Bodi"
            estimasi_biaya = 200000
        elif layanan == "4":
            jenis_layanan = "Cuci Mobil"
            estimasi_biaya = 75000
        elif layanan == "5":
            jenis_layanan = "Servis AC"
            estimasi_biaya = 300000
        else:
            print("Pilihan layanan tidak valid.")
            return

        print("Data layanan servis berhasil dimasukkan:")
        print("Jenis Layanan:", jenis_layanan)
        print("Estimasi Biaya:", estimasi_biaya)

input_servis_data()