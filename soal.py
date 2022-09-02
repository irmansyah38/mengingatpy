class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
    def get_data(self):
        print('{self.real}+{self.imag}j') 
    
num1 = ComplexNumber(2, 3)
num1.get_data()
num1.attr =10
num2 = ComplexNumber(5)
num2.attr = 10
print((num2.real, num2.imag, num2.attr))
print(num1.attr) 

class Mahasiswa:
	def _init_(self,nama,nim):
		self.nama = nama
		self.nim  = nim
		

karim = Mahasiswa("M.kharim Bachtiar","J0304211087")
irmansyah = Mahasiswa("irmansyah","J0304211155")
fikri = Mahasiswa("Fikri Fadilah","J0304211095")

