print("\n"+"="*25)
print("|Nama : Riyan Aldiansyah|")
print("|NIM  : L200170018      |")
print("|Kelas: A               |")
print("="*25+"\n")

#Nomer1
def cetakSiku(x):
    string = ""
    bar = 1
    while bar <= x:
        kol = bar
        while kol > 0:
            string = string + " * "
            kol = kol - 1
        string = string + "\n"
        bar = bar + 1
    print(string)
print("Nomer 1")
cetakSiku(5)
print("\n")

#Nomer2
def gambarlahPesegiEmpat(A,B):
    for i in range(A):
        if(i==0 or i==A-1):
            print("@"*B)
        else:
            print("@"+" "*(B-2)+"@")
print("Nomer 2")    
gambarlahPesegiEmpat(5,6)
print("\n")

#Nomer3
def JHV(k):
    jumlahvokal=""
    vokal="AIUEOaiueo"
    for karakter in k:
        if karakter in vokal:
            jumlahvokal+=karakter
    print((len(jumlahvokal),len(k)))
print("Nomer 3 A")
JHV("Surakarta")
print("Nomer 3 B")
def JHK(k):
    konsonan="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    jumlahkonsonan=""
    for karakter in k:
        if karakter in konsonan:
            jumlahkonsonan+=karakter
    print((len(jumlahkonsonan),len(k)))
JHK("Surakarta")
print("\n")

#Nomer4
print("Nomer 4")
def rerata(b=[]):
    x=0
    n=0
    if b != []:
        for i in b:
            x+=i
            n+=1
        return x/n
z=rerata([1,2,3,4,5])
print(z)

g=[3,4,5,4,3,4,5,2,2,10,11,23]
w=rerata(g)
print(w)
print("\n")

#Nomer 5
print("Nomer 5")
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))
print("\n")

#Nomer 6
print("Nomer 6")
def bilanganprima():
    prima=list()
    for i in range(2,100):
        x = True
        for iter in prima:
            if(i%iter==0):
                x=False
                break
        if(x):
            print(i)
            prima.append(i)
bilanganprima()
print("\n")

#Nomer 7
print("Nomer 7")
def faktorPrima(n):
    prima=list()
    for i in range(2,n):
        x = True
        for iter in prima:
            if(i%iter==0):
                x=False
                break
        if x and n%i==0:
            prima.append(i)
    return prima
print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))
print("\n")

#Nomer 8
print("Nomer 8")
def apakahTerkandung(a,b):
    return a in b
h ="do"
k ="Indonesia tanah air kita"
print(apakahTerkandung(h,k))
print(apakahTerkandung("pusaka",k))
print("\n")

#Nomer 9
print("Nomer 9")
def coba():
    for x in range(1,100):
        if (x%3)!=0 and (x%5)!=0:
            print(x)
        else:
            if (x%15)==0:
                print("PYTHON UMS")
            elif (x%3)==0:
                print("python")
            elif (x%5)==0:
                print("UMS")
coba()
print("\n")

#Nomer 10
print("Nomer 10")
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    d=(b**2)-(4*a*c)
    if d<0:
        return "determinan negatif. Persamaan tidak mempunyai akar real"
    return  "determinanpositif. Persamaan mempunyai akar real"
print(selesaikanABC(1,2,3))
print("\n")

#Nomer 11
print("Nomer 11")
def apakahkabisat(x):
    if(x%400==0):
        return True
    if(x%100==0):
        return False
    if(x%4==0):
        return True
    return False
print(apakahkabisat(2400))
print("\n")

#Nomer 12
print("Nomer 12")
import random
def permainanTA():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("masukan angka: "))
        if(b>a):
            print("itu terlalu besar,coba lagi")
        elif(b<a):
            print("itu terlalu kecil,coba lagi")
        else:
            print("benar")
            break
print("belum dimasukan Perintah 'permainanTA'")
print("\n")

#Nomer 13
print("Nomer 13")
def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",-6:"ratus ",-7:"juta ",8:"puluhjuta "}
    b=str(a)
    z=""
    i=-1
    while i>= -len(b):
        z=x[b[i]]+y[i]+z
        i-=1
    return z
print(katakan(3125750))
print("\n")

#Nomer 14
print("Nomer 14")
def formatRupiah(x):
    y=str(x)
    z=""
    i = -1
    while i>= -len(y):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+z
        z=y[i]+z
        i-=1
    return "'"+"Rp "+z+"'"
print(formatRupiah(1500))
print(formatRupiah(2560000))


















