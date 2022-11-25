import math

def p_pollard(n,c,func):
    a = c 
    b = func(c,n)
    count = 0
    while(True):
        a = func(a,n)
        b = func(b,n)
        d = math.gcd(a-b,n) #НОД
        count += 1
        if((d > 1) & (d < n)):
            return d
        elif(d == n): 
            return "делитель не найден"
        if(count>100):
            return "ошибка вычисления"

def func(x,n):
    return (x**2 + 5)%n

print(p_pollard(133,1,func))