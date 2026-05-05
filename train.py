# I-TASK
#Shunday function tuzing, unga string argument pass bolsin. Function ushbu argumentdagi digitalni yangi stringda return qilsin 
#MASALAN: get_digits("m14i1t") return qiladi "141"

def get_digits(str):
    new_str = ""
    for letter in str:
        if '0' <= letter <= '9':
            new_str += letter
    print(new_str)

get_digits("m14i12t")



# G-Task
# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini

# def get_highest_index(arr):
#     result = max(arr);
#     print(arr.index(result))

# get_highest_index([5, 21, 22, 21, 8])

