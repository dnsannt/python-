# CONTOH 1
# employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "r")
# print(employee_file.read())
# employee_file.close()

# CONTOH 2 APPEND = untuk menambahkan nilai array
# employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "a")
# employee_file.write("Toby - Human Resources")
# employee_file.close()

# CONTOH 3 APPEND \n = tambah ke bawah line 
# employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/employees.txt", "a")
# employee_file.write("\nKelly - Customer Service")
# employee_file.close()

# CONTOH 4 APPEND dengan W = write , replace data dengan yang baru
# employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/tester.txt", "w")
# employee_file.write("\nTIMPAH DATA YANG LAMA HILANG BRO")
# employee_file.close()

# CONTOH 5 APPEND , NEW FILE TXT (tester123)
# employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/tester123.txt", "w")
# employee_file.write("\notomatis nambah sendiri nih bro file txt nya")
# employee_file.close()

# CONTOH 6 APPEND = menambah file html 
employee_file = open("/Users/dennis/Desktop/Home/Source_Code/Py/Reading_Files/index.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()

