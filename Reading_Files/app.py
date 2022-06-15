# r = reading 
# r+ = reading & write
 
# Mode	    Ketereangan
# “r”	        hanya baca saja
# “w”	        akses untuk menulis file, jika file sudah ada, maka file akan di replace dan diganti dengan yang baru ditulis
# “a”	        digunakan untuk append atau menambah data ke file, artinya jika sudah ada data dalam file, maka akan ditambahkan dan tidak di-replace
# “r+”	    digunakan untuk membaca sekaligus menulis data ke file


# CONTOH 1 dengan Read = r
employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "r")
print(employee_file.readable())
employee_file.close()

# CONTOH 2 dengan W = akses untuk menulis file, jika file sudah ada, maka file akan di replace dan diganti dengan yang baru ditulis
# employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "w")
# print(employee_file.readable())
# employee_file.close()

# CONTOH 3 r = Read
employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "r")
print(employee_file.read())
employee_file.close()

# CONTOH 4 dengan readline
employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "r")
print(employee_file.readline())
employee_file.close()

# CONTOH 5 TEKNIK PRINT OUT SETIAP LINE / BARIS
employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "r")
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()

# CONTOH 6 menggunakan REDLINES
employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "r")
print(employee_file.readlines())
employee_file.close()

# CONTOH 7 REDLINES, SQUARE BRACKETS
employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "r")
print(employee_file.readlines()[1])
employee_file.close()

# CONTOH 8 STAFF PSC
data = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/staff.txt", "r")
for staff in data.readlines():
    print(staff)
data.close()

# CONTOH 9
employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()