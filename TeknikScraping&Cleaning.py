#!/usr/bin/env python
# coding: utf-8

# In[7]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


url = 'https://id.wikipedia.org/wiki/Daftar_negara_menurut_jumlah_penduduk'
headers = {'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=headers)
html_text = urlopen(req)
soup = BeautifulSoup(html_text, 'html.parser')

print(soup.title.text) 


# In[3]:


tabel = soup.findAll('table', {'class': 'wikitable'})[0]
baris = tabel.findAll('tr')


# In[4]:


tampiltabel = []

for row in baris:
    info = []
    for cell in row.findAll(['td', 'th']):
        info.append(cell.get_text().strip())
    tampiltabel.append(info)


# In[5]:


df = pd.DataFrame(tampiltabel)
display(df)


# In[6]:


import pandas as pd

df = pd.read_csv('datapendudukdunia.csv')
df.head()  # Menampilkan 5 baris pertama


# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[12]:


import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('datapendudukdunia.csv', encoding='utf-8')

df


# In[13]:


df.info()


# In[14]:


df.isnull()


# In[16]:


df.isnull().any()


# In[17]:


df.isnull().sum()


# In[19]:


df['Peringkat'].unique()


# In[20]:


df['Negara(atau wilayah dependen)'].unique()


# In[21]:


df['Populasi'].unique()


# In[22]:


df['Tanggal'].unique()


# In[27]:


df.columns = df.columns.str.strip().str.replace(' +', ' ', regex=True)
df.rename(columns={'% dari penduduk dunia': 'Persentase Penduduk'}, inplace=True)


# In[28]:


print(df.columns)


# In[29]:


df['Persentase Penduduk'].unique()


# In[30]:


df['Sumber'].unique()


# In[40]:


import pandas as pd

# Tampilkan semua baris
pd.set_option('display.max_rows', None)

# Tampilkan semua kolom (jika banyak kolom)
pd.set_option('display.max_columns', None)

# Baca CSV
df = pd.read_csv('datapendudukdunia.csv', encoding='utf-8')

# Tampilkan sebagai tabel rapi
df


# In[41]:


import pandas as pd
from dateutil import parser

# Data mentah
tanggal_list = [
    "Juni 15, 2025", "22-Apr-25", "1 Juli 2022", "1 Januari 2018",
    "Juli 1,2021", "September,9 2021", "Semptember 9, 2021", "01-Apr-18",
    "31 Desember 2017", "1 Juli 2017", "30-Apr-18", "1 Januari 2015"
    # tambahkan semua datamu di sini
]

# Buat DataFrame
df = pd.DataFrame(tanggal_list, columns=["Tanggal"])

# Mapping bulan ke Bahasa Indonesia
bulan_indonesia = {
    1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April',
    5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus',
    9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
}

# Fungsi untuk parsing dan konversi format
def format_tanggal_indonesia(tgl):
    try:
        tgl = tgl.replace(",", " ").replace("Semptember", "September").strip()
        dt = parser.parse(tgl, dayfirst=True)
        return f"{dt.day:02d} {bulan_indonesia[dt.month]} {dt.year}"
    except:
        return "Format Tidak Valid"

# Terapkan ke kolom baru
df["Tanggal_Normal"] = df["Tanggal"].apply(format_tanggal_indonesia)

# Tampilkan hasil
print(df)


# In[42]:


df


# In[43]:


import pandas as pd
from dateutil import parser
import re

# Contoh data
tanggal_list = [
    "Juni 15, 2025", "22-Apr-25", "1 Juli 2022", "1 Januari 2018",
    "Juli 1,2021", "September,9 2021", "Semptember 9, 2021",
    "01-Apr-18", "31 Desember 2017", "1 Juli 2017",
    "30-Apr-18", "1 Januari 2015"
]

df = pd.DataFrame(tanggal_list, columns=["Tanggal"])

# Mapping bulan Indonesia → Inggris untuk parsing
bulan_indo_to_eng = {
    'Januari': 'January',
    'Februari': 'February',
    'Maret': 'March',
    'April': 'April',
    'Mei': 'May',
    'Juni': 'June',
    'Juli': 'July',
    'Agustus': 'August',
    'September': 'September',
    'Oktober': 'October',
    'November': 'November',
    'Desember': 'December'
}

# Mapping bulan angka → Indonesia untuk output akhir
bulan_angka_to_indo = {
    1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April',
    5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus',
    9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
}

def format_tanggal_indonesia(tgl):
    try:
        # Perbaiki typo
        tgl = tgl.replace("Semptember", "September")

        # Ganti bulan Indonesia → Inggris
        for indo, eng in bulan_indo_to_eng.items():
            pattern = re.compile(rf'\b{indo}\b', re.IGNORECASE)
            tgl = pattern.sub(eng, tgl)

        # Parsing tanggal
        dt = parser.parse(tgl, dayfirst=True)
        
        # Format kembali ke Bahasa Indonesia
        return f"{dt.day:02d} {bulan_angka_to_indo[dt.month]} {dt.year}"
    
    except Exception as e:
        return "Format Tidak Valid"

df["Tanggal_Normal"] = df["Tanggal"].apply(format_tanggal_indonesia)
print(df)


# In[44]:


df


# In[45]:


print(df['Tanggal_Normal'].unique())


# In[46]:


df[['Tanggal', 'Tanggal_Normal']]


# In[48]:


import pandas as pd
from datetime import datetime

# Atur tampilan agar semua baris dan kolom terlihat
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Baca data
df = pd.read_csv('datapendudukdunia.csv', encoding='utf-8')

# Buat mapping nama bulan Indonesia
bulan_dict = {
    '01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April',
    '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus',
    '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'
}

# Fungsi untuk mengubah berbagai format tanggal menjadi format: DD Bulan YYYY
def normalisasi_tanggal(tanggal):
    # Coba beberapa format umum
    format_umum = [
        '%d %B %Y', '%B %d, %Y', '%d-%b-%y', '%d-%b-%Y',
        '%d %B,%Y', '%B,%d %Y', '%B %d,%Y', '%d-%m-%Y', '%Y-%m-%d'
    ]
    for fmt in format_umum:
        try:
            dt = datetime.strptime(tanggal.strip(), fmt)
            return f"{dt.day:02d} {bulan_dict[dt.strftime('%m')]} {dt.year}"
        except:
            continue
    return 'Format Tidak Valid'

# Terapkan fungsi ke kolom Tanggal
df['Tanggal_Normal'] = df['Tanggal'].apply(normalisasi_tanggal)

# Tampilkan hanya kolom tanggal dan hasil normalisasi
print(df[['Tanggal', 'Tanggal_Normal']])


# In[51]:


df.loc[df['Tanggal'] == 'Semptember 9, 2021', 'Tanggal_Normal'] = '9 September 2021'


# In[52]:


print(df[['Tanggal', 'Tanggal_Normal']])


# In[53]:


df.loc[(df['Tanggal'] == '9 September 2021') & (df['Tanggal_Normal'] == 'Format Tidak Valid'), 'Tanggal_Normal'] = '09 September 2021'


# In[54]:


print(df[['Tanggal_Normal']])


# In[55]:


print(df.info())


# In[56]:


print(df.columns)


# In[57]:


import pandas as pd

# Supaya semua kolom dan baris tampil dengan rapi
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Tampilkan isi tabel (misalnya 10 baris pertama)
print(df[['Peringkat', 
          'Negara(atau wilayah dependen)', 
          'Populasi', 
          'Tanggal',
          'Tanggal_Normal',
          '% dari  penduduk dunia', 
          'Sumber']].head(10))  # ganti .head(10) jadi .to_string(index=False) jika ingin semua & tanpa index


# In[58]:


import pandas as pd

# Tampilkan semua baris dan kolom
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Tampilkan seluruh DataFrame sebagai tabel
display(df)


# In[59]:


df.loc[(df['Tanggal'] == '21 Sep 2021') & (df['Tanggal_Normal'] == 'Format Tidak Valid'), 'Tanggal_Normal'] = '21 September 2021'


# In[60]:


df.loc[(df['Tanggal'] == 'Mei 2021') & (df['Tanggal_Normal'] == 'Format Tidak Valid'), 'Tanggal_Normal'] = '11 Mei 2021'


# In[61]:


display(df)


# In[64]:


print(df.columns.tolist())


# In[66]:


df = df.rename(columns={
    '% dari  penduduk dunia': 'Persentase Penduduk'
})


# In[67]:


df = df[['Peringkat',
         'Negara(atau wilayah dependen)',
         'Populasi',
         'Tanggal',
         'Tanggal_Normal',
         'Persentase Penduduk',
         'Sumber']]


# In[68]:


display(df)


# In[69]:


print(df['Peringkat'].unique())


# In[70]:


import re

# Hilangkan teks dalam tanda kurung siku
df['Negara(atau wilayah dependen)'] = df['Negara(atau wilayah dependen)'].replace(r"\[.*?\]", "", regex=True).str.strip()


# In[71]:


display(df)


# In[73]:


import re

def bersihkan_populasi(val):
    if pd.isnull(val):
        return pd.NA
    val = str(val)
    # Hilangkan semua titik (.) dan koma (,) sebagai pemisah ribuan
    val = re.sub(r'[.,]', '', val)
    try:
        return int(val)
    except:
        return pd.NA

# Terapkan ke kolom Populasi
df['Populasi'] = df['Populasi'].apply(bersihkan_populasi)


# In[74]:


print(df['Populasi'].head(10))  # Lihat 10 teratas
print(df['Populasi'].isnull().sum())  # Berapa yang tidak berhasil dibersihkan


# In[75]:


display(df)


# In[76]:


df['Populasi'] = df['Populasi'].apply(lambda x: f"{x:,}".replace(",", ".") if pd.notnull(x) else pd.NA)


# In[77]:


display(df)


# In[78]:


df.drop(columns=['Tanggal'], inplace=True)


# In[79]:


print(df.columns)


# In[80]:


df.rename(columns={'Tanggal_Normal': 'Tanggal'}, inplace=True)


# In[81]:


display(df)


# In[83]:


print(df["Populasi"].dtype)


# In[84]:


# Hilangkan titik/komanya dan ubah ke float
df["Populasi"] = df["Populasi"].astype(str).str.replace(".", "", regex=False)
df["Populasi"] = df["Populasi"].str.replace(",", "", regex=False)
df["Populasi"] = pd.to_numeric(df["Populasi"], errors='coerce')


# In[85]:


print(df["Populasi"].isna().sum())


# In[86]:


import matplotlib.pyplot as plt
plt.boxplot(df["Populasi"].dropna())  # drop NaN sebelum plot
plt.title("Boxplot Populasi")
plt.ylabel("Jumlah Populasi")
plt.show()


# In[87]:


display(df)


# In[105]:


display(df)


# In[106]:


import pandas as pd
from dateutil import parser

# Data mentah
tanggal_list = [
    "Juni 15, 2025", "22-Apr-25", "1 Juli 2022", "1 Januari 2018",
    "Juli 1,2021", "September,9 2021", "Semptember 9, 2021", "01-Apr-18",
    "31 Desember 2017", "1 Juli 2017", "30-Apr-18", "1 Januari 2015"
    # tambahkan semua datamu di sini
]

# Buat DataFrame
df = pd.DataFrame(tanggal_list, columns=["Tanggal"])

# Mapping bulan ke Bahasa Indonesia
bulan_indonesia = {
    1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April',
    5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus',
    9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
}

# Fungsi untuk parsing dan konversi format
def format_tanggal_indonesia(tgl):
    try:
        tgl = tgl.replace(",", " ").replace("Semptember", "September").strip()
        dt = parser.parse(tgl, dayfirst=True)
        return f"{dt.day:02d} {bulan_indonesia[dt.month]} {dt.year}"
    except:
        return "Format Tidak Valid"

# Terapkan ke kolom baru
df["Tanggal_Normal"] = df["Tanggal"].apply(format_tanggal_indonesia)

# Tampilkan hasil
print(df)


# In[107]:


df


# In[108]:


import pandas as pd
from datetime import datetime

# Atur tampilan agar semua baris dan kolom terlihat
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Baca data
df = pd.read_csv('datapendudukdunia.csv', encoding='utf-8')

# Buat mapping nama bulan Indonesia
bulan_dict = {
    '01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April',
    '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus',
    '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'
}

# Fungsi untuk mengubah berbagai format tanggal menjadi format: DD Bulan YYYY
def normalisasi_tanggal(tanggal):
    # Coba beberapa format umum
    format_umum = [
        '%d %B %Y', '%B %d, %Y', '%d-%b-%y', '%d-%b-%Y',
        '%d %B,%Y', '%B,%d %Y', '%B %d,%Y', '%d-%m-%Y', '%Y-%m-%d'
    ]
    for fmt in format_umum:
        try:
            dt = datetime.strptime(tanggal.strip(), fmt)
            return f"{dt.day:02d} {bulan_dict[dt.strftime('%m')]} {dt.year}"
        except:
            continue
    return 'Format Tidak Valid'

# Terapkan fungsi ke kolom Tanggal
df['Tanggal_Normal'] = df['Tanggal'].apply(normalisasi_tanggal)

# Tampilkan hanya kolom tanggal dan hasil normalisasi
print(df[['Tanggal', 'Tanggal_Normal']])


# In[109]:


df.loc[df['Tanggal'] == 'Semptember 9, 2021', 'Tanggal_Normal'] = '9 September 2021'


# In[110]:


print(df[['Tanggal_Normal']])


# In[111]:


print(df.info())


# In[112]:


print(df.columns)


# In[113]:


import pandas as pd

# Supaya semua kolom dan baris tampil dengan rapi
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Tampilkan isi tabel (misalnya 10 baris pertama)
print(df[['Peringkat', 
          'Negara(atau wilayah dependen)', 
          'Populasi', 
          'Tanggal',
          'Tanggal_Normal',
          '% dari  penduduk dunia', 
          'Sumber']].head(10))  # ganti .head(10) jadi .to_string(index=False) jika ingin semua & tanpa index


# In[114]:


import pandas as pd

# Tampilkan semua baris dan kolom
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Tampilkan seluruh DataFrame sebagai tabel
display(df)


# In[115]:


df.loc[(df['Tanggal'] == '21 Sep 2021') & (df['Tanggal_Normal'] == 'Format Tidak Valid'), 'Tanggal_Normal'] = '21 September 2021'


# In[116]:


df.loc[(df['Tanggal'] == 'Mei 2021') & (df['Tanggal_Normal'] == 'Format Tidak Valid'), 'Tanggal_Normal'] = '11 Mei 2021'


# In[117]:


display(df)


# In[118]:


print(df['Peringkat'].unique())


# In[119]:


import re

df['Negara(atau wilayah dependen)'] = df['Negara(atau wilayah dependen)'].replace(r"\[.*?\]", "", regex=True).str.strip()


# In[120]:


display(df)


# In[121]:


import re

def bersihkan_populasi(val):
    if pd.isnull(val):
        return pd.NA
    val = str(val)
    # Hilangkan semua titik (.) dan koma (,) sebagai pemisah ribuan
    val = re.sub(r'[.,]', '', val)
    try:
        return int(val)
    except:
        return pd.NA

# Terapkan ke kolom Populasi
df['Populasi'] = df['Populasi'].apply(bersihkan_populasi)


# In[122]:


print(df['Populasi'].head(10))  # Lihat 10 teratas
print(df['Populasi'].isnull().sum())  # Berapa yang tidak berhasil dibersihkan


# In[123]:


display(df)


# In[124]:


df['Populasi'] = df['Populasi'].apply(lambda x: f"{x:,}".replace(",", ".") if pd.notnull(x) else pd.NA)


# In[125]:


display(df)


# In[126]:


df.drop(columns=['Tanggal'], inplace=True)


# In[127]:


print(df.columns)


# In[128]:


df.rename(columns={'Tanggal_Normal': 'Tanggal'}, inplace=True)


# In[129]:


display(df)


# In[134]:


df = df[['Peringkat',
         'Negara(atau wilayah dependen)',
         'Populasi',
         '% dari  penduduk dunia',
         'Sumber',
         'Tanggal']]


# In[135]:


display(df)


# In[136]:


df = df.rename(columns={
    '% dari  penduduk dunia': 'Persentase Penduduk'
})


# In[137]:


display(df)


# In[138]:


df.to_csv('data_penduduk_dunia_bersih.csv', index=False)


# In[139]:


import os
print(os.getcwd())


# In[140]:


import pandas as pd

# Ubah kolom 'Tanggal' ke format datetime
df['Tanggal'] = pd.to_datetime(df['Tanggal'], dayfirst=True, errors='coerce')

# Format ulang menjadi 'tanggal bulan tahun' (dalam Bahasa Indonesia)
df['Tanggal'] = df['Tanggal'].dt.strftime('%d %B %Y')

# Simpan ke file CSV
df.to_csv('data_penduduk_fix.csv', index=False)


# In[141]:


import pandas as pd


# In[142]:


# Ubah kolom 'Tanggal' ke format datetime
df['Tanggal'] = pd.to_datetime(df['Tanggal'], dayfirst=True, errors='coerce')


# In[143]:


# Format ulang menjadi 'tanggal bulan tahun' (dalam Bahasa Indonesia)
df['Tanggal'] = df['Tanggal'].dt.strftime('%d %B %Y')


# In[144]:


# Simpan ke file CSV
df.to_csv('data_penduduk_fix.csv', index=False)


# In[145]:


from dateutil import parser
import pandas as pd

def parse_tanggal_manual(x):
    try:
        return parser.parse(x, dayfirst=True)
    except:
        return pd.NaT  # kalau tidak bisa di-parse, jadikan kosong (NaT)

# Terapkan parsing manual
df['Tanggal'] = df['Tanggal'].astype(str).apply(parse_tanggal_manual)

# Format ke 'tanggal bulan tahun' setelah semua berhasil di-parse
df['Tanggal'] = df['Tanggal'].dt.strftime('%d %B %Y')


# In[146]:


display(df)


# In[147]:


from dateutil import parser

def parse_tanggal(x):
    try:
        return parser.parse(x, dayfirst=True)
    except:
        return pd.NaT

df['Tanggal'] = df['Tanggal'].apply(parse_tanggal)


# In[148]:


df['Tanggal'] = df['Tanggal'].dt.strftime('%d %B %Y')


# In[149]:


display(df)


# In[1]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


df = pd.read_csv('data_penduduk_dunia_bersih.csv')
  


# In[3]:


display(df)


# In[4]:


df.head()


# In[5]:


df = pd.read_csv('data_penduduk_dunia_bersih.csv', encoding='utf-8')



# In[6]:


df.head()


# In[8]:


import pandas as pd

# 1. Baca CSV; pakai utf-8 jika ada karakter khusus, atau coba tanpa encoding jika sederhana
df = pd.read_csv('data_penduduk_dunia_bersih.csv', encoding='utf-8')

# 2a. Tampilkan 5 baris pertama dengan tampilan “baku”
print(df.head())

# 2b. (Jupyter) Cukup tulis nama variabel, Jupyter akan render tabel rapi
df


# In[10]:


import pandas as pd

df = pd.read_csv(
    'data_penduduk_dunia_bersih.csv',
    sep=';',           # gunakan titik-koma sebagai delimiter
    encoding='utf-8'   # atau 'latin-1' jika muncul error unicode
)

df.head(100)


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

# Contoh data (masukkan sesuai struktur yang kamu miliki)
data = {
    'Negara': ['India', 'Tiongkok', 'Amerika Serikat', 'Indonesia', 'Pakistan',
               'Nigeria', 'Brasil', 'Bangladesh', 'Rusia', 'Meksiko',
               'Tuvalu', 'Nauru', 'Palau', 'Vatikan', 'Niue',
               'Tokelau', 'Montserrat', 'Pitcairn', 'Saint Helena', 'San Marino'],
    'Persentase Penduduk': [18.0, 17.9, 4.31, 3.46, 2.93,
                             2.63, 2.77, 2.23, 1.83, 1.58,
                             0.00013, 0.00013, 0.00022, 0.00001, 0.00002,
                             0.000019, 0.000061, 0.00000062, 0.00007, 0.00042]
}

# Buat DataFrame
df = pd.DataFrame(data)

# Konversi ke numeric (jika persentase disimpan sebagai string)
df['Persentase Penduduk'] = pd.to_numeric(df['Persentase Penduduk'], errors='coerce')

# 10 Terbesar
top10 = df.sort_values(by='Persentase Penduduk', ascending=False).head(10)

# 10 Terkecil
bottom10 = df.sort_values(by='Persentase Penduduk', ascending=True).head(10)

# Visualisasi 10 terbesar
plt.figure(figsize=(10,6))
plt.barh(top10['Negara'], top10['Persentase Penduduk'], color='green')
plt.xlabel('Persentase Penduduk (%)')
plt.title('10 Negara dengan Persentase Penduduk Terbesar')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Visualisasi 10 terkecil
plt.figure(figsize=(10,6))
plt.barh(bottom10['Negara'], bottom10['Persentase Penduduk'], color='red')
plt.xlabel('Persentase Penduduk (%)')
plt.title('10 Negara dengan Persentase Penduduk Terkecil')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[12]:


# Donut chart untuk 10 negara dengan penduduk terbesar
plt.figure(figsize=(8,8))
plt.pie(top10['Persentase Penduduk'], labels=top10['Negara'], 
        autopct='%1.1f%%', startangle=140, pctdistance=0.85, colors=plt.cm.tab10.colors)

# Buat lingkaran putih di tengah agar jadi bentuk donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Donut Chart: Kontribusi 10 Negara Terbesar terhadap Populasi Dunia')
plt.tight_layout()
plt.show()



# In[13]:


# Semua negara diurutkan dari besar ke kecil
sorted_df = df.sort_values(by='Persentase Penduduk', ascending=False)

plt.figure(figsize=(12,6))
plt.bar(sorted_df['Negara'], sorted_df['Persentase Penduduk'], color='skyblue')
plt.xticks(rotation=90)
plt.ylabel('Persentase Penduduk (%)')
plt.title('Bar Plot: Ranking Negara berdasarkan Persentase Penduduk ')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()



# In[14]:


top15 = df.sort_values(by='Persentase Penduduk', ascending=False).head(15)

plt.figure(figsize=(10,6))
plt.hlines(y=top15['Negara'], xmin=0, xmax=top15['Persentase Penduduk'], color='grey', alpha=0.7)
plt.plot(top15['Persentase Penduduk'], top15['Negara'], "o", color='dodgerblue')
plt.xlabel('Persentase Penduduk (%)')
plt.title('Lollipop Chart: 15 Negara dengan Populasi Terbesar')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# In[ ]:




