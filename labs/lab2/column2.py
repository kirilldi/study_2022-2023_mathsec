
from numpy import sort


msg_str = "договор подписали"
m = 4 #кол-во блоков
n = 4 # длина блоков
password = "шифр"
def get_input():
    msg_str = input("введите сообщение:", )
    m = input("введите кол-во блоков:",)
    n = input("введите длину блоков:",)
    return(msg_str,m,n)

msg = list()
for char in msg_str:
    if char == ' ': continue
    msg.append(char)
msg_split = list()
for i in range(0, len(msg), n):
    msg_split.append(msg[i:i+n])

code = list([])
for i in range(n):
    code.append([])
    for j in range(m):
        code[i].append(msg_split[j][i])

d = dict()
p = list(password)
for i in range(n):
    d[p[i]] = code[i]
    
p.sort()

sorted_code = list()
for char in p:
    sorted_code.append(d[char])

final_code = ""
for i in range(n):
    for j in range(m):
        final_code = final_code + sorted_code[i][j]

print("Encoded message: ",final_code)