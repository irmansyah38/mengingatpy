class person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    
    def display(self):
        print('saya adalah '+self.name +" seorang mahasiswa di ipb")
        
p1 = person("irmansyah" , 21)

print(p1.name)
print(p1.age)
p1.display()