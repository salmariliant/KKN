#Aplikasi GUI berbasis streamlit

#import modul yang dibutuhkan
import streamlit as st
import pandas as pd
import plotly.express as px

#Judul
st.title('Data Kependudukan Desa Sukomanah')

#baca data
dataSalma = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSBTUdsckaiDWEKWeyRvknuBOvk7Yu17gxjQ7ZCxF3vHk9SpEc9eOpkK4KVbLNPOJEccJMlG8MrWr43/pub?gid=596766692&single=true&output=csv")
dataSalma['Usia'] = dataSalma['Usia'].astype(int)
dataSalma['No KK'] = dataSalma['No KK'].astype(str).replace('\.0', '', regex=True)
dataSalma['NIK'] = dataSalma['NIK'].astype(str).replace('\.0', '', regex=True)
dataSalma['RT'] = dataSalma['RT'].astype(int)
dataSalma['RW'] = dataSalma['RW'].astype(int)

selectorPendidikan = ['All','TIDAK/BLM SEKOLAH','BELUM TAMAT SD/SEDERAJAT','TAMAT SD/SEDERAJAT','SLTP/SEDERAJAT','SLTA/SEDERAJAT','DIPLOMA I/II','AKADEMI/DIPLOMA III/SARJANA MUDA','DIPLOMA IV/STRATA I','STRATA-II','STRATA-III']
selectorPekerjaan = ['All','KARYAWAN SWASTA','BELUM/TIDAK BEKERJA','PETANI/PEKEBUN','MENGURUS RUMAH TANGGA','PELAJAR/MAHASISWA','BURUH HARIAN LEPAS','WIRASWASTA','PEDAGANG','PERDAGANGAN','PERANGKAT DESA','BURUH TANI/PERKEBUNAN','PEGAWAI NEGERI SIPIL (PNS)','BURUH NELAYAN/PERIKANAN','PENSIUNAN','GURU','TENTARA NASIONAL INDONESIA (TNI)','DOSEN','KARYAWAN HONORER','KARYAWAN BUMN','PEMBANTU RUMAH TANGGA','SOPIR','KEPOLISIAN RI (POLRI)','BIDAN','KEPALA DESA','DOKTER','TUKANG BATU']
selectorUsia = ['All','DI BAWAH 10 TAHUN','10 SAMPAI 19 TAHUN' , '20 SAMPAI 29 TAHUN' , '30 SAMPAI 39 TAHUN' , '40 SAMPAI 49 TAHUN' , '50 SAMPAI 59 TAHUN' , '60 TAHUN KE ATAS']
selectorJK = ['All','Lk','Pr']
selectorRT = ['All',1,2,3]
selectorRW = ['All',1,2,3]

selectPendidikan = st.selectbox('Pilih Pendidikan',selectorPendidikan)
if selectPendidikan == 'All' :
    dataA = dataSalma
else :
    dataA = dataSalma[dataSalma['Pendidikan'] == selectPendidikan]

selectPekerjaan = st.selectbox('Pilih Pekerjaan',selectorPekerjaan)
if selectPekerjaan == 'All' :
    dataB = dataA
else :
    dataB = dataA[dataA['Pekerjaan'] == selectPekerjaan]

selectUsia = st.selectbox('Pilih Rentang Usia',selectorUsia)
if selectUsia == 'All' :
    dataC = dataB
elif selectUsia == 'DI BAWAH 10 TAHUN' :
    dataC = dataB[dataB['Usia'] < 10]
elif selectUsia == '10 SAMPAI 19 TAHUN' :
    dataC = dataB[(dataB['Usia'] < 20) & (dataB['Usia'] > 9)]
elif selectUsia == '20 SAMPAI 29 TAHUN' :
    dataC = dataB[(dataB['Usia'] < 30) & (dataB['Usia'] > 19)]
elif selectUsia == '30 SAMPAI 39 TAHUN' :
    dataC = dataB[(dataB['Usia'] < 40) & (dataB['Usia'] > 29)]
elif selectUsia == '40 SAMPAI 49 TAHUN' :
    dataC = dataB[(dataB['Usia'] < 50) & (dataB['Usia'] > 39)]
elif selectUsia == '50 SAMPAI 59 TAHUN' :
    dataC = dataB[(dataB['Usia'] < 60) & (dataB['Usia'] > 49)]
else :
    dataC = dataB[dataB['Usia'] > 59]

selectJK = st.selectbox('Pilih Jenis Kelamin',selectorJK)
if selectJK == 'All' :
    dataD = dataC
else :
    dataD = dataC[dataC['JK'] == selectJK]

selectRT = st.selectbox('Pilih RT',selectorRT)
if selectRT == 'All' :
    dataE = dataD
else :
    dataE = dataD[dataD['RT'] == selectRT]

selectRW = st.selectbox('Pilih RW',selectorRW)
if selectRW == 'All' :
    dataF = dataE
else :
    dataF = dataE[dataE['RW'] == selectRW]
    
teksA = (str(dataF.shape[0]) + " Penduduk")

listKK = dataSalma['No KK'].values.tolist()
setKK = set(listKK)
teksB = (str(len(setKK)) + " KK")

dataF = dataF.sort_values(by=['Nama Lengkap'])
dataF = dataF.reset_index(drop=True)
dataF = dataF.drop(columns="NO")
dataF.index += 1

'''

'''
dataF
'''

'''
teksA
'''
'''
teksB
'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
by KKN-PPM UGM 2021
'''
