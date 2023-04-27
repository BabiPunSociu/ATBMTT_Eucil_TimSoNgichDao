
def nhapSoTuNhien(mes):
    while True:
        a = input(mes).strip()
        try:
            a = int(a) 
            if a >= 0: return a 
            else:
                print('Bạn phải nhập số tự nhiên.')
        except ValueError:
            print('Bạn phải nhập số tự nhiên.')

def showMenu():
    print('Chon cac chuc nang sau:')
    print('1. Tim so nghich dao')
    print('2. tim so nghich dao (co bang)')
    print('0. thoat')
    while True:
        luachon = nhapSoTuNhien('Lua chon cua ban la: ')
        if luachon < 3: return luachon

def timSoDaiDien(a, m): # Tim so dai dien cua a theo modulo m
    a = int(a)
    while a<0:
        a = a+m 
    return a 

def Tim_SND(m,b):    # Tim b^(-1) mod m
    # Buoc 1
    a1, a2, a3 = 1,0,m 
    b1, b2, b3 = 0,1,b 
    while True:
        # Buoc 2
        if b3 == 0:
            return "khong co"
        # Buoc 3
        if b3 == 1:
            return b2 
        # Buoc 4
        q = a3//b3 
        # Buoc 5
        t1, t2, t3 = (a1-q*b1),(a2-q*b2),(a3-q*b3)
        # Buoc 6
        a1,a2,a3 = b1,b2,b3 
        # Buoc 7
        b1,b2,b3 = t1,t2,t3

def Tim_SND_co_bang(m,b):    
    matran = [['Q', 'A1', 'A2','A3','B1','B2','B3'], ['',1,0,m,0,1,b]]
    ketqua = ''
    while True:
        hang = [] 
        n = len(matran)
        q = matran[n-1][3] // matran[n-1][-1]   # A3//B3
        hang.append(q)
        hang.append(matran[n-1][-3])
        hang.append(matran[n-1][-2])
        hang.append(matran[n-1][-1])
        b1 = matran[n-1][1] - q * matran[n-1][-3]
        b2 = matran[n-1][2] - q * matran[n-1][-2]
        b3 = matran[n-1][3] - q * matran[n-1][-1] 
        hang.append(b1) 
        hang.append(b2)
        hang.append(b3)
        matran.append(hang)  

        if b3==0:
            ketqua = 'khong co'
            break
        if b3==1:
            ketqua = str(b2) 
            break 
    # in bang
    print('Bang:')
    for x in matran:
        for a in x:
            print('%10s'%str(a), end='|')
        print()
    return ketqua


if __name__ == "__main__":
    while True:
        luaChon = showMenu()
        if luaChon==0:
            print('Tam biet')
            break
        elif(luaChon ==1):
            print('Tim so nghich dao cua b theo modulo m')
            b = nhapSoTuNhien("b = ")
            m = nhapSoTuNhien('m = ')
            ketqua = Tim_SND(m,b)
            if ketqua != 'khong co':
                ketqua = timSoDaiDien(ketqua, m) 
            print("Ket qua:", ketqua)
        else:
            print('Tim so nghich dao cua b theo modulo m')
            b = nhapSoTuNhien("b = ")
            m = nhapSoTuNhien('m = ')
            ketqua = Tim_SND_co_bang(m,b)
            if ketqua != 'khong co':
                ketqua = timSoDaiDien(ketqua, m) 
            print("Ket qua:", ketqua)