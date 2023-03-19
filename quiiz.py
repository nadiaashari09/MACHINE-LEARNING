import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from pandas import DataFrame

readFile = pd.read_csv("soal.csv")
dataBersih = pd.read_csv("soal.csv")
dataBersih.loc[2] = ["B456", "kaos", 8, "sandang"]
dataBersih.loc[3] = ["B457", "sabuk", 9, "sandang"]
dataBersih.loc[4] = ["B455", "anduk", 17, "sandang"]
dataBersih.loc[7] = ["B126", "sate", 16, "pangan"]
dataBersih.loc[8] = ["B447", "celana", 20, "sandang"]

while True:
    print("Menu")
    print("1. Print Data")
    print("2. Hitung Missing Value")
    print("3. Ubah data ke numerik")
    print("4. prosess feature scalling")
    print("0. exit")
    pilihan = input("Pilih: ")
    if pilihan == "1":
        print(readFile)

    elif pilihan == "2":
        daftarKolom = []
        index = 0
        for namaKolom in readFile:
            daftarKolom.append(namaKolom)
            print(f"{index}. {namaKolom}")
            index+=1
        
        inputIndex = int(input("Pilih Kolom : "))
        namaKolom = daftarKolom[inputIndex]
        jumlahMiss = readFile[namaKolom].isnull().sum()
        print(f"Data missing pada kolom {namaKolom} adalah {jumlahMiss}")

    elif pilihan == "3":
        LabelEncoder = LabelEncoder()
        for col in dataBersih.columns.values:
            if dataBersih[col].dtypes == 'object':
                data = dataBersih[col].append(dataBersih[col])
                LabelEncoder.fit(data.values)
                dataBersih[col]= LabelEncoder.transform(dataBersih[col])
        print(dataBersih)
    elif pilihan == "4":
        try:
            scale = MinMaxScaler()
            label = ['kode_barang',' nama_barang', ' jumlah_barang',' jenis_barang']
            loc = dataBersih.loc[0:, label]
            loc = scale.fit_transform(loc)
            dataBersih.loc[0:, label] = loc
            print(dataBersih)
        except:
            print("\nubah data ke numerik dulu!")


    elif pilihan == "0":
        break

