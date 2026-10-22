
teks = "Python untuk data. Python untuk pendidikan."
teks = teks.lower()
kata = "python"

print("Kata ditemukan:", kata in teks)
print("Jumlah kemunculan:", teks.count(kata))
print("Posisi kemunculan pertama:", teks.find(kata))
