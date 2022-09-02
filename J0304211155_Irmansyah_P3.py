class Mahasiswa:
    
    jumlahMahasiswa = 0
    
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim
        Mahasiswa.jumlahMahasiswa += 1 
        
    def tampilkanTotalMahasiswa(self):
        print('jumlah mahasiswa adalah '+Mahasiswa.jumlahMahasiswa)
        
    def tampilkanInfoMahasiswa(self):
        print("nama : "+self.nama)
        print("nim : "+ self.nim)
        
mahasiswa1 = Mahasiswa('irmansyah','J0304211155')
mahasiswa2 = Mahasiswa('arda,','J0304211156')
mahasiswa3 = Mahasiswa('karim','j0304211157')


