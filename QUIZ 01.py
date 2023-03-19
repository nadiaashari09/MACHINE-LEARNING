import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

while True:
    print(60*"=")
    print(28*"=","MENU",26*"=")
    print(60*"=")
    print("1. Menampilkan Data Asli")
    print("2. Jumlah Missing Value")
    print("3. Ubah Data")
    print("4. Feature Scalling")
    print("0. Selesai")
    print(60*"=")
    menu = input("Pilih MENU : ")

    if menu == "1":
        print(60*"=")
        print(22*"=","TAMPILKAN DATA",22*"=")
        print(60*"=")
        read_document = pd.read_csv('soal.csv')
        print(f"\n{read_document}")

    elif menu == "2":
        kolom = []

        for col in read_document:
            kolom.append(col)

        print(60*"=")
        print("Kolom : ", kolom)
        menu = input("Nama Kolom : ")
        print(60*"=")
        print(21*"=","TAMPILKAN KOLOM",22*"=")
        print(60*"=")
        try:
            read_document = read_document[menu]
            print(read_document)
        except :
            print("Data tidak ditemukan")
        
        print(60*"=")
        read_jumlah_Null = read_document.isnull().sum().sum()
        print(f"Missing Value : {read_jumlah_Null}")

    elif menu == "3":
        ubah_data = pd.read_csv('soal.csv')
        LabelEn = LabelEncoder()
        
        for col in ubah_data.columns.values:
            if ubah_data[col].dtypes == 'object':
                data = ubah_data[col].append(ubah_data[col])
                LabelEn.fit(data.values)
                ubah_data[col] = LabelEn.transform(ubah_data[col])
        print(ubah_data)

    elif menu == "4":
        print(60*"=")
        read_data = pd.read_csv('soal.csv')
        print(read_data)
        scaler = MinMaxScaler()
        read_data[' jumlah_barang']= scaler.fit_transform(read_data[[' jumlah_barang']])

        print(60*"=")
        print(read_data)

    elif menu == '0' :
        print("Selesai :)\n")
        break

    else :
        print("\nPilihan Tidak Ada Menu\n")
    input("\nEnter Untuk Melanjutkan......")