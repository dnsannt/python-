# kondisi TRUE contoh ke 1
is_male = True

if is_male: 
    print("You are a male")

# # kondisi False contoh ke 2
is_male = False

if is_male:
    print("You are a male")

# contoh ke 3 kondisi False
is_male = False 

if is_male:
    print("You are a male")
else:
    print("You are not a male")

# contoh ke 4 kondisi True
is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")

# contoh ke 5 kondisi TRUE semua
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

# contoh ke 6 kondisi TRUE or False
is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

# contoh ke 7 kondisi False semua
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

# contoh ke 8 kondisi dengan AND
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not or both ")

# contoh ke 9 
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")
