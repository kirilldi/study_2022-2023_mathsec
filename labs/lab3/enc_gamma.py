alfabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯ"

# Функция переводящяя строку в последовательность из алфавитного номера букв сообщения
def to_number(msg):
    number_arr = []
    for char in msg:
        number_arr.append(alfabet.index(char)+1)
    return number_arr

# Функция переводящяя последовательность из алфавитного номера букв сообщения в строку букв
def to_letters(num_arr):
    letter_arr = []
    for num in num_arr:
        letter_arr.append(alfabet[num-1])
    return letter_arr

# Функция выполняющая шифрование
def encrypt_gamma(msg,key,m):
    code = []
    i = 0
    for num in msg:
        if i == len(key):
            i = 0
        code.append((num + key[i])%m)
        i += 1
    return to_letters(code)

# вызов функций

a = to_number("ПРИКАЗ") # сообщение
b = to_number("ГАММА") # ключ
m = 33
print("Зашифрованное сообщение: ",encrypt_gamma(a,b,m))