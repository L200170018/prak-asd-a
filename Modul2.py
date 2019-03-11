print("\n"+"="*25)
print("|Nama : Riyan Aldiansyah|")
print("|NIM  : L200170018      |")
print("|Kelas: A               |")
print("="*25+"\n")



class Pesan():
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self,sebuahString):
        self.teks=sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai",len(self.teks),"karakter")
    def perbarui(self,stringBaru):
        self.teks=stringBaru
    def apakahTerkandung(self,x):
        if x in self.teks:
            print("Terdapat")
        else:
            print("Tidak Terdapat")
    def hitungKonsonan(self):
        konsonan="bcdfghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        jumlahKonsonan=""
        for karakter in self.teks:
            if karakter in konsonan:
                jumlahKonsonan+=karakter
        print(len(jumlahKonsonan))
    def hitungVokal(self):
        vokal="aiueoAIUEO"
        jumlahVokal=""
        for karakter in self.teks:
            if karakter in vokal:
                jumlahVokal+=karakter
        print(len(jumlahVokal))
print("Nomer 1 A")
p9=Pesan("Indonesia adalah negeri yang indah")
p9.apakahTerkandung("ege")
p9.apakahTerkandung("eka")
print("\n"+"Nomer 1 B")
p10=Pesan("Surakarta")
p10.hitungKonsonan()
print("\n"+"Nomer 1 C")
p10.hitungVokal()


class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keaddan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2

p1=Manusia("Riyan")
p1.ucapkanSalam()
        
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    matkul=[]
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupimetode inisiasi di class Manusia."""
        self.nama=nama
        self.NIM=NIM
        self.kotaTinggal=kota
        self.uangsaku=us
    def __str__(self):
        s=self.nama+", NIM "+str(self.NIM)\
           +". Tinggal di " +self.kotaTinggal \
           +". Uang saku Rp."+str(self.uangsaku)\
           +" tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangsaku
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,k):
        self.kotaTinggal=k
    def tambahUangSaku(self,t):
        self.uangsaku+=t
    def ambilMK(self, mk):
        self.matkul.append(mk)
    def listKuliah(self):
        print(self.matkul)
    def hapusMataKuliah(self, mk):
        return self.matkul.remove(mk)


m9=Mahasiswa("Riyan","L200170018","Sukoharjo",500000)

print("\n"+"Nomer 2"+"\n",m9)
print("nomer 2 A,",m9.ambilKotaTinggal())
m9.perbaruiKotaTinggal("Sleman")
print("nomer 2 B,",m9.ambilKotaTinggal())
print("nomer 2 C,",m9.ambilUangSaku())
m9.tambahUangSaku(50000)
print("          ",m9.ambilUangSaku())


print("\n"+"Nomer 3")
nama = input("Masukkan Nama Anda      : ")
NIM  = input("Masukkan NIM Anda       :")
kota = input("Masukkan Kota Asal Anda :")
us   = input("Masukkan Uang Saku Anda :")
m2 = Mahasiswa(nama,NIM,kota,us)
print(m2)

print("\n"+"Nomer 4")
print(m9)
m9.listKuliah()
m9.ambilMK("Matematika Diskrit")
m9.listKuliah()
m9.ambilMK("Algoritma dan Struktur Data")
m9.listKuliah()

print("\n"+"Nomer 5")
m9.hapusMataKuliah("Matematika Diskrit")
m9.listKuliah()

print("\n"+"Nomer 6")
class SiswaSMA(Manusia):
    jurusan = "Belum Ditentukan"
    univ = "Belum Ditentukan"
    def __init__(self, nama, nisn, sma):
        self.nama = nama
        self.nisn = nisn
        self.sma = sma
    def __str__(self):
        return "Data Diri\n"\
               +"Nama            : "+self.nama\
               +"\nNISN            : "+str(self.nisn)\
               +"\nSMA             : "+self.sma\
               +"\nUniv Pilihan    : "+self.univ\
               +"\nJurusan Pilihan : "+self.jurusan
    def ambil(self):
        print("\n\nUpdate Data Universitas Pilihan...")
        self.univ = input("Pilih Univ : ")
        self.jurusan = input("Ambil Jurusan : ")


sis = SiswaSMA("Saya","727387238","SMANSA")
print(sis)
sis.ambil()
print(sis)

print("\n"+"Nomer 7")
class MhsTIF(Mahasiswa):    
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def kataKanPy(self):
        print('Python is cool.')













    
