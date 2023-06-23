import mysql.connector


def access():
    option = begin()
    if option == "login":
        no_ktp = input("Masukkan Nomor KTP: ")
        nama_customer = input("Masukkan Nama: ")
        login(no_ktp, nama_customer)
    else:
        print("Masukkan Nomor KTP dan Nama anda yang baru")
        no_ktp = input("Masukkan Nomor KTP: ")
        nama_customer = input("Masukkan Nama: ")
        register(no_ktp, nama_customer)
        print("Register Berhasil, Silakan Login")

def begin():
    print("SELAMAT DATANG")
    print("KETIK 'login' JIKA SUDAH PUNYA AKUN")
    print("KETIK 'reg' JIKA BELUM PUNYA AKUN")

    while True:
        option = input("Silakan masukkan (login/reg): ")
        if option == "login" or option == "reg":
            break

    return option

def login(no_ktp, nama_customer):
    
    file = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="servismobil"
    )
    c = file.cursor()

    c.execute("SELECT * FROM customer WHERE no_ktp = %s AND nama_customer = %s", (no_ktp, nama_customer))
    result = c.fetchone()

    if result:
        print("Login Berhasil")
    else:
        print("Anda Belum Terdaftar, Silakan Register")

    file.close()

    return no_ktp

def register(no_ktp, nama_customer):
    file = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="servismobil"
    )
    c = file.cursor()
    c.execute("INSERT INTO customer(no_ktp, nama_customer) VALUES (%s, %s)", (no_ktp, nama_customer))
    file.commit()
    file.close()

    return no_ktp