# contoh ke 1
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# menggunakan SQUARE BRACKETS
print(monthConversions["Nov"])
# menggunakan GET
print(monthConversions.get("Dec"))
# DEFAULT VALUE
print(monthConversions.get("Luv", "Not a valid Key"))


# contoh ke 2
monthConversions = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
# menggunakan SQUARE BRACKETS
print(monthConversions["1"])
# menggunakan GET
# print(monthConversions.get("Dec"))
# # DEFAULT VALUE
# print(monthConversions.get("Luv", "Not a valid Key"))
