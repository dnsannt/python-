# contoh ke 1
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)

# contoh ke 2 (EXTEND)
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)

# fungsi extend : menambahkan array di last(terakhir)
list1 = [1234, 'abcd', 'efgh', 'xyz', 567];
list2 = [2015, 'dodol'];
list1.extend(list2)
print ("Extended List : ", list1) 

# contoh menggunakan append
aList = [1234, 'abc', 'def', 'ghi'];
aList.append( 5432 );
print ("Hasil append : ", aList)

# contoh ke 3 (APPEND) menambah nilai array pada urutan terakhir
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
print(friends)

# contoh ke 4 (INSERT) salah satu array
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)

# contoh ke 5 (REMOVE) salah satu array
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Kevin")
print(friends)

# contoh ke 5 (CLEAR) hapus seluruh array
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)

# fungsi POP untuk menghapus elemen terakhir array
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Dennis"]
friends.pop()
print(friends)

# fungsi COUNT untuk menjumlahkan ada berapa array
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Kevin", "Karen", "Jim", "Oscar", "Toby", "Dennis"]

print(friends.count("Kevin"))

# fungsi SORT untuk mengurutkan array
lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Kevin", "Karen", "Jim", "Oscar", "Toby", "Dennis"]
friends.sort()
print(friends)

# contoh SORT
test = [0,9,7,7,8,10,12]
test.sort()
print(test)

# contoh sort : mengurutkan data
lucky_numbers = [42, 8, 15, 16, 23]
friends = ["Dennis", "Dwiki", "Fakhrul", "Anam"]
lucky_numbers.sort()
print(lucky_numbers)

# contoh SORT : menggunakan fungsi cetak 2 baris (PRINT)
lucky_numbers = [42, 8, 15, 16, 23]
friends = ["Dennis", "Dwiki", "Fakhrul", "Anam"]
lucky_numbers.sort()
friends.sort()
print(lucky_numbers)
print(friends)

# contoh SORT : fungsi print satu baris. fungsi(+)
lucky_numbers = [42, 8, 15, 16, 23]
friends = ["Dennis", "Dwiki", "Fakhrul", "Anam"]
lucky_numbers.sort()
friends.sort()
print(lucky_numbers + friends) 

# fungsi REVERSE : membalikan nilai array
lucky_numbers = [42, 8, 15, 16, 23]
friends = ["Dennis", "Dwiki", "Fakhrul", "Anam"]
lucky_numbers.reverse()
print(lucky_numbers) 

# REVERRSE
number = [5,4,3,2,1]
number.reverse()
print(number)

# Fungsi COPY berbeda situasi
lucky_number = [42, 8, 15, 16, 23]
friends = ["Kevin", "Keren", "Jim", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()
print(friends2)

