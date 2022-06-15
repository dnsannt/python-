# CONTOH NUMBER GRID 
# 1,4,7,0 kebawah adalah rows
# 1,2,3  kesamping kanan = kolom 
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[3][0])

# # CONTOH KE 2
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in number_grid:
    print(row)

# CONTOH KE 
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in number_grid:
    for col in row:
        print(col)