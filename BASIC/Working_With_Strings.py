# FULL INTRODUCTION WITH STRING 
# perintah cetak python working with string 
print("Giraffe Academy CETAK")

# spasi ke bawah
print("Spasi\nKebawah")

# backslash quotaion mark "tanda petik "
print("Dennis\"Academy (PETIK)")

# function menggunakan lower case 
phrase = "Giraffe Academy (LOWER)"
print(phrase.lower())

# test upper true or false CEK APAKAH UPPER ATAU BUKAN
phrase = "Dennis Ananto TRUE OR FALSE"
print(phrase.isupper())

# FUNGSI PYTHON Check upper tidak = benar hasil nya upper 
phrase = "DWIKI SETIAWAN"
print(phrase.upper().isupper())

# menggunakan function uppper 
phrase = "DENNIS ANANTO is COOL"
print(phrase.upper())

# cetak dengan function 
phrase = "Giraffe Academy"
print(phrase + " is cool ")

# HITUNG KARAKTER hasil nya 15 karakter
phrase = "Giraffe Academy"
print(len(phrase))

# HASIL NYA = G
phrase = "Giraffe Academy"
print(phrase[2])
# phrase ="Giraffe Academy"
#          0123456
# print(phrase[0])

# mencari nilai karakter di value 0-1000 
phrase = "Giraffe Academy"
print(phrase.index("Acad"))

# replace
phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant"))

