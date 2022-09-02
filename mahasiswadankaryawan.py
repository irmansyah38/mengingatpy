class Mahasiswa :                # membuat class Mahasiswa
    
    def __init__(self,nama,nim): # membuat fungsi untuk atribut class mahasiswa
        self.nama = nama         # self untuk menunjukan ke sebuah class yaitu mahasiswa sebuah atribut
        self.nim = nim           #
        
class Karyawan :
    
    def __init__(self,nama,jabatan):# membuat fungsi untuk atribut class karyawan
        self.nama = nama # self untuk menunjukan ke sebuah class yaitu mahasiswa sebuah atribut
        self.jabatan = jabatan #        
    
mahasiswa1 = Mahasiswa('irmansyah','J0304211155')#
mahasiswa2 = Mahasiswa('arda','j0304211166')# membuat object dan di simpan di variable
mahasiswa3 = Mahasiswa('irfa','j0304211151')#  

karyawan1 = Karyawan('ahmad','rektor ipb')#
karyawan2 = Karyawan('yusuf','dosen ipb')# membuat object dan di simpan di variable
karyawan3 = Karyawan('yahya','dosen tamu ipb')#

del karyawan3  # menghapus sebuah objek