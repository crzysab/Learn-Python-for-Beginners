import datetime

x = datetime.datetime.now()

print("Tanggal hari ini : ", x.strftime("%D"))
print("Hari  :", x.strftime("%A"))
print("Bulan :", x.strftime("%B"))

'''
Untuk daftar semua parameter dapat dilihat di google dengan kata kunci "Date formatting methods in python"
'''