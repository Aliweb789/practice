# O-TASK (PYTHON)
# Shunday function yozing, u har xil valuelardan iborat array qabul qilsin va List ichidagi sonlar yigindisini hisoblab chiqqan javobni qaytarsin.
# MASALAN: calculate_summary([10, "10", {son: 10}, true, 35]) return 45

def calculate_summary(arr):
    numbers = []
    sum = 0
    for item in arr:
        if isinstance(item, (int, float)) and not isinstance(item, (bool)):
            numbers.append(item)
    for i in numbers:
        sum = sum + i
    print(sum)


calculate_summary([10, "13", {"son": 14}, True, 35])


# M-TASK (PYTHON)
# Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham, orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
# MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;

# def palindrom_check(str):
#     new_str = str[::-1]
#     if str == new_str:
#         print(True)
#     else:
#         print(False)

# palindrom_check("nonon")


# K-TASK
# Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin. Masalan: find_longest("I come from Uzbekistan")
# return "Uzbekistan"
# def find_longest(str):
#     new_array = str.split()
#     max_leng = 0
#     for i in new_array:
#         if len(i) > max_leng:
#             max_leng = len(i)
#     for j in new_array:
#         if len(j) == max_leng:
#             print(j)
# find_longest("I come from Uzbekistan")


# I-TASK
# Shunday function tuzing, unga string argument pass bolsin. Function ushbu argumentdagi digitalni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"

# def get_digits(str):
#     new_str = ""
#     for letter in str:
#         if '0' <= letter <= '9':
#             new_str += letter
#     print(new_str)

# get_digits("m14i12t")


# G-Task
# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini

# def get_highest_index(arr):
#     result = max(arr);
#     print(arr.index(result))

# get_highest_index([5, 21, 22, 21, 8])
