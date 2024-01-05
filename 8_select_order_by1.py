import sqlite3
#select all data fauna
bende = sqlite3.connect('database_fauna1.db')

kursor = bende.cursor()
kursor.execute("SELECT * FROM fauna ORDER BY nama_fauna ASC ")

data_fauna = kursor.fetchall()

print("DATA FAUNA")
print("="*120)
print("{:<5} {:<20} {:<20} {:<15} {:<20}{:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))
print("-"*120)

# tampilkan data sesuai format tabel dengan perulangan
for baris in data_fauna:
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

kursor.close