def euclidean():
    b = 1
    a = 0
    while(b>a):
        a = int(input("a: "))
        b = int(input("b: "))
        if(b>a):
            print("b cant be greater than a")
    
      
    while b != 0:
        t = b
        b = a%b
        a = t
    print("НОД = ", a)
    return a

def euclidean_binary():
    b = 1
    a = 0
    while(b>a):
        a = int(input("a: "))
        b = int(input("b: "))
        if(b>a):
            print("b cant be greater than a")
    

    g = 1
    while((a % 2 == 0) | (b % 2 == 0)):
        a = a/2
        b = b/2
        g = 2*g
    u = a 
    v = b
    while(u != 0):
            if(u % 2 == 0):
                u = u/2
            if(v % 2 == 0):
                v = v/2
            if(u>=v):
                u = u-v
            else:
                v = v-u
    d = g*v
    print("НОД = ",d)
        
def euclidean_extended():
    b = 1
    a = 0
    while(b>a):
        a = int(input("a: "))
        b = int(input("b: "))
        if(b>a):
            print("b cant be greater than a")

    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1

    while b != 0:
        t = b
        q = a // b
        print(q)
        b = a%b
        a = t
        t_x = x1
        x1 = x0 - q*x1
        x0 = t_x
        t_y = y1
        y1 = y0 - q*y1
        y0 = t_y

    print("НОД = ", a)
    print("коэффициенты Безу: ", x0,y0)

def euclidean_binary_extended():
    b = 1
    a = 0
    while(b>a):
        a = int(input("a: "))
        b = int(input("b: "))
        if(b>a):
            print("b cant be greater than a")
    
    g = 1
    while((a % 2 == 0) | (b % 2 == 0)):
        a = a/2
        b = b/2
        g = 2*g
    u = a 
    v = b
    A = D = 1
    B = C = 0
    while(u != 0):
            while(u % 2 == 0):
                u = u/2
                if((A % 2 == 0) & (B % 2 == 0)):
                    A = A/2
                    B = B/2
                else:
                    A = (A+v)/ 2
                    B = (B-u)/ 2
            while(v % 2 == 0):
                v = u/2
                if((C % 2 == 0) & (D % 2 == 0)):
                    A = A/2
                    B = B/2
                else:
                    C = (C+v)/ 2
                    D = (D-u)/ 2
            if(u>=v):
                u = u-v
                A = A - C
                B = B - D
            else:
                v = v - u
                C = C - A
                D = D - B
    d = g*v
    
    print("НОД = ",d)
    print("коэффициенты Безу: ",C,D)



euclidean()
euclidean_extended()
euclidean_binary()
euclidean_binary_extended()